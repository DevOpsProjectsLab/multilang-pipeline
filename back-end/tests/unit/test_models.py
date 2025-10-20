import pytest
from app.models import Todo

def test_create_todo_ok():
    t = Todo.create("  estudar CI  ")
    assert t.title == "estudar CI"
    assert t.done is False
    assert isinstance(t.id, str)

def test_create_todo_title_vazio():
    with pytest.raises(ValueError):
        Todo.create("   ")

def test_mark_done_retorna_novo_objeto():
    t1 = Todo.create("x")
    t2 = t1.mark_done()
    assert t1 is not t2
    assert t1.done is False
    assert t2.done is True
