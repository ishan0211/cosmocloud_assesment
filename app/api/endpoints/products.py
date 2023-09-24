from fastapi import APIRouter,Query
from app.exceptions.service_exception import ServiceException
from app.api.schema.create_product_request import CreateProductRequest
from app.actions.product.create_product import CreateProduct
from app.api.schema.service_response import SessionResponse
from typing import Optional
from app.actions.product.list_products import ListProducts
from app.actions.product.update_product_details import UpdateProductDetails
from app.api.schema.update_product_request import UpdateProductRequest
from app.actions.product.bulk_create_product import BulkCreateProducts

router = APIRouter(prefix="/products")

@router.post("/", tags=['products'])
async def create_new_product(create_request: CreateProductRequest):
    try:
        product_id = await CreateProduct(**dict(create_request)).run()
        return SessionResponse(message="success !!", status=200, data={"product_id": str(product_id)})
    except ServiceException as e:
        return SessionResponse(message=str(e), status=404, data=None)

@router.post("/bulk", tags=['products'])
async def bulk_create_product():
    try:
        product_ids = await BulkCreateProducts().run()
        return SessionResponse(message="success !!", status=200, data={"product_ids": product_ids})
    except ServiceException as e:
        return SessionResponse(message=str(e), status=404, data=None)

@router.get('/', tags=["products"])    
async def list_products(
    product_name: Optional[str] = Query(None),
    min_price: Optional[float] = Query(None),
    max_price: Optional[float] = Query(None),
    page: int = Query(1, ge=1),
    page_limit: int = Query(10, le=100),
):
    products = await ListProducts(
        product_name = product_name,
        min_price = min_price,
        max_price = max_price,
        page=page,
        page_limit=page_limit
    ).run()

    return products

@router.put('/', tags=["products"])
async def update_product_details(update_request: UpdateProductRequest):
    try:
        product_id = await UpdateProductDetails(**dict(update_request)).run()
        return SessionResponse(message="success !!", status=200, data={"product_id": str(product_id)})
    except ServiceException as e:
        return SessionResponse(message=str(e), status=404, data=None)