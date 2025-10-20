import { render, screen, fireEvent } from "@testing-library/react";
import { Counter } from "../../src/components/Counter";

test("incrementa e reseta contagem", () => {
  render(<Counter />);
  const valor = screen.getByTestId("value");
  expect(valor.textContent).toBe("Contagem: 0");

  fireEvent.click(screen.getByText("Incrementar"));
  expect(valor.textContent).toBe("Contagem: 1");

  fireEvent.click(screen.getByText("Resetar"));
  expect(valor.textContent).toBe("Contagem: 0");
});
