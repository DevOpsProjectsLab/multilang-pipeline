from app.repo import InMemoryTodoRepo
from app.models import Todo

def test_add_get_list():
    repo = InMemoryTodoRepo()
    t = Todo.create("coisa")
    repo.add(t)
    assert repo.get(t.id) == t
    assert t in repo.list()

def test_mark_done():
    repo = InMemoryTodoRepo()
    t = repo.add(Todo.create("coisa"))
    done = repo.mark_done(t.id)
    assert done and done.done is True
    assert repo.get(t.id).done is True

def test_mark_done_id_inexistente():
    repo = InMemoryTodoRepo()
    assert repo.mark_done("nao-existe") is None
