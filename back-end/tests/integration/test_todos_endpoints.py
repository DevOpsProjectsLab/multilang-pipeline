from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}

def test_cria_lista_busca_conclui_fluxo():
    # cria
    r = client.post("/todos", json={"title": "integrar pipeline"})
    assert r.status_code == 201
    created = r.json()
    assert created["title"] == "integrar pipeline"
    todo_id = created["id"]

    # lista
    r = client.get("/todos")
    assert r.status_code == 200
    assert any(t["id"] == todo_id for t in r.json())

    # busca por id
    r = client.get(f"/todos/{todo_id}")
    assert r.status_code == 200
    assert r.json()["id"] == todo_id

    # conclui
    r = client.post(f"/todos/{todo_id}/done")
    assert r.status_code == 200
    assert r.json()["done"] is True

def test_cria_todo_invalido_retorna_400():
    r = client.post("/todos", json={"title": "   "})
    assert r.status_code == 400
    assert r.json()["detail"]  # mensagem de erro do ValueError

def test_get_todo_inexistente_404():
    r = client.get("/todos/nao-existe")
    assert r.status_code == 404
    assert r.json()["detail"] == "Not found"

def test_mark_done_inexistente_404():
    r = client.post("/todos/nao-existe/done")
    assert r.status_code == 404
    assert r.json()["detail"] == "Not found"