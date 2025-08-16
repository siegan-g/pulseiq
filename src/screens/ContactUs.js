import React from 'react';
import BlurText from '../components/BlurText';
import '../styles/Transaction.css';

const ContactUs = () => {
    return (
        <div>
            <BlurText
                text={`Contact Us`}
                delay={150}
                animateBy="words"
                direction="top"
                className="mb-8"
                style={styles.heading}
            />
        </div>
    );
};

const styles = {
    heading: {
        color: '#38b954ff',
        fontWeight: 'bold',
        lineHeight: '1',
        fontSize: '3rem',
    },
};

export default ContactUs;