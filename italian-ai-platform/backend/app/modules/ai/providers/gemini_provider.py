import json
from typing import Any

from app.modules.ai.providers.base import AIProvider


class ProviderNotConfiguredError(Exception):
    pass


class GeminiProvider(AIProvider):
    name = "gemini"

    def __init__(self, api_key: str | None = None, model: str = "gemini-3.5-flash"):
        self._api_key = api_key
        self._model = model
        self._client = None

    def _check_key(self) -> None:
        if not self._api_key:
            raise ProviderNotConfiguredError("GEMINI_API_KEY is not configured")

    def _get_client(self):
        self._check_key()
        if self._client is None:
            from google import genai

            self._client = genai.Client(api_key=self._api_key)
        return self._client

    def generate_text(self, prompt: str, context: dict | None = None) -> str:
        client = self._get_client()
        response = client.models.generate_content(
            model=self._model,
            contents=prompt,
        )
        text = getattr(response, "text", None)
        if not text:
            raise RuntimeError("Gemini returned an empty response")
        return text.strip()

    def generate_json(self, prompt: str, schema_hint: dict | None = None, context: dict | None = None) -> dict[str, Any]:
        json_prompt = prompt
        if schema_hint:
            json_prompt += (
                "\n\nReturn only valid JSON. Do not wrap it in markdown. "
                f"Use this schema hint: {json.dumps(schema_hint)}"
            )
        else:
            json_prompt += "\n\nReturn only valid JSON. Do not wrap it in markdown."

        text = self.generate_text(json_prompt, context)
        cleaned = text.strip()
        if cleaned.startswith("```"):
            cleaned = cleaned.strip("`")
            if cleaned.lower().startswith("json"):
                cleaned = cleaned[4:].strip()
        try:
            return json.loads(cleaned)
        except json.JSONDecodeError as exc:
            raise RuntimeError(f"Gemini returned invalid JSON: {text[:500]}") from exc
