import React, { useState, useRef } from 'react';
import axios from 'axios';

export default function Form() {
  const [recording, setRecording] = useState(false);
  const [audioBlob, setAudioBlob] = useState(null);
  const [responseData, setResponseData] = useState('')
  const mediaRecorderRef = useRef(null);
  const audioChunksRef = useRef([]);

  const startRecording = async () => {
    const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
    mediaRecorderRef.current = new MediaRecorder(stream);
    audioChunksRef.current = [];

    mediaRecorderRef.current.ondataavailable = event => {
      audioChunksRef.current.push(event.data);
    };

    mediaRecorderRef.current.onstop = () => {
      const audioBlob = new Blob(audioChunksRef.current, { type: 'audio/wav' });
      setAudioBlob(audioBlob);
    };

    mediaRecorderRef.current.start();
    setRecording(true);
  };

  const stopRecording = () => {
    mediaRecorderRef.current.stop();
    setRecording(false);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!audioBlob) {
      alert('Please record audio first!');
      return;
    }

    const formData = new FormData();
    formData.append('file', audioBlob, 'recording.wav');

    try {
      const response = await axios.post('http://127.0.0.1:5000/upload', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });
      console.log(response.data.result[0]);
      setResponseData(response.data.result[0])
    } catch (error) {
      console.error('Error uploading audio file:', error);
    }
  };

  return (
    <>
      <button onClick={recording ? stopRecording : startRecording}>
        {recording ? 'Stop Recording' : 'Start Recording'}
      </button>
      <form onSubmit={handleSubmit}>
        <button type="submit">Submit</button>
      </form>
      <div>
        {responseData === '' ? <p>send a recording</p> : responseData === 0 ? <p>male</p> : <p>female</p>}
      </div>
    </>
  );
}
