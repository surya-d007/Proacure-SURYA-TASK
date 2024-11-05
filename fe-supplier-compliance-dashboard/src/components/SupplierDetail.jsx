import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { getSupplierById } from "../services/api";

const SupplierDetail = () => {
  const { supplierId } = useParams();
  const [supplier, setSupplier] = useState(null);
  const [error, setError] = useState("");

  useEffect(() => {
    async function fetchSupplier() {
      try {
        const response = await getSupplierById(supplierId);
        setSupplier(response.data);
      } catch (error) {
        setError("Failed to fetch supplier details");
      }
    }
    fetchSupplier();
  }, [supplierId]);

  if (error) return <p>{error}</p>;
  if (!supplier) return <p>Loading...</p>;

  return (
    <div>
      <h1>{supplier.name}</h1>
      <p>Country: {supplier.country}</p>
      <p>Compliance Score: {supplier.compliance_score}</p>
      <p>Last Audit: {supplier.last_audit}</p>
      <h2>Contract Terms</h2>
      <pre>{JSON.stringify(supplier.contract_terms, null, 2)}</pre>
      <h2>Compliance Records</h2>
      <ul>
        {supplier.compliance_records.map((record) => (
          <li key={record.id}>
            {record.metric}: {record.result} - {record.status}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default SupplierDetail;
