import React, { useEffect, useState } from "react";
import axios from "axios";

const API_URL = process.env.REACT_APP_API_URL;

function App() {
  const [message, setMessage] = useState("");

  useEffect(() => {
    axios.get(API_URL)
      .then(res => setMessage(res.data.message))
      .catch(err => console.error(err));
  }, []);

  return (
    <div style={{ padding: 40 }}>
      <h1>Stock Reposición App</h1>
      <p>{message}</p>
    </div>
  );
}

export default App;