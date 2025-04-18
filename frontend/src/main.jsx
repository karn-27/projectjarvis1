import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App"; // Make sure App.js is imported
import "./index.css"; // Ensure Tailwind is included

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
