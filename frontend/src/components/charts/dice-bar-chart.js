import { BarChart, Bar, Cell, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';

function DiceBarChart(staticDiceRolls, changingDiceRolls){
    const bardata = [
        {
          name: '1',
          static: staticDiceRolls[0],
          changing: changingDiceRolls[0],
        },
        {
          name: '2',
          static: staticDiceRolls[1],
          changing: changingDiceRolls[1],
        },
        {
          name: '3',
          static: staticDiceRolls[2],
          changing: changingDiceRolls[2],
        },
        {
          name: '4',
          static: staticDiceRolls[3],
          changing: changingDiceRolls[3],
        },
        {
          name: '5',
          static: staticDiceRolls[4],
          changing: changingDiceRolls[4],
        },
        {
          name: '6',
          static: staticDiceRolls[5],
          changing: changingDiceRolls[5],
        },
      ];

    return (<BarChart
    width={800}
    height={500}
    data={bardata}
    margin={{
      top: 10,
      right: 100,
      left: 100,
      bottom: 10,
    }}
  >
    <CartesianGrid strokeDasharray="3 3" />
    <XAxis dataKey="name" />
    <YAxis />
    <Tooltip />
    <Legend />
    <Bar dataKey="static" fill="#8884d8" />
    <Bar dataKey="changing" fill="#82ca9d" />
  </BarChart>);
}export default DiceBarChart