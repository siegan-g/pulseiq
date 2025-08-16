import React from 'react';
import BlurText from '../components/BlurText';
import '../styles/Transaction.css';

const AboutUs = () => {
  return (
    <div className="about-us-container" style={{ padding: '2rem', maxWidth: '900px', margin: '0 auto' }}>
      <BlurText
          text={`Latency`}
          delay={150}
          animateBy="words"
          direction="top"
          className="mb-8"
          style={styles.heading}
        />

      <p style={{ fontSize: '1.1rem', lineHeight: '1.6', color: 'white' }}>
  <strong>PulseIQ</strong> is a real-time predictive analytics platform designed to empower operations teams
  with foresight into their payment systems. In high-volume environments, milliseconds can be the difference
  between seamless service and critical failure — that's where PulseIQ steps in.
</p>

<h2 style={{ fontSize: '1.8rem', marginTop: '2rem', color: 'white' }}>Our Scope</h2>

<ul style={{ fontSize: '1.1rem', lineHeight: '1.8', paddingLeft: '1.2rem', color: 'white' }}>
  <li>
    ✅ <strong>Real-Time Ingestion:</strong> Our backend service ingests mock or live transaction streams using WebSockets,
    enabling instant access to system performance data.
  </li>
  <li>
    📊 <strong>Live Dashboard:</strong> A sleek, React-powered dashboard powered by Recharts provides live visualizations of
    key metrics like transaction volume, latency, and error rates.
  </li>
  <li>
    🤖 <strong>Predictive Machine Learning:</strong> Our ML engine forecasts anomalies and performance spikes 5–10 minutes in advance,
    giving ops teams valuable time to respond proactively.
  </li>
  <li>
    ⚙️ <strong>Scalable & Resilient Architecture:</strong> The system is built with performance and fault tolerance in mind — leveraging
    async processing, auto-scaling strategies, and monitoring integrations.
  </li>
  <li>
    🚨 <strong>Operational Value:</strong> PulseIQ transforms reactive monitoring into proactive incident prevention, reducing system
    downtime and improving reliability at scale.
  </li>
</ul>

<p style={{ fontSize: '1.1rem', marginTop: '2rem', color: 'white' }}>
  Whether it's predicting failures, visualizing live trends, or enabling smart operations — PulseIQ is built
  to keep your payment systems resilient and ready for the future.
</p>

    </div>
  );
};

const styles ={
    heading: {
    color: '#38b954ff', 
    fontWeight: 'bold',
    lineHeight: '1',
    fontSize: '3rem',
  },
};

export default AboutUs;
