import pytest

from app.core.exceptions import NotFoundException
from app.modules.ai.orchestrator import AIOrchestrator
from app.modules.ai.providers.fake_provider import FakeAIProvider


def test_explain_lesson_a1_5():
    orchestrator = AIOrchestrator(FakeAIProvider())
    result = orchestrator.explain_lesson("A1.5")
    assert "A1.5" in result["explanation"] or "Food" in result["explanation"]


def test_explain_lesson_includes_context():
    orchestrator = AIOrchestrator(FakeAIProvider())
    result = orchestrator.explain_lesson("A1.5")
    assert result["used_context"]["unit_code"] == "A1.5"
    assert "objectives" in result["used_context"]


def test_answer_question_a1_5():
    orchestrator = AIOrchestrator(FakeAIProvider())
    result = orchestrator.answer_lesson_question("A1.5", "How do I ask for the bill?")
    assert result["unit_code"] == "A1.5"
    assert result["answer"]


def test_unknown_unit_raises():
    orchestrator = AIOrchestrator(FakeAIProvider())
    with pytest.raises(NotFoundException):
        orchestrator.explain_lesson("UNKNOWN")
