import { Button } from "react-bootstrap";
import "./../../main.css";

function ChangeViewButton({ children, switchView }) {
  return (
    <div className="changeViewButton">
      <Button onClick={switchView} className="button">
        {children}
      </Button>
    </div>
  );
}
export default ChangeViewButton;
