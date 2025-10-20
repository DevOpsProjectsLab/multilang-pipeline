import { render, screen, fireEvent } from "@testing-library/react";
import App from "../../src/App";

test("fluxo completo: contador + todo list", () => {
  render(<App />);

  // Counter
  fireEvent.click(screen.getByText("Incrementar"));
  expect(screen.getByTestId("value").textContent).toBe("Contagem: 1");

  // TodoList
  fireEvent.change(screen.getByPlaceholderText("Novo item"), {
    target: { value: "Estudar Matrix CI" },
  });
  fireEvent.click(screen.getByText("Adicionar"));
  expect(screen.getByText("Estudar Matrix CI")).toBeInTheDocument();
});
