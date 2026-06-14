from app.core.config import get_settings
from app.modules.ai.orchestrator import AIOrchestrator
from app.modules.ai.providers.fake_provider import FakeAIProvider
from app.modules.ai.providers.gemini_provider import GeminiProvider

_orchestrator: AIOrchestrator | None = None


def _build_provider():
    settings = get_settings()
    provider_mode = settings.AI_PROVIDER.lower()

    if provider_mode == "fake":
        return FakeAIProvider()

    if provider_mode in {"auto", "gemini"} and settings.GEMINI_API_KEY:
        return GeminiProvider(settings.GEMINI_API_KEY, settings.GEMINI_MODEL)

    return FakeAIProvider()


def reset_orchestrator_for_tests() -> None:
    global _orchestrator
    _orchestrator = None


def get_orchestrator() -> AIOrchestrator:
    global _orchestrator
    if _orchestrator is None:
        _orchestrator = AIOrchestrator(_build_provider())
    return _orchestrator
