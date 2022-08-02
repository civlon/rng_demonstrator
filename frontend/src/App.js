import React, { useState, useCallback } from 'react'
import { Button, Spinner } from 'react-bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css';
import './App.css'

const prngMode = {
  changing: 'changing',
  static: 'static',
};

function App() {
  const [data, setData] = useState({})
  const [mode, setMode] = useState(prngMode.static)

  const getTestData = (data) => {
    setData(data)
  }

  const toggleMode = () => {
    setMode((mode) => (mode === prngMode.static ? prngMode.changing
      : prngMode.static))
  }

  return (
    <div class="homepage">
      <p>testing results: {JSON.stringify(data)}</p>
      <GetTestDataButton getTestData={getTestData} mode={mode}>Get Test Data</GetTestDataButton>
      &nbsp;&nbsp;&nbsp;
      <ChangePrngModeButton toggleMode={toggleMode} >Change Mode</ChangePrngModeButton>
      <p>current mode: {mode}</p>
    </div>
  )

}

export default App

function GetTestDataButton({ children, getTestData, mode, ...props }) {
  const [isButtonLoading, setIsButtonLoading] = useState(false);

  const handleOnClick = async () => {
    setIsButtonLoading(true);
    await fetch("/get?" + mode).then(res => res.json()).then(data => { getTestData(data) }, [])
    setIsButtonLoading(false);
  }

  return (
    <Button onClick={async () => await handleOnClick()} className="button" {...props}>
      {isButtonLoading ? <Spinner animation="border" variant="primary" /> : children}
    </Button>
  );
}

function ChangePrngModeButton({ children, toggleMode, ...props }) {

  return (
    <Button onClick={() => toggleMode()} className="button" {...props}>
      {children}
    </Button>
  );
}