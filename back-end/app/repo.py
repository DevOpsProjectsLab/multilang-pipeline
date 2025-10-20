from typing import Dict, List, Optional
from .models import Todo

class InMemoryTodoRepo:
    def __init__(self):
        self._db: Dict[str, Todo] = {}

    def add(self, todo: Todo) -> Todo:
        self._db[todo.id] = todo
        return todo

    def get(self, todo_id: str) -> Optional[Todo]:
        return self._db.get(todo_id)

    def list(self) -> List[Todo]:
        return list(self._db.values())

    def mark_done(self, todo_id: str) -> Optional[Todo]:
        todo = self._db.get(todo_id)
        if not todo:
            return None
        done = todo.mark_done()
        self._db[todo_id] = done
        return done
