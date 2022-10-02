import React, { useState } from "react";
import { Row, Col, Modal } from "react-bootstrap";
import { Button, Spinner } from "react-bootstrap";
import TestComponent from "./components/tests/test-component";
import TestOverview from "./components/tests/test-overview";
import { useIdleTimer } from "react-idle-timer";

function AdvancedView({ isLoading, data, switchView }) {
  const [showModal, setShowModal] = useState(false);
  const [timeoutTime, setTimeoutTime] = useState(1000 * 60 * 2);

  const handleOnIdle = async () => {
    if (showModal) {
      setShowModal(false);
      setTimeoutTime(1000 * 60);
      switchView();
      return;
    }
    setShowModal(true);
    setTimeoutTime(1000 * 15);
  };

  const handleModalClose = () => {
    setShowModal(false);
    reset();
  };

  const { reset } = useIdleTimer({
    timeout: timeoutTime,
    onIdle: handleOnIdle,
  });

  return (
    <div>
      {isLoading && data === 0 ? (
        <div class="loading-tests">
          <p>
            Die Tests werden ausgeführt, bitte haben Sie einen Moment Geduld...
          </p>
          <Spinner animation="border" variant="primary" />
        </div>
      ) : data === 0 ? (
        <div>
          <p class="test-intro-text">
            Um zu testen, wie gut ein Zufallszahlengenerator ist, werden
            statistische Tests durchgeführt. Diese Tests sammeln empirische
            Daten, um die Null Hypothese: <br />
            "Die vom Generator G erzeugten Zahlen sind im gegebenen Interval
            (0,1] identisch gleichverteilt und unabhängig voneinander." <br />
            zu wiederlegen, oder anzunehmen. Das Ergebnis eines solchen Tests
            ist ein p-Wert(oder auch Signifikanzwert), welcher dafür steht, wie
            wahrscheinlich die Nullhypothese angenommen werden kann. Also je
            höher der p-Wert, desto höher ist die Wahrscheinlichkeit, dass der
            getestete Zufallszahlengenerator gut ist. <br />
            Für diesen Demonstrator wird für das Auführen der Tests die Testuite
            Dieharder verwendet.
            <br />
            In dieser Ansicht kannst du die Zufallszahlengeneratoren mit
            verschiedenen statistischen Tests testen. Drücke auf "Starte Tests"
            um die beiden Generatoren mit einander zu vergleichen und genauer zu
            erkennen, warum der schlechte Zufallszahlengenerator ungeeignet ist.
          </p>
        </div>
      ) : (
        <div>
          <Row>
            <Col>
              {data.map((testData, index) => {
                return (
                  <div class="test-component">
                    <TestComponent testData={testData} testNumber={index + 1} />
                  </div>
                );
              })}
              <p class="test-explanation">
                Ein Test ist besteht, wenn der resultierende p-Wert größer a =
                0,000001 und kleiner 1-a ist. <br />
                Ist der p-Wert kleiner a = 0,005 und größer 1-a wurde der Test
                nur knapp bestanden. <br />
                Prinzipiell gilt: je höher der p-Wert desto besser (bis zur
                vorher genannten Grenze)
              </p>
            </Col>
            <Col>
              <div class="test-overview">
                <TestOverview data={data} />
              </div>
            </Col>
          </Row>
        </div>
      )}
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
export default AdvancedView;
