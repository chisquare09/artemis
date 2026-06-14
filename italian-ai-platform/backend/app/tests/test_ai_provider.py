from app.modules.ai.providers.fake_provider import FakeAIProvider
from app.modules.ai.providers.fallback_provider import FallbackAIProvider


def test_fake_provider_generate_text():
    provider = FakeAIProvider()
    result = provider.generate_text("explain", {"unit_code": "A1.5", "title": "Food"})
    assert "A1.5" in result


def test_fake_provider_generate_json():
    provider = FakeAIProvider()
    result = provider.generate_json("test", {})
    assert "status" in result
    assert result["provider"] == "fake"


def test_gemini_provider_import_no_crash():
    from app.modules.ai.providers.gemini_provider import GeminiProvider
    provider = GeminiProvider()
    assert provider.name == "gemini"


def test_groq_provider_import_no_crash():
    from app.modules.ai.providers.groq_provider import GroqProvider
    provider = GroqProvider()
    assert provider.name == "groq"


def test_fallback_provider_uses_fake():
    fake = FakeAIProvider()
    fallback = FallbackAIProvider([fake])
    result = fallback.generate_text("explain", {"unit_code": "A1.5", "title": "Food"})
    assert "A1.5" in result


def test_gemini_provider_generate_text_with_mock_client(monkeypatch):
    from google import genai
    from app.modules.ai.providers.gemini_provider import GeminiProvider

    class FakeResponse:
        text = "Gemini text"

    class FakeModels:
        def generate_content(self, model, contents):
            assert model == "test-model"
            assert contents == "prompt"
            return FakeResponse()

    class FakeClient:
        models = FakeModels()

    monkeypatch.setattr(genai, "Client", lambda api_key: FakeClient())
    provider = GeminiProvider("test-key", "test-model")
    assert provider.generate_text("prompt") == "Gemini text"


def test_ai_service_uses_gemini_when_key_exists(monkeypatch):
    from types import SimpleNamespace
    from app.modules.ai import service as ai_service

    monkeypatch.setattr(
        ai_service,
        "get_settings",
        lambda: SimpleNamespace(AI_PROVIDER="auto", GEMINI_API_KEY="test-key", GEMINI_MODEL="test-model"),
    )
    ai_service.reset_orchestrator_for_tests()
    orchestrator = ai_service.get_orchestrator()
    assert orchestrator._provider.name == "gemini"
    ai_service.reset_orchestrator_for_tests()
