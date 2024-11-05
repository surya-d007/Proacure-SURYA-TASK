import React, { useState } from "react";
import { checkCompliance } from "../services/api";

const UploadCompliance = ({ supplierId }) => {
  const [complianceData, setComplianceData] = useState("");
  const [message, setMessage] = useState("");

  const handleUpload = async () => {
    try {
      await checkCompliance(supplierId, { complianceData });
      setMessage("Compliance data uploaded successfully!");
    } catch (error) {
      setMessage("Failed to upload compliance data.");
    }
  };

  return (
    <div>
      <h2>Upload Compliance Data</h2>
      <textarea
        value={complianceData}
        onChange={(e) => setComplianceData(e.target.value)}
        placeholder="Enter compliance data in JSON format"
      />
      <button onClick={handleUpload}>Submit</button>
      {message && <p>{message}</p>}
    </div>
  );
};

export default UploadCompliance;
