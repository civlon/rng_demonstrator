import React from "react";

import { Modal } from "react-bootstrap";

function DiceGuessingGameModal({ showModal, closeModal, title, text }) {
  return (
    <Modal show={showModal} onHide={() => closeModal()}>
      <Modal.Header closeButton={() => closeModal()}>
        <Modal.Title>{title}</Modal.Title>
      </Modal.Header>
      <Modal.Body>{text}</Modal.Body>
    </Modal>
  );
}

export default DiceGuessingGameModal;
