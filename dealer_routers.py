import logging
from fastapi import APIRouter, Depends, status, HTTPException
from database import get_db
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from models import Dealer
from schemas import DealerSchema


logging.basicConfig(format="%(levelname)s: %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)
router = APIRouter(prefix="/dealer")


@router.post("/", status_code=status.HTTP_201_CREATED)
async def add_dealer(request: DealerSchema, db: Session = Depends(get_db)):
    """Creates a new dealer record"""

    try:
        created_dealer = Dealer(**request.model_dump())
        db.add(created_dealer)
        db.commit()
        db.refresh(created_dealer)
        return {"status": "success", "dealer": created_dealer}

    except SQLAlchemyError as err:
        db.rollback()
        logger.exception(f"An error occurred: {err}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="Internal server error")


@router.get("/", status_code=status.HTTP_200_OK)
async def get_dealers(db: Session = Depends(get_db)):
    """Fetches information of all the dealers in the database."""

    dealers = db.query(Dealer).all()
    if not dealers:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="No Dealers found")

    return {"status": "success", "dealers": dealers}


@router.get("/{id}", status_code=status.HTTP_200_OK)
async def get_dealer_by_id(id: str, db: Session = Depends(get_db)):
    """Fetches information of a single dealer in the database based on the provided dealer id."""

    dealer = db.query(Dealer).get(id)
    if not dealer:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Dealer with ID {id} not found")

    return {"status": "success", "dealer": dealer}


@router.put("/{id}", status_code=status.HTTP_200_OK)
async def update_dealer(id: int, request: DealerSchema, db: Session = Depends(get_db)):
    """Updates the information of a dealer based on the provided dealer id."""

    get_dealer_query = db.query(Dealer).filter(Dealer.id == id)
    dealer = get_dealer_query.first()
    if not dealer:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Dealer with ID {id} not found")

    try:
        get_dealer_query.update(request.model_dump())
        db.commit()
        db.refresh(dealer)
        return {"status": "success", "dealer": dealer}

    except SQLAlchemyError as err:
        db.rollback()
        logger.exception(f"An error occurred: {err}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="Internal server error")
    

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_dealer_by_id(id: int, db: Session = Depends(get_db)):
    """Deletes a dealer record from the database based on the provided dealer id."""

    dealer = db.query(Dealer).get(id)
    if not dealer:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Dealer with ID {id} not found")

    try:
        db.delete(dealer)
        db.commit()

    except SQLAlchemyError as err:
        db.rollback()
        logger.exception(f"An error occurred: {err}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="Internal server error")
