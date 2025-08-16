import React from 'react';
import BlurText from '../components/BlurText';
import Silk from '../components/SilkBackground';

const LandingPage = () => {
  return (
    <div style={styles.container}>
      <div style={styles.silkWrapper}>
        <Silk
          speed={5}
          scale={1}
          color="#439049"
          noiseIntensity={1.5}
          rotation={0}
        />
      </div>

      <div style={styles.content}>
        <BlurText
          text={`Empower Your Financial Journey with PulseIQ`}
          delay={150}
          animateBy="words"
          direction="top"
          className="mb-8"
          style={styles.heading}
        />
        <BlurText
          text={`From reactive firefighting to proactive decision-making`}
          delay={150}
          animateBy="words"
          direction="top"
          className="mb-8"
          style={styles.tagline}
        />
      </div>
    </div>
  );
};

const styles = {
  container: {
    height: '100vh',
    width: '100%',
    position: 'relative', 
    overflow: 'hidden',
  },
  silkWrapper: {
    position: 'fixed', 
    top: 0,
    left: 0,
    width: '100%',
    height: '100%',
    zIndex: -1,
  },
  content: {
    marginTop: '4rem',
    paddingLeft: '2rem',
    position: 'relative', 
    zIndex: 1,
  },
  heading: {
    color: '#abbc56ff', 
    fontWeight: 'bold',
    lineHeight: '1',
    fontSize: '3rem',
  },
  tagline: {
    marginTop: '2rem',
    color: '#95a318ff',
  },
};

export default LandingPage;
