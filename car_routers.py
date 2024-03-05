import logging
from fastapi import APIRouter, Depends, status, HTTPException
from database import get_db
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from models import Car
from schemas import CarSchema


logging.basicConfig(format="%(levelname)s: %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)
router = APIRouter(prefix="/car")


@router.post("/", status_code=status.HTTP_201_CREATED)
async def add_car(request: CarSchema, db: Session = Depends(get_db)):
    """Creates a new car record"""
    
    try:
        created_car = Car(**request.model_dump())
        db.add(created_car)
        db.commit()
        db.refresh(created_car)
        return {"status": "success", "car": created_car}
   
    except SQLAlchemyError as err:
        db.rollback()
        logger.exception(f"An error occurred: {err}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="Internal server error")


@router.get("/", status_code=status.HTTP_200_OK)
async def get_cars(db: Session = Depends(get_db)):
    """Fetches information of all the cars in the database."""

    cars = db.query(Car).all()
    if not cars:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"No Cars found")

    return {"status": "success", "cars": cars}


@router.get("/{id}", status_code=status.HTTP_200_OK)
async def get_car(id: str, db: Session = Depends(get_db)):
    """Fetches information of a single car in the database based on the provided car id."""

    car = db.query(Car).get(id)
    if not car:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Car with ID {id} not found")

    return {"status": "success", "car": car}


@router.put("/{id}", status_code=status.HTTP_200_OK)
async def update_car(id: int, request: CarSchema, db: Session = Depends(get_db)):
    """Updates the information of a car based on the provided car id."""

    get_car_query = db.query(Car).filter(Car.id == id)
    car = get_car_query.first()
    if not car:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Car with ID {id} not found")

    try:
        get_car_query.update(request.model_dump())
        db.commit()
        db.refresh(car)
        return {"status": "success", "car": car}

    except SQLAlchemyError as err:
        db.rollback()
        logger.exception(f"An error occurred: {err}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="Internal server error")


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_car_by_id(id: int, db: Session = Depends(get_db)):
    """Deletes a car record from the database based on the provided car id."""

    car = db.query(Car).get(id)
    if not car:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Car with ID {id} not found")

    try:
        db.delete(car)
        db.commit()

    except SQLAlchemyError as err:
        db.rollback()
        logger.exception(f"An error occurred: {err}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="Internal server error")
