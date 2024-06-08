import React, { useState, useRef } from 'react';
import axios from 'axios';

export default function Form() {
  const [recording, setRecording] = useState(false);
  const [audioBlob, setAudioBlob] = useState(null);
  const [responseData, setResponseData] = useState('')
  const [submitted, setSubmitted] = useState(false)
  const mediaRecorderRef = useRef(null);
  const audioChunksRef = useRef([]);

  const startRecording = async () => {
    setSubmitted(false)
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
    setSubmitted(true)
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
      console.log(response.data);
      setResponseData(response.data.result[0])
    } catch (error) {
      console.error('Error uploading audio file:', error);
    }
  };

  return (
    <div className = "flex flex-col items-center justify-center space-y-10">
      <button className = "btn btn-outline btn-error" onClick={recording ? stopRecording : startRecording}>
        {recording ? 'Stop Recording' : 'Start Recording'}
      </button>
      <form className = "btn btn-outline btn-secondary" onSubmit={handleSubmit}>
        <div className="tooltip" data-tip="if nothing happens, click again!">
          <button type="submit">Submit</button>
        </div>
      </form>
      <div>
        <div>
          {/* make this text box be the message that was said */}
          <div className="chat chat-start">
            <div className="chat-bubble chat-bubble-info">Send a recording! Please wait a bit during submissions.</div>
          </div>
        </div>
        {!recording && submitted && (
          <div className="chat chat-end">
            <div className="chat-bubble chat-bubble-accent">{responseData === 0 ? 'Male Voice Detected' : 'Female Voice Detected'}</div>
          </div>
        )}


      </div>
    </div>
  );
}
