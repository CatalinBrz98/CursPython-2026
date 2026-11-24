import csv

user_columns = ["email", "password"]
products_columns = ["id", "name", "category", "price", "discount", "quantity"]


def login_helper(email: str, password: str):
    with open("db/users.csv", mode="r") as f:
        users = csv.DictReader(f)
        for user in users:
            if user["email"] == email and user["password"] == password:
                return True
    return False

def product_new_id():
    with open("db/products.csv", mode="r") as f:
        return len(f.readlines())