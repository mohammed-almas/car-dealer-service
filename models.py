from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class Dealer(Base):
    __tablename__ = "dealers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    address = Column(String(100), nullable=False)
    contact_no = Column(String(20), nullable=False)

    cars = relationship("Car", back_populates="dealers", cascade="all, delete")


class Car(Base):
    __tablename__ = "cars"

    id = Column(Integer, primary_key=True, index=True)
    model = Column(String(50), nullable=False)
    price = Column(Float, nullable=False)
    vehicle_type = Column(String, nullable=True)
    fuel_type = Column(String, nullable=True)
    transmission_type = Column(String, nullable=True)
    engine_no = Column(String, nullable=True)
    chasis_no = Column(String, nullable=True)
    color = Column(String, nullable=True)
    mfg_year = Column(Integer, nullable=True)

    dealer_id = Column(Integer, ForeignKey("dealers.id", ondelete="CASCADE"))

    dealers = relationship("Dealer", back_populates="cars")
