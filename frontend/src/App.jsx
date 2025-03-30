import React, { useState } from "react";
import { motion } from "framer-motion";
import { Button } from "./components/ui/button";
import { Input } from "./components/ui/input";

export default function App() {
  const [input, setInput] = useState("");
  const [response, setResponse] = useState("");

  const handleSend = async () => {
    if (!input) return;
    setResponse("Thinking... 🤔");

    const res = await fetch("https://jarvis-ai-breq.onrender.com/speak", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text: input }),
    });
    const data = await res.json();
    setResponse(data.message);
  };

  return (
    <div className="flex flex-col items-center justify-center h-screen bg-gray-900 text-white">
      <motion.h1
        initial={{ opacity: 0, y: -20 }}
        animate={{ opacity: 1, y: 0 }}
        className="text-4xl font-bold mb-4"
      >
        Jarvis AI
      </motion.h1>

      <div className="flex gap-2">
        <Input
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Ask Jarvis..."
          className="p-3 rounded-lg text-black"
        />
        <Button onClick={handleSend} className="bg-blue-500 hover:bg-blue-600">
          Send
        </Button>
      </div>

      {response && (
        <motion.p
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          className="mt-4 text-lg"
        >
          {response}
        </motion.p>
      )}
    </div>
  );
}
