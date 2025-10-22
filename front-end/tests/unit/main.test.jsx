import { describe, it, vi, expect } from "vitest";

vi.mock("react-dom/client", () => {
  const createRoot = vi.fn(() => ({
    render: vi.fn(),
  }));
  return {
    createRoot,
    default: { createRoot },
  };
});

describe("main.jsx", () => {
  it("monta o App no elemento root", async () => {
    const root = document.createElement("div");
    root.id = "root";
    document.body.appendChild(root);

    await import("../../src/main.jsx");

    const ReactDOM = await import("react-dom/client");
    expect(ReactDOM.createRoot).toHaveBeenCalled();
  });
});
