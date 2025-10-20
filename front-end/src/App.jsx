import React from "react";
import { Counter } from "./components/Counter";
import { TodoList } from "./components/TodoList";

export default function App() {
  return (
    <div>
      <h1>App Frontend Isolado</h1>
      <Counter />
      <hr />
      <TodoList />
    </div>
  );
}
