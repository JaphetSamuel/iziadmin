from fastapi import FastAPI
from config.app import app
from customer.main import router as cutomers_router
from driver.main import router as driver_router
from wallet.main import router as wallet_router
from order.main import router as order_router
from promotion.main import router as promotion_router
from service.main import router as service_router
from package.main import router as package_router
from auth.main import router as auth_router


app.include_router(auth_router)
app.include_router(cutomers_router)
app.include_router(driver_router)
app.include_router(wallet_router)
app.include_router(order_router)
app.include_router(promotion_router)
app.include_router(service_router)
app.include_router(package_router)



@app.get("/")
async def root():
    return {"message": "Hello World"}

