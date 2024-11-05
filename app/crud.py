from sqlalchemy.orm import Session
from . import models, schemas
from .models import ComplianceRecord

def update_compliance_status(db: Session, record_id: int, status: str):
    record = db.query(ComplianceRecord).filter(ComplianceRecord.id == record_id).first()
    if record:
        record.status = status
        db.commit()
        db.refresh(record)
        return record
    else:
        raise Exception("Compliance record not found")
    
    
def get_suppliers(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Supplier).offset(skip).limit(limit).all()

def get_supplier(db: Session, supplier_id: int):
    return db.query(models.Supplier).filter(models.Supplier.id == supplier_id).first()

def create_supplier(db: Session, supplier: schemas.SupplierCreate):
    db_supplier = models.Supplier(**supplier.dict())
    db.add(db_supplier)
    db.commit()
    db.refresh(db_supplier)
    return db_supplier

def create_compliance_record(db: Session, record: schemas.ComplianceRecordCreate):
    db_record = models.ComplianceRecord(**record.dict())
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return db_record
