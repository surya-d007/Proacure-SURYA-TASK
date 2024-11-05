from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime

from . import crud, models, schemas, openai_utils , weather_utils
from typing import List
from .database import engine, Base, get_db
Base.metadata.create_all(bind=engine)

app = FastAPI()


# New endpoint to check weather impact on delivery compliance
@app.post("/suppliers/check-weather-impact")
def check_weather_impact(
    supplier_id: int, latitude: float, longitude: float, delivery_date: str, db: Session = Depends(get_db)
):
    # Fetch weather data for the given location and date
    try:
        weather_data = weather_utils.get_historical_weather(latitude, longitude, delivery_date)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    # Analyze weather impact
    adverse_weather = weather_utils.check_adverse_weather_conditions(weather_data)

    # Update compliance status if adverse weather detected
    if adverse_weather:
        # Find the latest compliance record for the given supplier
        compliance_record = db.query(models.ComplianceRecord).filter(
            models.ComplianceRecord.supplier_id == supplier_id,
            models.ComplianceRecord.date_recorded == datetime.strptime(delivery_date, "%Y-%m-%d").date()
        ).first()

        if compliance_record:
            crud.update_compliance_status(db, compliance_record.id, "Excused - Weather Delay")
            return {"status": "Compliance record updated due to adverse weather conditions"}
        else:
            raise HTTPException(status_code=404, detail="Compliance record not found")
    else:
        return {"status": "No adverse weather conditions detected"}


@app.get("/suppliers", response_model=List[schemas.Supplier])
def read_suppliers(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_suppliers(db, skip=skip, limit=limit)

@app.post("/suppliers", response_model=schemas.Supplier)
def create_supplier(supplier: schemas.SupplierCreate, db: Session = Depends(get_db)):
    return crud.create_supplier(db=db, supplier=supplier)

@app.get("/suppliers/{supplier_id}", response_model=schemas.Supplier)
def read_supplier(supplier_id: int, db: Session = Depends(get_db)):
    db_supplier = crud.get_supplier(db, supplier_id=supplier_id)
    if db_supplier is None:
        raise HTTPException(status_code=404, detail="Supplier not found")
    return db_supplier

@app.post("/suppliers/check-compliance")
def check_compliance(data: dict, db: Session = Depends(get_db)):
    analysis = openai_utils.analyze_compliance(data)
    return {"analysis": analysis}

@app.get("/suppliers/insights")
def get_insights():
    insights = openai_utils.generate_insights()
    return {"insights": insights}
