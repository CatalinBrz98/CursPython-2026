from fastapi import HTTPException, APIRouter
import csv
from schemas import ProductCreate, ProductDB
from dependencies import login_helper, product_new_id, products_columns


router = APIRouter(
    prefix="/shop",
    tags=["shop"],
)

@router.get("/products")
def show_products() -> list[ProductDB]:
    with open("db/products.csv", mode="r") as f:
        products = csv.DictReader(f)
        return [ProductDB(**product) for product in products]

@router.get("/product/{product_id}")
def show_product(product_id: int) -> ProductDB:
    with open("db/products.csv", mode="r") as f:
        products = csv.DictReader(f)
        for product in products:
            if int(product["id"]) == product_id:
                return ProductDB(**product)
    raise HTTPException(status_code=404, detail="Product not found")

@router.post("/product/create")
def create_product(product: ProductCreate):
    if login_helper(product.email, product.password):
        with open("db/products.csv", mode="a", newline="") as g:
            products = csv.DictWriter(g, fieldnames=products_columns)
            products.writerow({
                "id": product_new_id(),
                "name": product.name,
                "category": product.category,
                "price": product.price,
                "discount": product.discount,
                "quantity": product.quantity
            })

        return "Product created successfully!"
    else:
        raise HTTPException(status_code=401, detail="Wrong user credentials!")
