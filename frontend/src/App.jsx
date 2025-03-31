const handleSend = async () => {
  try {
      const response = await fetch("http://127.0.0.1:8000/speak", {  // ✅ Flask Localhost URL
          method: "POST",
          headers: {
              "Content-Type": "application/json"
          },
          body: JSON.stringify({ text: "Hello, Jarvis!" }),
      });

      if (!response.ok) {
          throw new Error("Failed to fetch");
      }

      const data = await response.json();
      console.log("Response:", data);
  } catch (error) {
      console.error("Error:", error);
  }
};
