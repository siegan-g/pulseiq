// src/data/throughputData.js

const throughputData = [
  { time: '12:00', actual: 120, predicted: 120 },
  { time: '12:01', actual: 130, predicted: 130 },
  { time: '12:02', actual: 140, predicted: 140 },
  { time: '12:03', actual: 150, predicted: 150 },
  { time: '12:04', actual: 155, predicted: 160 },
  { time: '12:05', actual: 160, predicted: 180 },
  { time: '12:06', actual: 165, predicted: 210 },
  { time: '12:07', actual: 170, predicted: 240 }, // Forecast spike
  { time: '12:08', actual: 175, predicted: 280 },
  { time: '12:09', actual: 180, predicted: 300 },
  { time: '12:10', actual: 220, predicted: 320 }, // Spike begins
  { time: '12:11', actual: 260, predicted: 330 },
  { time: '12:12', actual: 300, predicted: 340 },
  { time: '12:13', actual: 340, predicted: 345 },
  { time: '12:14', actual: 370, predicted: 350 },
  { time: '12:15', actual: 400, predicted: 340 }, // Plateau
];

export default throughputData;
