from fastapi import HTTPException, APIRouter
import csv
from schemas import UserRegister
from dependencies import login_helper, user_columns

router = APIRouter(
    prefix="/user",
    tags=["user"],
)

@router.get("/login")
def login(email: str, password: str):
    if login_helper(email, password):
        return "Login successful!"
    else:
        raise HTTPException(status_code=401, detail="Wrong user credentials!")

@router.post("/register")
def register(user: UserRegister):
    with open("db/users.csv", mode="r") as f:
        users = csv.DictReader(f)
        for user_csv in users:
            if user_csv["email"] == user.email:
                raise HTTPException(status_code=422, detail="This email is already registered!")

    with open("users.csv", mode="a", newline="") as g:
        users = csv.DictWriter(g, fieldnames=user_columns)
        users.writerow({"email": user.email, "password": user.password})
        return "Registered successfully!"
