import { Col } from "react-bootstrap";
import { Spinner } from "react-bootstrap";
import React from "react";
import "./../../main.css";

function TestComponent({ testData, testNumber }) {
  const data = testData;

  const getTestDiscription = (testName) => {
    switch (testName) {
      case "diehard_dna":
        return "Der DNA Test besteht aus einem Alphabet mit vier Buchstaben: C,G,A,T, die anhand von 2 zugewiesenen Bits der Eingabe gesetzt werden. Es werden Wörter der Länge 10 betrachtet. Somit entstehen 2**20 mögliche Wörter. Bei einer 2**21 langen Zeichenkette sollte der Mittelwert der fehlenden Wörter bei 141909 liegen.";
      case "diehard_count_1s_str":
        return "Im count-the-1's on a stream of bytes Test wird die Eingabe als Bitstream betrachtet, wobei jede 32-Bit Ganzzahl in 4 Bytes gespaltet wird. Jedes Byte kann Null bis Acht mal das Bit 1 enthalten. Nun werden die Bytestreams überlappend in Wörter der Länge Fünf aufgeteilt. Jeder Buchstabe wird einem Wert A, B, C, D oder E zugeteilt. Dieser Wert ergibt sich aus der Anzahl an Einsen in dem jeweiligen Byte. Null, Eins oder Zwei werfen A, Drei werfen B, 4 werfen C, 5 werfen D und Sechs, Sieben und Acht werfen E. Bei 5**5 möglichen Wörtern über einen String von 256000 Wörtern, werden die Anzahl aller vorkommenden Wörter gezählt. Mit den Ergebnissen kann ein Chi-Quadrat-Test durchgeführt werden, um einen p-Wert zu ermitteln.";
      case "diehard_birthdays":
        return "Im birthday spacing Test werden m Geburtstage in einem Jahr von n Tagen festgelegt. Die Werte für die Distanzen zwischen Geburtstagen werden in eine Liste aufgenommen. Nun wird geschaut, wie oft diese Werte mehr als einmal vorkommen. Diese Variable wird j genannt. Bei gutem Zufall sollte j nun asymptotisch Poissen-verteilt sein. Mit den Werten n = 2**24 und m = 2**9 werden 500 Proben von j ermittelt. Damit wird ein Chi-Quadrat-Verteilungstest durchgeführt um einen p-Wert zu erhalten.";
      case "sts_monobit":
        return "Im sts monobit Test wurde aus der STS Testsuite übernommen und in Dieharder neu implementiert. Ziel ist es zu überprüfen, ob die Anzahl an Nullen und Einsen ungefähr gleich ist, wie es bei gutem Zufall der Fall wäre.";
      case "diehard_runs":
        return "Im runs Test wird eine lange Sequenz an zufälligen Gleitkommazahlen generiert. Diese sind im Interval [0,1). Beim Betrachten dieser Sequenz werden die Anzahl der Aufstiege (up-runs) und die Anzal der Abstiege (down-runs) gezählt. Zum Beispiel bei der Sequenz: 0.243, 0.124, 0.119, 0.597, 0.932 kommt ein up-run der Länge 2 und ein down-run der Länge 3 vor(ohne den nächsten Wert in betracht zuziehen). Mit diesen Ergebnissen kann ein Chi-Quadrat-Test durchgeführt werden.";
      case "dab_dct":
        return "Im dab dct Test wird eine Diskrete Kosinustransformation auf die Ausgabe des Zufallszahlengenerators ausgeführt. Es werden die Positionen der maximalen Werte jeder Transformation gespeichert, um damit einen Chi-Quadrat-Test durchzuführen.";
      case "sts_runs":
        return "Im sts runs Test ist eine andere Version des runs Test. Er wurde von der STS Testsuite übernommen und arbeitet mit Bits, anstatt mit Ganz- beziehungsweise Gleitkommazahlen.";
      case "dab_filltree2":
        return "Der dab filltree2 Test erstellt mehrere kleine binäre Bäume. Nun wird für jedes Bit der Zufallszahlengeneratoreneingabe nach unten in den Baum gewandert. Bei einer Null wird nach rechts gegangen und bei einer Eins nach links. Trifft der Pfad auf einen unmakierten Knoten wird er markiert und der Pfad wird neugestartet. Bei einem bereits markierten Knoten wandert der Pfad weiter. Um einen p-Wert zu errechnen, werden die Ergebnisse mit den erwarteten Ergebnissen in einem Chi-Quadrat-Test verglichen.";
      case "diehard_bitstream":
        return "Im bitstream Test wird die Eingabe als Bitstream betrachtet. Mit {0,1} als Alphabet, wird der Bitstream in Wörter der Länge 20 überlappend aufgeteilt. Somit besteht das erste Wort aus b1b2...b20, das zweite Wort aus b2b3...b21 und so fortführend. Nun werden die fehlenden Wörter in einer 2**21 langen Zeichenkette gezählt. Bei einer 2**21 langen Zeichenkette sollte die Anzahl an fehlenden Wörtern, von den 2**20 möglichen Wörten, nahezu normal verteilt sein. Mit einem Mittelwert von 141.909 und einem sigma von 428, kann der p-Wert mit der Formel: p-Wert = (j - 141909) / 428 berechnet werden. Dabei ist j die Anzahl an fehlenden Wörtern.";
      case "diehard_rank_6x8":
        return "Im Rank 6x8 Test werden von 6 zufälligen 32-Bit Ganzzahlen jeweils ein Byte gewählt. Die ausgewählten 6 Bytes ergeben eine 6x8 binäre Matrix, von welcher der Rang bestimmt wird. Der Rang kann einen Wert von 0 bis 6 einnehmen, wobei 0,1,2,3 selten sind und deswegen mit Rang 4 vereinigt werden. Dies wird 100000 mal wiederholt, um einen Chi-Quadrat-Test auf die Anzahl an den Rängen 6,5 und der Vereinigung der Ränge 1,2,3,4 auszuführen";
      default:
        return "";
    }
  };

  const displayResult = (result, pValue) => {
    let testResult;
    switch (result) {
      case "PASSED":
        testResult = "Bestanden";
        break;
      case "FAILED":
        testResult = "Durchgefallen";
        break;
      case "WEAK":
        testResult = "Knapp";
        break;
      default:
        testResult = "";
        break;
    }
    return testResult + "(" + pValue + ")";
  };

  return (
    <div class="test-component-border">
      {testData === undefined ? (
        <Spinner animation="border" variant="primary" />
      ) : (
        <div>
          <details>
            <summary class="test-discription">
              <div class="test-component-row">
                <Col>
                  <p class="test-name">
                    {testNumber}. {data.testName}:
                  </p>
                </Col>
                <Col>
                  <p className="changingRngText">
                    {displayResult(
                      data.dieharderTestChangingMode.result,
                      data.dieharderTestChangingMode.p_value
                    )}
                  </p>
                </Col>
                <Col>
                  <p className="staticRngText">
                    {displayResult(
                      data.dieharderTestStaticMode.result,
                      data.dieharderTestStaticMode.p_value
                    )}
                  </p>
                </Col>
              </div>
              {/*           <details class="test-discription">
            <summary class="text-discription">Testbeschreibung</summary>
            <p>dieser test ist voll mega cool.</p>
          </details> */}
            </summary>
            <p class="test-discription-text">
              {getTestDiscription(data.testName)}
            </p>
          </details>
        </div>
      )}
    </div>
  );
}
export default TestComponent;
