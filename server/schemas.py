from pydantic import BaseModel
from typing import List, Optional
from datetime import date

class SupplierBase(BaseModel):
    name: str
    country: str
    contract_terms: dict
    compliance_score: int
    last_audit: date

class SupplierCreate(SupplierBase):
    pass

class Supplier(SupplierBase):
    id: int

    class Config:
        orm_mode = True

class ComplianceRecordBase(BaseModel):
    metric: str
    date_recorded: date
    result: float
    status: str

class ComplianceRecordCreate(ComplianceRecordBase):
    supplier_id: int

class ComplianceRecord(ComplianceRecordBase):
    id: int

    class Config:
        orm_mode = True
