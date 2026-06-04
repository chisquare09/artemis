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
