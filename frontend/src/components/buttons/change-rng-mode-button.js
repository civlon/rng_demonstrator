import { Button } from "react-bootstrap";
import "./../../main.css";

function ChangeRngModeButton({ children, toggleMode, ...props }) {
  return (
    <div className="changeRngModeButton">
      <Button onClick={() => toggleMode()} className="button" {...props}>
        {children}
      </Button>
    </div>
  );
}
export default ChangeRngModeButton;
