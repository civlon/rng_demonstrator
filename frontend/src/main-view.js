import React, { useState } from "react";
import { Row, Col } from "react-bootstrap";
import "./main.css";
import GetTestDataButton from "./components/buttons/get-test-data-button.js";
import ChangeRngModeButton from "./components/buttons/change-rng-mode-button";
import ChangeViewButton from "./components/buttons/change-view-button";
import BeginnerView from "./beginner-view";
import AdvancedView from "./advanced-view";

const prngMode = {
  changing: "changing",
  static: "static",
};

const demonstratorView = {
  beginner: "Anfänger",
  advanced: "Fortgeschritten",
};

function MainView() {
  const [data, setData] = useState(0);
  const [mode, setMode] = useState(prngMode.static);
  const [requestTime, setRequestTime] = useState(0);
  const [currentView, setCurrentView] = useState(demonstratorView.beginner);
  const [isLoading, setIsLoading] = useState(false);

  const switchView = () => {
    if (currentView === demonstratorView.beginner) {
      setCurrentView(demonstratorView.advanced);
      return;
    }
    setData(0);
    setCurrentView(demonstratorView.beginner);
  };

  const toggleMode = () => {
    setMode((mode) =>
      mode === prngMode.static ? prngMode.changing : prngMode.static
    );
  };

  const toggleIsLoading = () => {
    setIsLoading(!isLoading);
  };

  const showMode = () => {
    if (mode === prngMode.static) {
      return <span style={{ color: "red" }}>schlechte</span>;
    }
    return <span style={{ color: "green" }}>gute</span>;
  };

  return (
    <div class="main-view">
      <h1>Demonstrator für Zufallszahlengeneratoren</h1>
      {currentView === demonstratorView.beginner ? (
        <p class="intro-text">
          Willkommen zum Demonstrator für Zufallszahlengenerierung. <br />
          Heutzutage benutzt jeder täglich das Internet und somit spielt
          Internetsicherheit eine immer wichtigere Rolle.
          Zufallszahlengeneratoren sind ein fundamentaler Bestandteil der
          Kryptographie, also der Verschlüsselung von Daten. Somit bedeuten
          schlechte Zufallszahlengeneratoren ein großes Risiko für unsere
          Sicherheit im Internet. <br />
          Kannst du den Unterschied zwischen einen guten und einen schlechten
          Zufallszahlengenerator erkennen?
        </p>
      ) : (
        <div></div>
      )}
      {/* show wanted view */}
      {currentView === demonstratorView.advanced ? (
        <div class="advanced-view">
          <AdvancedView
            data={data}
            isLoading={isLoading}
            requestTime={requestTime}
            mode={mode}
            switchView={switchView}
          />
        </div>
      ) : (
        <div className="beginnerView">
          <BeginnerView mode={mode} />
        </div>
      )}
      <Row>
        <Col>
          {currentView === demonstratorView.beginner ? (
            <div>
              <ChangeRngModeButton toggleMode={toggleMode}>
                Wechsel den Zufallszahlengenerator
              </ChangeRngModeButton>
              <p>Gerade ist der {showMode()} Zufallszahlengenerator aktiv</p>
            </div>
          ) : (
            <div>
              <GetTestDataButton
                setData={setData}
                setRequestTime={setRequestTime}
                toggleIsLoading={toggleIsLoading}
                data={data}
              >
                Starte Tests
              </GetTestDataButton>
              {data === 0 ? (
                <p>
                  Schau dir genauere Daten zu den Zufallszahlengeneratoren an
                </p>
              ) : (
                <p>Führe die Tests bei Bedarf erneut aus</p>
              )}
            </div>
          )}
        </Col>
        <Col>
          <ChangeViewButton switchView={switchView}>
            {currentView === demonstratorView.beginner
              ? "Erweiterte Ansicht"
              : "Einfache Ansicht"}
          </ChangeViewButton>
          {currentView === demonstratorView.beginner ? (
            <p>Schau dir an, wie ein Generator getestet wird</p>
          ) : (
            <p>Geh zurück zum Würfelspiel</p>
          )}
        </Col>
      </Row>
    </div>
  );
}
export default MainView;
