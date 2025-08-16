import React from "react";
import "../styles/FadeInSection.css";

export default function FadeInSection(props) {
    const [isVisible, setVisible] = React.useState(false);
    const domRef = React.useRef();
    React.useEffect(() => {
        const observer = new IntersectionObserver(entries => {
            entries.forEach(entry => setVisible(entry.isIntersecting));
        });
        observer.observe(domRef.current);
        return () => observer.disconnect();
    }, []);
    return (
        <div
            className={`fade-in-section ${isVisible ? "visible" : ""}`}
            ref={domRef}
        >
            {props.children}
        </div>
    );
}