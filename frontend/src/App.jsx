import React, { useState } from "react";
import axios from "axios";

function App() {
  const [file, setFile] = useState(null);
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");

  const handleUpload = async () => {
    const formData = new FormData();
    formData.append("file", file);
    await axios.post("/api/upload/", formData, {
      baseURL: "http://localhost:8000",
      headers: { "Content-Type": "multipart/form-data" },
    });
    alert("File uploaded!");
  };

  const handleAsk = async () => {
    const res = await axios.get("/api/query/", {
      baseURL: "http://localhost:8000",
      params: { q: question },
    });
    setAnswer(res.data.answer);
  };

  return (
    <div style={{maxWidth: 600, margin: "auto", padding: 32}}>
      <h1>Multimodal Personal Knowledge Base Agent</h1>
      <h2>Upload Note/Diagram/Paper/Code</h2>
      <input type="file" onChange={e => setFile(e.target.files[0])} />
      <button onClick={handleUpload} disabled={!file}>Upload</button>
      <hr />
      <h2>Ask a Question</h2>
      <input
        style={{width: "100%"}}
        placeholder='e.g. What was my last project’s evaluation metric and what was the score?'
        value={question}
        onChange={e => setQuestion(e.target.value)}
      />
      <button onClick={handleAsk} disabled={!question}>Ask</button>
      {answer && (
        <div style={{marginTop: 16}}>
          <b>Answer:</b>
          <div>{answer}</div>
        </div>
      )}
    </div>
  );
}

export default App;
