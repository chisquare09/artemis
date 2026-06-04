from app.core.config import get_settings
from app.modules.ai.orchestrator import AIOrchestrator
from app.modules.ai.providers.fake_provider import FakeAIProvider

_orchestrator: AIOrchestrator | None = None


def get_orchestrator() -> AIOrchestrator:
    global _orchestrator
    if _orchestrator is None:
        settings = get_settings()
        # Default to FakeAIProvider in development when no keys configured
        provider = FakeAIProvider()
        _orchestrator = AIOrchestrator(provider)
    return _orchestrator
