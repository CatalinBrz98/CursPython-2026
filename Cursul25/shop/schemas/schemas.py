from pydantic import BaseModel

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

class ProductCreate(BaseModel):
    name: str
    category: str
    price: float
    discount: int
    quantity: int

    email: str
    password: str