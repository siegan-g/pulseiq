import './App.css';
import React, { useState } from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Sidebar from './components/SideNavbar';
import LandingPage from './screens/LandingPage';
import TransactionsThroughput from './screens/TransactionsThroughput';
import Latency from './screens/Latency';
import UptimeAvailability from './screens/UptimeAvailability';
import AboutUs from './screens/AboutUs';
import ContactUs from './screens/ContactUs';

function App() {
  const [collapsed, setCollapsed] = useState(false);

  return (
    <Router>
      <div className="app-container">
        <Sidebar collapsed={collapsed} setCollapsed={setCollapsed} />
        <div className="main-content" style={{ marginLeft: collapsed ? 80 : 200 }}>
          <Routes>
            <Route path="/" element={<LandingPage />} />
            <Route path="/transactions-throughput" element={<TransactionsThroughput />} />
            <Route path="/latency" element={<Latency />} />
            <Route path="/uptime-availability" element={<UptimeAvailability />} />
            <Route path="/about" element={<AboutUs />} />
            <Route path="/contact" element={<ContactUs />} />
          </Routes>
        </div>
      </div>
    </Router>
  );
}

export default App;
