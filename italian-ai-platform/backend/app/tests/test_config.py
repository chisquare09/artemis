from app.core.config import get_settings


def test_settings_load():
    settings = get_settings()
    assert settings is not None


def test_default_app_env():
    settings = get_settings()
    assert settings.APP_ENV == "development"
