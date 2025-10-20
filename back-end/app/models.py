from dataclasses import dataclass, field
from typing import Optional
import uuid

@dataclass(frozen=True)
class Todo:
    id: str
    title: str
    done: bool = False

    @staticmethod
    def create(title: str) -> "Todo":
        title = (title or "").strip()
        if not title:
            raise ValueError("title não pode ser vazio")
        return Todo(id=str(uuid.uuid4()), title=title, done=False)

    def mark_done(self) -> "Todo":
        return Todo(id=self.id, title=self.title, done=True)
