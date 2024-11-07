import React, { useEffect, useState } from "react";
import { getComplianceInsights } from "../services/api";

const ComplianceInsights = () => {
  const [insights, setInsights] = useState([]);
  const [error, setError] = useState("");

  useEffect(() => {
    async function fetchInsights() {
      try {
        const response = await getComplianceInsights();
        setInsights(response.data);
      } catch (error) {
        setError("Failed to load compliance insights");
      }
    }
    fetchInsights();
  }, []);

  return (
    <div>
      <h2>Compliance Insights</h2>
      {error && <p>{error}</p>}
      <ul>
        {insights.map((insight, index) => (
          <li key={index}>{insight}</li>
        ))}
      </ul>
    </div>
  );
};

export default ComplianceInsights;
