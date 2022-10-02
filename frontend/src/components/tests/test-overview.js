import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
  Label,
} from "recharts";

function TestOverview(data) {
  const testData = data.data;

  const getBarData = () => {
    let bardata = [];
    for (let i = 0; i < testData.length; i++) {
      bardata.push({
        name: i + 1,
        changing: testData[i].dieharderTestChangingMode.p_value,
        static: testData[i].dieharderTestStaticMode.p_value,
      });
    }
    return bardata;
  };

  return (
    <BarChart
      width={390}
      height={310}
      data={getBarData()}
      margin={{
        top: 18,
        bottom: 10,
      }}
    >
      <CartesianGrid strokeDasharray="3 3" />
      <XAxis dataKey="name" />
      <YAxis domain={[0, 1]}>
        <Label
          value="p-Wert"
          position="top"
          style={{
            fontSize: "90%",
            fill: "rgba(130, 130, 130, 1)",
            paddingBottom: "2%",
            paddingLeft: "1%",
          }}
        />
      </YAxis>
      <Tooltip />
      <Legend />
      <Bar dataKey="changing" fill="green" name="Guter Generator" />
      <Bar dataKey="static" fill="red" name="Schlechter Generator" />
    </BarChart>
  );
}
export default TestOverview;
