from fastapi import FastAPI

from database import engine, Base
from dealer_routers import router as dealer_routers
from car_routers import router as car_routers


Base.metadata.create_all(bind=engine)
app = FastAPI()

# Including routers from all controllers
app.include_router(dealer_routers)
app.include_router(car_routers)

# Root address
@app.get("/")
def home():
    return {"message": "Welcome to Car Dealer Service"}
