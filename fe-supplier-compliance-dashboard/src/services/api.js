import axios from "axios";

const API_BASE_URL = "http://localhost:8000"; // Change this if your backend runs on a different URL

export const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    "Content-Type": "application/json",
  },
});

// GET all suppliers
export const getSuppliers = () => api.get("/suppliers");

// GET a single supplier by ID
export const getSupplierById = (id) => api.get(`/suppliers/${id}`);

// POST to add new compliance data and analyze it
export const checkCompliance = (supplierId, complianceData) =>
  api.post(`/suppliers/check-compliance`, complianceData);

// GET AI-generated insights for suppliers
export const getComplianceInsights = () => api.get("/suppliers/insights");

// POST to check weather impact for compliance
export const checkWeatherImpact = (data) =>
  api.post(`/suppliers/check-weather-impact`, data);
