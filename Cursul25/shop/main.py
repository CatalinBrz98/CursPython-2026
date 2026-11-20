from fastapi import FastAPI, HTTPException
import csv
from pydantic import BaseModel

app = FastAPI()

class UserRegister(BaseModel):
    email: str
    password: str

class ProductDB(BaseModel):
    id: int
    name: str
    category: str
    price: float
    discount: int
    quantity: int

@app.get("/")
def home():
    return {"message": "Welcome to my online shop!"}

@app.get("/login")
def login(email: str, password: str):
    with open("users.csv", mode="r") as f:
        users = csv.DictReader(f)
        for user in users:
            if user["email"] == email and user["password"] == password:
                return "Login successful!"
    return "Wrong details!"

@app.post("/register")
def register(user: UserRegister):
    with open("users.csv", mode="r") as f:
        users = csv.DictReader(f)
        for user_csv in users:
            if user_csv["email"] == user.email:
                raise HTTPException(status_code=422, detail="This email is already registered!")

    with open("users.csv", mode="a", newline="") as g:
        users = csv.DictWriter(g, fieldnames=["email", "password"])
        users.writerow({"email": user.email, "password": user.password})
        return "Registered successfully!"

@app.get("/shop/products")
def show_products() -> list[ProductDB]:
    with open("products.csv", mode="r") as f:
        products = csv.DictReader(f)
        return [ProductDB(**product) for product in products]

@app.get("/shop/product/{product_id}")
def show_product(product_id: int) -> ProductDB:
    with open("products.csv", mode="r") as f:
        products = csv.DictReader(f)
        for product in products:
            if int(product["id"]) == product_id:
                return ProductDB(**product)
    raise HTTPException(status_code=404, detail="Product not found")

@app.post("/shop/product/create")
def create_product(user: UserRegister):
    with open("users.csv", mode="r") as f:
        users = csv.DictReader(f)
        for user_csv in users:
            if user_csv["email"] == user.email:
                raise HTTPException(status_code=422, detail="This email is already registered!")

    with open("users.csv", mode="a", newline="") as g:
        users = csv.DictWriter(g, fieldnames=["email", "password"])
        users.writerow({"email": user.email, "password": user.password})
        return "Registered successfully!"