import React, { useEffect } from "react";
import Dice from "react-dice-roll";

function DiceComponent({ diceRef, getDiceRoll, mode, dice, isRolling }) {
  const roll = async () => {
    if (isRolling) {
      await getRoll();
    }
  };

  const getRoll = async () => {
    let res = await fetch("/roll?" + mode);
    let diceRoll = await res.json();
    await getDiceRoll(diceRoll);
  };

  useEffect(() => {
    if (diceRef && diceRef.current && diceRef.current.children[0]) {
      diceRef.current.style.pointerEvents = "auto";
      diceRef.current.children[0].click();
      diceRef.current.style.pointerEvents = "none";
    }
    const interval = setInterval(() => {
      roll();
    }, 3000);
    return () => clearInterval(interval);
  }, [getDiceRoll, dice, diceRef, isRolling]);

  return (
    <div ref={diceRef} style={{ pointerEvents: "none" }}>
      <Dice
        size={190}
        cheatValue={dice}
        key={"dice"}
        faceBg={mode === "changing" ? "green" : "red"}
      />
    </div>
  );
}
export default DiceComponent;
