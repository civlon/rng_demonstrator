function DiceHistory({ diceHistory, mode }) {
  const getBorderColor = () => {
    if (mode === "changing") {
      return "green";
    }
    return "red";
  };

  return (
    <div style={{ width: 100 }}>
      <div
        style={{
          width: "310px",
          height: "25px",
          borderTop: `2px solid ${getBorderColor()}`,
          borderLeft: `2px solid ${getBorderColor()}`,
          borderRight: `2px solid ${getBorderColor()}`,
        }}
      >
        <h6>Würfelergebnisse:</h6>
      </div>
      <div
        style={{
          display: "flex",
          flexDirection: "horizontal",
          width: "310px",
          height: "125px",
          fontSize: "18px",
          borderTop: `2px solid ${getBorderColor()}`,
          borderBottom: `2px solid ${getBorderColor()}`,
          borderLeft: `2px solid ${getBorderColor()}`,
          borderRight: `2px solid ${getBorderColor()}`,
          flexWrap: "wrap",
        }}
      >
        {diceHistory.slice(0).map((diceRoll, index) => {
          if (index === diceHistory.length - 1) {
            return (
              <div
                style={{
                  width: "40px",
                  height: "30px",
                  background: "#0d6efd",
                  borderRadius: "5px",
                  margin: "5px",
                  textAlign: "center",
                }}
              >
                {diceRoll}
              </div>
            );
          }
          return (
            <div
              style={{
                width: "40px",
                height: "30px",
                background: "#1E90FF",
                borderRadius: "5px",
                margin: "5px",
                textAlign: "center",
              }}
            >
              {diceRoll}
            </div>
          );
        })}
      </div>
    </div>
  );
}
export default DiceHistory;
/* 

display: "flex",
flexDirection: "horizontal",
width: "360px",
height: "160px",
fontSize: "20px",
margin: "20px",
borderTop: `2px solid ${getBorderColor()}`,
borderBottom: `2px solid ${getBorderColor()}`,
borderLeft: `2px solid ${getBorderColor()}`,
borderRight: `2px solid ${getBorderColor()}`,
flexWrap: "wrap", */

/* width: "40px",
height: "30px",
background: "#0d6efd",
borderRadius: "5px",
margin: "10px",
textAlign: "center", */
