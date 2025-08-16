import React from 'react';
import BlurText from '../components/BlurText';
import '../styles/Transaction.css';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';
import throughputData from '../data/throughputData';

const TransactionsThroughput = () => {
    return <div><BlurText
          text={`Transactions Throughput`}
          delay={150}
          animateBy="words"
          direction="top"
          className="mb-8"
          style={styles.heading}
        />
<div style={{ width: '100%', height: 400 }}>
      <h3 style={{ color: '#fff', textAlign: 'center' }}>Transaction Throughput (Real-Time vs Prediction)</h3>
      <ResponsiveContainer>
        <LineChart data={throughputData} margin={{ top: 20, right: 30, left: 20, bottom: 5 }}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="time" />
          <YAxis />
          <Tooltip />
          <Legend />
          <Line type="monotone" dataKey="actual" stroke="#00c49f" strokeWidth={2} dot={false} name="Actual" />
          <Line type="monotone" dataKey="predicted" stroke="#ff7300" strokeWidth={2} strokeDasharray="5 5" dot={false} name="ML Prediction" />
        </LineChart>
      </ResponsiveContainer>
    </div>
        </div>
        
        ;
};

const styles ={
    heading: {
    color: '#38b954ff', 
    fontWeight: 'bold',
    lineHeight: '1',
    fontSize: '3rem',
  },
};

export default TransactionsThroughput;