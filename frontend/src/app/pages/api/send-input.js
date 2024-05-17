// pages/api/send-input.js
export default async function handler(req, res) {
    if (req.method === 'POST') {
      const { inputValue } = req.body;
  
      // Send the input to your Python backend
      const response = await fetch('http://127.0.0.1:5000/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ inputValue }),
      });
  
      if (response.ok) {
        res.status(200).json({ message: 'Input sent successfully' });
      } else {
        res.status(response.status).json({ message: 'Error sending input' });
      }
    } else {
      res.status(405).json({ message: 'Method not allowed' });
    }
  }
  