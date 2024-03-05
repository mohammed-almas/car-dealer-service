from pydantic import BaseModel
from typing import Optional


class DealerSchema(BaseModel):

    name: str
    address: str
    contact_no: str


class CarSchema(BaseModel):

    model: str
    price: int
    vehicle_type: Optional[str]
    fuel_type: Optional[str]
    transmission_type: Optional[str]
    engine_no: Optional[str]
    chasis_no: Optional[str]
    color: Optional[str]
    mfg_year: Optional[int]

    dealer_id: int
