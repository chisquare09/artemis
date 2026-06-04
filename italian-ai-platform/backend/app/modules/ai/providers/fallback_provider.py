from app.modules.ai.providers.base import AIProvider


class FallbackAIProvider(AIProvider):
    name = "fallback"

    def __init__(self, providers: list[AIProvider]):
        if not providers:
            raise ValueError("FallbackAIProvider requires at least one provider")
        self._providers = providers

    def generate_text(self, prompt: str, context: dict | None = None) -> str:
        errors = []
        for provider in self._providers:
            try:
                result = provider.generate_text(prompt, context)
                self.name = f"fallback({provider.name})"
                return result
            except Exception as e:
                errors.append(f"{provider.name}: {e}")
        raise RuntimeError(f"All providers failed: {'; '.join(errors)}")

    def generate_json(self, prompt: str, schema_hint: dict | None = None, context: dict | None = None) -> dict:
        errors = []
        for provider in self._providers:
            try:
                result = provider.generate_json(prompt, schema_hint, context)
                self.name = f"fallback({provider.name})"
                return result
            except Exception as e:
                errors.append(f"{provider.name}: {e}")
        raise RuntimeError(f"All providers failed: {'; '.join(errors)}")
