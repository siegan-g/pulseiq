import React from 'react';
import BlurText from '../components/BlurText';
import '../styles/Transaction.css';
import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
  ResponsiveContainer,
} from 'recharts';
import { latencyData } from '../data/latencyData';


const Latency = () => {
    return <div>
        <BlurText
          text={`Latency`}
          delay={150}
          animateBy="words"
          direction="top"
          className="mb-8"
          style={styles.heading}
        />
        <div style={{ width: '100%', height: 400, marginTop: '2rem' }}>
      <h3 style={{ color: '#fff', textAlign: 'center' }}>Transaction Latency (ms)</h3>
      <ResponsiveContainer>
        <LineChart data={latencyData} margin={{ top: 20, right: 30, left: 20, bottom: 5 }}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="time" />
          <YAxis unit="ms" />
          <Tooltip />
          <Legend />
          <Line type="monotone" dataKey="actual" stroke="#8884d8" strokeWidth={2} dot={false} name="Actual Latency" />
          <Line type="monotone" dataKey="predicted" stroke="#ff0000" strokeWidth={2} strokeDasharray="5 5" dot={false} name="ML Prediction" />
        </LineChart>
      </ResponsiveContainer>
    </div>
        </div>;
};

const styles ={
    heading: {
    color: '#38b954ff', 
    fontWeight: 'bold',
    lineHeight: '1',
    fontSize: '3rem',
  },
};

export default Latency;