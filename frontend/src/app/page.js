'use client';
import React from 'react';
import Form from './components/Form';

function App() {

  return (
    <>
    <div className="navbar bg-base-100">
      <a className="btn btn-ghost text-xl">Voice Recognition</a>
    </div>
    <div className = "absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2">
      <Form/>
    </div>
    </>
  );
}

export default App;
