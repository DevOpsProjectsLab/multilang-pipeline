from fastapi import FastAPI, HTTPException
from .repo import InMemoryTodoRepo
from .models import Todo
from .schemas import TodoIn, TodoOut

app = FastAPI(title="Todos API", version="1.0.0")
repo = InMemoryTodoRepo()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/todos", response_model=TodoOut, status_code=201)
def create_todo(payload: TodoIn):
    try:
        todo = Todo.create(payload.title)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    repo.add(todo)
    return todo

@app.get("/todos", response_model=list[TodoOut])
def list_todos():
    return repo.list()

@app.get("/todos/{todo_id}", response_model=TodoOut)
def get_todo(todo_id: str):
    todo = repo.get(todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Not found")
    return todo

@app.post("/todos/{todo_id}/done", response_model=TodoOut)
def mark_done(todo_id: str):
    todo = repo.mark_done(todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Not found")
    return todo
