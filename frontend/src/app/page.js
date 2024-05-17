'use client';
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import Form from './components/Form';

function App() {
  const [result, setResult] = useState(null);
  const [error, setError] = useState('');

  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    try {
      const response = await axios.get('http://127.0.0.1:5000/endpoint');
      setResult(response.data); // response.data contains the JSON object
    } catch (error) {
      setError('Error fetching data');
      console.error('Error:', error);
    }
  };

  return (
    <div>
      <h1>Result:</h1>
      {result ? <p>{result.message}</p> : <p>Loading...</p>}
      {error && <p>{error}</p>}
      <Form />
    </div>
  );
}

export default App;
