'use client'
import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
  const [result, setResult] = useState('');

  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    try {
      const response = await axios.get('http://127.0.0.1:5000');
      setResult(response.data);
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <div>
      <h1>Result:</h1>
      <p>{result}</p>
    </div>
  );
}

export default App;
