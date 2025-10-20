import { render, screen, fireEvent } from "@testing-library/react";
import { TodoList } from "../../src/components/TodoList";

test("adiciona item na lista", () => {
  render(<TodoList />);
  fireEvent.change(screen.getByPlaceholderText("Novo item"), {
    target: { value: "Aprender CI/CD" },
  });
  fireEvent.click(screen.getByText("Adicionar"));
  expect(screen.getByText("Aprender CI/CD")).toBeInTheDocument();
});
