'use client';
import React from 'react';
import Form from './components/Form';

function App() {
  const reloadPage = () => {
    window.location.reload();
  };
  return (
    <>
    <div className="navbar bg-base-100 justify-between">
      <a className="btn btn-ghost text-xl" onClick={reloadPage}>Voice-Gen</a>
      <a className="btn btn-ghost text-l" href = "https://github.com/raincoat4/voicegen">Click here to view the source code!</a>
    </div>
    <div className = "absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2">
      <Form/>
    </div>
    </>
  );
}

export default App;
