import React, { useState } from "react";

export function TodoList() {
  const [todos, setTodos] = useState([]);
  const [input, setInput] = useState("");

  const addTodo = () => {
    if (!input.trim()) return;
    setTodos([...todos, input.trim()]);
    setInput("");
  };

  return (
    <div>
      <input
        placeholder="Novo item"
        value={input}
        onChange={(e) => setInput(e.target.value)}
      />
      <button onClick={addTodo}>Adicionar</button>
      {todos.length === 0 ? (
        <p data-testid="empty">Nenhum item</p>
      ) : (
        <ul>
          {todos.map((t, i) => (
            <li key={i}>{t}</li>
          ))}
        </ul>
      )}
    </div>
  );
}
