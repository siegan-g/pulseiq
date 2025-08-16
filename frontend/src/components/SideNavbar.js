import React, { useState } from 'react';
import '../styles/SideNavbar.css';
import { FaAnglesRight, FaAnglesLeft } from "react-icons/fa6";
import { FaChevronDown, FaChevronUp } from "react-icons/fa"; // for dropdown arrow
import PulseIQ from '../assets/PulseIQ.png';
import { Link } from 'react-router-dom';

function Sidebar({ collapsed, setCollapsed }) {
  const [showServicesDropdown, setShowServicesDropdown] = useState(false);

  const toggleSidebar = () => {
    setCollapsed(!collapsed);
  };

  const toggleServicesDropdown = () => {
    setShowServicesDropdown(!showServicesDropdown);
  };

  return (
    <div className={`sidebar ${collapsed ? 'collapsed' : ''}`}>
      <div className="logo-container">
        <img src={PulseIQ} alt="PulseIQ Logo" className="sidebar-logo" />
      </div>

      <button className="toggle-button" onClick={toggleSidebar}>
        {collapsed ? <FaAnglesRight className="icon" /> : <FaAnglesLeft className="icon" />}
      </button>

      <ul className="menu">
        <li>
          <Link to="/" className="menu-link">Home</Link>
        </li>

        <li onClick={toggleServicesDropdown} className="dropdown-toggle">
          Services
          {!collapsed && (showServicesDropdown ? <FaChevronUp className="dropdown-icon" /> : <FaChevronDown className="dropdown-icon" />)}
        </li>

        {!collapsed && showServicesDropdown && (
          <ul className="submenu">
            <li>
              <Link to="/transactions-throughput" className="menu-link">Transaction Throughput</Link>
            </li>
            <li>
              <Link to="/latency" className="menu-link">Latency</Link>
            </li>
            <li>
              <Link to="/uptime-availability" className="menu-link">Uptime Availability</Link>
            </li>
          </ul>
        )}

        <li>
          <Link to="/about" className="menu-link">About</Link>
        </li>
        <li>
          <Link to="/contact" className="menu-link">Contact</Link>
        </li>
      </ul>
    </div>
  );
}

export default Sidebar;
