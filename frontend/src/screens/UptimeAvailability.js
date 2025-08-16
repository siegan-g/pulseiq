import React from "react";
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
import { availabilityData } from '../data/availabilityData';

const UptimeAvailability = () => {
    return <div><BlurText
          text={`Uptime Availability`}
          delay={150}
          animateBy="words"
          direction="top"
          className="mb-8"
          style={styles.heading}
        />
        <div style={{ width: '100%', height: 400, marginTop: '2rem' }}>
      <h3 style={{ color: '#fff', textAlign: 'center' }}>Uptime Availability (%)</h3>
      <ResponsiveContainer>
        <LineChart data={availabilityData} margin={{ top: 20, right: 30, left: 20, bottom: 5 }}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="time" />
          <YAxis domain={[98, 100]} unit="%" />
          <Tooltip />
          <Legend />
          <Line type="monotone" dataKey="actual" stroke="#00BFFF" strokeWidth={2} dot={false} name="Actual Uptime" />
          <Line type="monotone" dataKey="predicted" stroke="#FF69B4" strokeWidth={2} strokeDasharray="5 5" dot={false} name="ML Prediction" />
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

export default UptimeAvailability;