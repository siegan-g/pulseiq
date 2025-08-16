import React, { useState } from 'react';
import '../styles/SideNavbar.css';
import { FaAnglesRight, FaAnglesLeft } from "react-icons/fa6";
import { FaChevronDown, FaChevronUp } from "react-icons/fa"; // for dropdown arrow
import PulseIQ from '../assets/PulseIQ.png';

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
        <li>Home</li>

        <li onClick={toggleServicesDropdown} className="dropdown-toggle">
          Services
          {!collapsed && (showServicesDropdown ? <FaChevronUp className="dropdown-icon" /> : <FaChevronDown className="dropdown-icon" />)}
        </li>

        {!collapsed && showServicesDropdown && (
          <ul className="submenu">
            <li>Throughput</li>
            <li>Latency</li>
            <li>Uptime</li>
          </ul>
        )}

        <li>Metrics</li>
      </ul>
    </div>
  );
}

export default Sidebar;
