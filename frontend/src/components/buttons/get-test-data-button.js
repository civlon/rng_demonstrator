import { Button, Spinner } from "react-bootstrap";
import React, { useEffect, useState } from "react";

function GetTestDataButton({
  children,
  setData,
  setRequestTime,
  toggleIsLoading,
  isLoading,
  data,
}) {
  const ALL_TEST_NUMBERS = [3, 208, 101, 0, 8, 7, 15, 100, 206, 4];
  const [buttonSpinning, setButtonSpinning] = useState(false);

  const getData = async () => {
    setButtonSpinning(true);
    setData(0);
    toggleIsLoading();
    await fetchTests();
  };

  const fetchTests = async () => {
    var testData = [];
    ALL_TEST_NUMBERS.forEach(async (testNumber) => {
      const request = await fetch("/run?" + testNumber);
      const result = await request.json();
      testData = [...testData, result];
      setData(testData);
    });
  };

  useEffect(() => {
    if (data.length === 10) {
      setButtonSpinning(false);
      toggleIsLoading();
    }
  }, [data, toggleIsLoading]);

  return (
    <div className="changeRngModeButton">
      {buttonSpinning ? (
        <Spinner animation="border" variant="primary"></Spinner>
      ) : (
        <Button onClick={async () => await getData()} className="button">
          {children}
        </Button>
      )}
    </div>
  );
}
export default GetTestDataButton;
