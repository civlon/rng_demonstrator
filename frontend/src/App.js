import React, { useState } from 'react'
import { Button, Spinner } from 'react-bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css';
import './App.css'

function App() {
  const [data, setData] = useState({})

  const getTestData = (data) => {
    setData(data)
  }

  return (
    <div class="homepage">
      <p>Results of testing: {JSON.stringify(data)}</p>
      <GetTestDataButton getTestData={getTestData}>Get Test Data</GetTestDataButton>
    </div>
  )

}

export default App

function GetTestDataButton({ children, getTestData, ...props }) {
  const [isButtonLoading, setIsButtonLoading] = useState(false);

  const handleOnClick = async () => {
    setIsButtonLoading(true);
    await fetch("/getTestData").then(res => res.json()).then(data => { getTestData(data) }, [])
    setIsButtonLoading(false);
  }

  return (
    <Button onClick={async () => await handleOnClick()} className="button" {...props}>
      {isButtonLoading ? <Spinner animation="border" variant="primary" /> : children}
    </Button>
  );
}