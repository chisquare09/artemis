from abc import ABC, abstractmethod


class AIProvider(ABC):
    name: str = "base"

    @abstractmethod
    def generate_text(self, prompt: str, context: dict | None = None) -> str:
        pass

    @abstractmethod
    def generate_json(self, prompt: str, schema_hint: dict | None = None, context: dict | None = None) -> dict:
        pass
