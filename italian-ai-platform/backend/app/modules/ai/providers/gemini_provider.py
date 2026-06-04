from app.modules.ai.providers.base import AIProvider


class ProviderNotConfiguredError(Exception):
    pass


class GeminiProvider(AIProvider):
    name = "gemini"

    def __init__(self, api_key: str | None = None):
        self._api_key = api_key

    def _check_key(self):
        if not self._api_key:
            raise ProviderNotConfiguredError("GEMINI_API_KEY is not configured")

    def generate_text(self, prompt: str, context: dict | None = None) -> str:
        self._check_key()
        raise NotImplementedError("Gemini provider not yet implemented")

    def generate_json(self, prompt: str, schema_hint: dict | None = None, context: dict | None = None) -> dict:
        self._check_key()
        raise NotImplementedError("Gemini provider not yet implemented")
