// Header.js
import React from "react";
import { Link } from "react-router-dom";

const Header = () => (
  <nav>
    <Link to="/">Suppliers</Link> |
    <Link to="/upload-compliance">Upload Compliance Data</Link> |
    <Link to="/insights">Compliance Insights</Link>
  </nav>
);

export default Header;
