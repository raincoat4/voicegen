// components/Form.js
import { useState } from 'react';

export default function Form() {
  const [inputValue, setInputValue] = useState('');

  const handleSubmit = async (event) => {
    event.preventDefault();
    
    const response = await fetch('./api/send-input', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ inputValue }),
    });

    if (response.ok) {
      // Handle successful response
      console.log('Input sent successfully');
    } else {
      // Handle error response
      console.error('Error sending input');
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <label>
        Input:
        <input
          type="text"
          value={inputValue}
          onChange={(e) => setInputValue(e.target.value)}
          className = "text-black"
        />
      </label>
      <button type="submit">Submit</button>
    </form>
  );
}
