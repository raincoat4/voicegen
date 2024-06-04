import { useState, useEffect } from 'react';

export default function Form() {
  const [inputValue, setInputValue] = useState('');
  const [data, setData] = useState('');
  const [submitted, setSubmitted] = useState(false);

  useEffect(() => {
    if (submitted) {
      fetch('http://127.0.0.1:5000/backend', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ inputValue })
      })
        .then(response => response.json()) // Assuming the backend returns JSON
        .then(data => {
          setData(data);
          console.log(data);
        })
        .catch(error => {
          console.error('Error fetching data:', error);
        })
        .finally(() => {
          setSubmitted(false); // Reset submission state
        });
    }
  }, [submitted, inputValue]);

  const handleSubmit = (e) => {
    e.preventDefault(); // Prevent default form submission
    setSubmitted(true);
  };

  return (
    <>
      <form onSubmit={handleSubmit}>
        <label>
          Input:
          <input
            type="text"
            className="text-black"
            value={inputValue}
            onChange={(e) => setInputValue(e.target.value)}
          />
        </label>
        <button type="submit">Submit</button>
      </form>
      {data === '' ? <p>no data submitted</p> : <p>{JSON.stringify(data)}</p>}
    </>
  );
}
