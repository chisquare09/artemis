from app.shared.enums import CEFRLevel, Skill, StudyMode


def test_study_mode_value():
    assert StudyMode.daily_communication.value == "daily_communication"


def test_cefr_level_value():
    assert CEFRLevel.A1.value == "A1"


def test_skill_value():
    assert Skill.listening.value == "listening"
