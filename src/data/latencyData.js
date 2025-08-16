// latencyData.js
export const latencyData = [
  { time: '12:00', actual: 120, predicted: 120 },
  { time: '12:01', actual: 125, predicted: 125 },
  { time: '12:02', actual: 130, predicted: 130 },
  { time: '12:03', actual: 128, predicted: 132 },
  { time: '12:04', actual: 127, predicted: 135 },
  { time: '12:05', actual: 129, predicted: 145 },
  { time: '12:06', actual: 135, predicted: 160 },
  { time: '12:07', actual: 140, predicted: 185 },
  { time: '12:08', actual: 145, predicted: 210 }, // Predicted spike begins
  { time: '12:09', actual: 155, predicted: 230 },
  { time: '12:10', actual: 200, predicted: 250 }, // Spike realized
  { time: '12:11', actual: 240, predicted: 260 },
  { time: '12:12', actual: 260, predicted: 270 },
  { time: '12:13', actual: 275, predicted: 275 },
  { time: '12:14', actual: 280, predicted: 270 },
  { time: '12:15', actual: 285, predicted: 260 }, // Recovery
];
