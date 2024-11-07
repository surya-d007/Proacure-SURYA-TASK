import React, { useEffect, useState } from "react";
import { getSuppliers } from "../services/api";

const SupplierList = () => {
  const [suppliers, setSuppliers] = useState([]);
  const [error, setError] = useState("");

  useEffect(() => {
    async function fetchSuppliers() {
      try {
        const response = await getSuppliers();
        setSuppliers(response.data);
      } catch (error) {
        setError("Failed to fetch suppliers");
      }
    }
    fetchSuppliers();
  }, []);

  return (
    <div>
      <h1>Suppliers</h1>
      {error && <p>{error}</p>}
      <ul>
        {suppliers.map((supplier) => (
          <li key={supplier.id}>
            <h2>{supplier.name}</h2>
            <p>Compliance Score: {supplier.compliance_score}</p>
            <p>Last Audit: {supplier.last_audit}</p>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default SupplierList;
