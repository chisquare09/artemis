from app.modules.ai.providers.base import AIProvider


class FakeAIProvider(AIProvider):
    name = "fake"

    def generate_text(self, prompt: str, context: dict | None = None) -> str:
        unit_code = context.get("unit_code", "unknown") if context else "unknown"
        title = context.get("title", "Lesson") if context else "Lesson"

        if "explain" in prompt.lower():
            return (
                f"This is {unit_code} — {title}. "
                "In this lesson you will learn about ordering food and drinks, "
                "asking prices, asking for the bill, and expressing likes and dislikes. "
                "Practice with Italian café vocabulary and common restaurant phrases."
            )

        if "question" in prompt.lower() or "answer" in prompt.lower():
            question = context.get("question", "") if context else ""
            return f"For {unit_code}, regarding your question: {question[:50]}... The answer involves Italian vocabulary from this lesson."

        return f"Fake response for {unit_code}."

    def generate_json(self, prompt: str, schema_hint: dict | None = None, context: dict | None = None) -> dict:
        return {"status": "ok", "provider": self.name, "data": "fake_json_response"}
