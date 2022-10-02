import { Button, Form, Container } from "react-bootstrap";
import React, { useState } from "react";
import DiceGuessingGameModal from "./dice-guessing-game-modal";

function RollDiceGuessingGame({
  isRolling,
  updateIsRolling,
  getDiceRoll,
  mode,
}) {
  const [guess, setGuess] = useState(0);
  const [showModal, setShow] = useState(false);
  const [modalTitle, setModalTitle] = useState("");
  const [modalText, setModalText] = useState("");

  const closeModal = () => {
    setShow(false);
  };

  const openModal = (title, text) => {
    setModalTitle(title);
    setModalText(text);
    setShow(true);
  };

  const onInput = (e) => {
    setGuess(e.target.value);
  };

  const onRoll = async (e) => {
    e.preventDefault();
    let res = await fetch("/roll?" + mode);
    let diceRoll = await res.json();
    await getDiceRoll(diceRoll);
    if (diceRoll === guess) {
      openModal("Glückwunsch!", "Du hast den Wurf korrekt geraten.");
      return;
    }
    openModal(
      "Leider Falsch...",
      `Das war nicht korrekt. Du hast ${guess} getippt, doch das Ergebnis war ${diceRoll}. Probiere es doch nochmal.`
    );
  };

  return (
    <div className="guessingGame">
      <Container>
        {isRolling ? (
          <div />
        ) : (
          <Form className="mb-3" controlId="guessNextRoll" onSubmit={onRoll}>
            <Form.Label>Was kommt als nächstes?:</Form.Label>
            <Form.Control
              type="guessDice"
              placeholder="Nächster Wurf"
              onChange={onInput}
            />
            <Form.Text className="text-muted">
              Tippe eine Zahl von 1-6
            </Form.Text>
            <Button type="submit">Werfe den Würfel</Button>
          </Form>
        )}
      </Container>
      <Container>
        <Button onClick={() => updateIsRolling(!isRolling)}>
          {isRolling ? "Rate den nächsten Wurf" : "Raten beenden"}
        </Button>
      </Container>
      <DiceGuessingGameModal
        showModal={showModal}
        closeModal={closeModal}
        title={modalTitle}
        text={modalText}
      ></DiceGuessingGameModal>
    </div>
  );
}
export default RollDiceGuessingGame;
