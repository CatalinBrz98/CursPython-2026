from fastapi import FastAPI
from routers import shop_router, users_router

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to my online shop!"}

app.include_router(users_router)
app.include_router(shop_router)
