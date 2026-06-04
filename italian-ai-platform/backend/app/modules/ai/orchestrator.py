from pathlib import Path

from app.modules.ai.providers.base import AIProvider
from app.modules.lessons.content_builder import build_lesson_detail

PROMPTS_DIR = Path(__file__).parent / "prompts"

MODE_CONTEXT = {
    "daily_communication": "Focus on practical conversation, real-life interaction, and everyday usage.",
    "academic_purpose": "Focus on grammar accuracy, structured practice, reading/writing, and exam-style preparation.",
}


def _load_prompt(name: str) -> str:
    return (PROMPTS_DIR / f"{name}.txt").read_text()


def _format_objectives(objectives: dict[str, list[str]]) -> str:
    lines = []
    for category, items in objectives.items():
        lines.append(f"- {category}: {', '.join(items)}")
    return "\n".join(lines)


class AIOrchestrator:
    def __init__(self, provider: AIProvider):
        self._provider = provider

    def explain_lesson(self, unit_code: str, study_mode: str | None = None) -> dict:
        mode = study_mode or "daily_communication"
        lesson = build_lesson_detail(unit_code, mode)
        mode_guidance = MODE_CONTEXT.get(mode, MODE_CONTEXT["daily_communication"])

        context = {
            "unit_code": lesson.unit_code,
            "level": lesson.level,
            "title": lesson.title,
            "summary": lesson.summary or "",
            "objectives": lesson.objectives,
            "study_mode": mode,
            "mode_guidance": mode_guidance,
        }
        prompt_template = _load_prompt("explain_lesson")
        prompt = prompt_template.format(
            unit_code=lesson.unit_code,
            title=lesson.title,
            level=lesson.level,
            summary=lesson.summary or "",
            objectives=_format_objectives(lesson.objectives),
        ) + f"\n\nStudy mode: {mode}. {mode_guidance}"

        explanation = self._provider.generate_text(prompt, context)
        return {
            "unit_code": unit_code,
            "provider": self._provider.name,
            "explanation": explanation,
            "used_context": context,
        }

    def answer_lesson_question(self, unit_code: str, question: str, study_mode: str | None = None) -> dict:
        mode = study_mode or "daily_communication"
        lesson = build_lesson_detail(unit_code, mode)
        mode_guidance = MODE_CONTEXT.get(mode, MODE_CONTEXT["daily_communication"])

        # Retrieve relevant material chunks
        retrieved_chunks = []
        try:
            from app.modules.rag.retriever import retrieve_chunks
            chunks = retrieve_chunks(unit_code, question, limit=3)
            retrieved_chunks = [{"content": c["content"], "source": c["material_title"]} for c in chunks]
        except Exception:
            pass

        context = {
            "unit_code": lesson.unit_code,
            "level": lesson.level,
            "title": lesson.title,
            "summary": lesson.summary or "",
            "objectives": lesson.objectives,
            "question": question,
            "retrieved_chunks": retrieved_chunks,
            "study_mode": mode,
            "mode_guidance": mode_guidance,
        }

        material_context = ""
        if retrieved_chunks:
            material_context = "\n\nRelevant learning materials:\n" + "\n".join(f"- {c['content']}" for c in retrieved_chunks)

        prompt_template = _load_prompt("answer_question")
        prompt = prompt_template.format(
            unit_code=lesson.unit_code,
            title=lesson.title,
            level=lesson.level,
            summary=lesson.summary or "",
            objectives=_format_objectives(lesson.objectives),
            question=question,
        ) + material_context + f"\n\nStudy mode: {mode}. {mode_guidance}"

        answer = self._provider.generate_text(prompt, context)
        return {
            "unit_code": unit_code,
            "provider": self._provider.name,
            "answer": answer,
            "used_context": context,
        }
