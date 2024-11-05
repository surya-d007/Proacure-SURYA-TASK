// App.js
import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import SupplierList from "./components/SupplierList";
import SupplierDetail from "./components/SupplierDetail";
import UploadCompliance from "./components/UploadCompliance";
import ComplianceInsights from "./components/ComplianceInsights";
import Header from "./components/Header";

function App() {
  return (
    <Router>
      <Header />
      <Routes>
        {" "}
        {/* Replace Switch with Routes */}
        <Route path="/" element={<SupplierList />} />
        <Route path="/suppliers/:supplierId" element={<SupplierDetail />} />
        <Route path="/upload-compliance" element={<UploadCompliance />} />
        <Route path="/insights" element={<ComplianceInsights />} />
      </Routes>
    </Router>
  );
}

export default App;
