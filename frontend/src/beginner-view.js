import React, { useState, useRef } from "react";
import "bootstrap/dist/css/bootstrap.min.css";
import DiceComponent from "./components/dice/dice-component";
import DiceHistory from "./components/dice/dice-hostory";
import RollDiceGuessingGame from "./components/dice/dice-guessing-game/roll-dice-guessing-game";
import { useIdleTimer } from "react-idle-timer";
import { Col, Container, Modal, Button } from "react-bootstrap";
import "./main.css";

function BeginnerView({ mode }) {
  const [dice, setDice] = useState(0);
  const [staticDiceHistory, setStaticDiceHistory] = useState([]);
  const [changingDiceHistory, setChangingDiceHistory] = useState([]);
  const [isRolling, setIsRolling] = useState(true);

  const [showModal, setShowModal] = useState(false);
  const [timeoutTime, setTimeoutTime] = useState(1000 * 45);

  const diceRef = useRef(0);

  const updateIsRolling = (rollingUpdate) => {
    setIsRolling(rollingUpdate);
  };

  const timeout = (delay) => {
    return new Promise((res) => setTimeout(res, delay));
  };

  const updateDiceHistory = async (diceRoll, diceHistory, setDiceHistory) => {
    if (diceHistory.length >= 18) {
      let arr = [...diceHistory];
      arr.splice(0, 6);
      arr.push(diceRoll);
      setDiceHistory(arr);
      return;
    }
    let arr = [...diceHistory];
    arr.push(diceRoll);
    setDiceHistory(arr);
  };

  const getDiceRoll = async (diceRoll) => {
    setDice(diceRoll);
    await timeout(1000);
    if (mode === "changing") {
      return updateDiceHistory(
        diceRoll,
        changingDiceHistory,
        setChangingDiceHistory
      );
    }
    updateDiceHistory(diceRoll, staticDiceHistory, setStaticDiceHistory);
  };

  const handleModalClose = () => {
    setShowModal(false);
    reset();
  };

  const handleOnIdle = async () => {
    if (showModal) {
      setTimeoutTime(1000 * 45);
      setShowModal(false);
      setIsRolling(true);
      return;
    }
    if (!isRolling) {
      setTimeoutTime(1000 * 15);
      setShowModal(true);
    }
  };

  const { reset } = useIdleTimer({
    timeout: timeoutTime,
    onIdle: handleOnIdle,
  });

  return (
    <div>
      <Container>
        <div class="dice-row">
          <Col>
            <RollDiceGuessingGame
              isRolling={isRolling}
              updateIsRolling={updateIsRolling}
              getDiceRoll={getDiceRoll}
              mode={mode}
            />
          </Col>
          <Col
            className="dice"
            style={{ disply: "flex", justifyContent: "left" }}
          >
            <DiceComponent
              diceRef={diceRef}
              isRolling={isRolling}
              getDiceRoll={getDiceRoll}
              mode={mode}
              dice={dice}
              key={"dice"}
            />
          </Col>
          <Col style={{ disply: "flex", justifyContent: "left" }}>
            {mode === "changing" ? (
              <DiceHistory diceHistory={changingDiceHistory} mode={mode} />
            ) : (
              <DiceHistory diceHistory={staticDiceHistory} mode={mode} />
            )}
          </Col>
        </div>
        {/*       <div>current dice roll: {dice}</div>
      <div>{diceHistory}</div>
      <div>{diceHistory.slice(0).reverse()}</div> */}
      </Container>
      <Modal show={showModal} onHide={handleModalClose}>
        <Modal.Header closeButton={handleModalClose}>
          <Modal.Title>Hallo?...</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          Ist noch jemand da? Sonst wird die Seite neugeladen.
        </Modal.Body>
        <Modal.Footer>
          <Button variant="primary" onClick={handleModalClose}>
            Ja, Ich bin noch da
          </Button>
        </Modal.Footer>
      </Modal>
    </div>
  );
}
export default BeginnerView;
