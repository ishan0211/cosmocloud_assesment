from fastapi import APIRouter,Query,HTTPException,Body
from beanie import PydanticObjectId
from uuid import UUID
from app.exceptions.service_exception import ServiceException
from app.api.schema.create_product_request import CreateProductRequest
from app.actions.product.create_product import CreateProduct
from app.api.schema.service_response import SessionResponse
from typing import List,Optional
from app.actions.product.list_products import ListProducts
from app.actions.product.update_product_details import UpdateProductDetails
from app.api.schema.update_product_request import UpdateProductRequest
from app.api.schema.create_order_request import CreateOrderRequest
from app.actions.order.create_order import CreateOrder

router = APIRouter(prefix="/orders")

@router.post("/", tags=['orders'])
async def create_order(create_request: CreateOrderRequest):
    try:
        product_id = await CreateOrder(**dict(create_request)).run()
        return SessionResponse(message="success !!", status=200, data={"product_id": str(product_id)})
    except ServiceException as e:
        return SessionResponse(message=str(e), status=404, data=None)

@router.delete("/", tags=['orders'])
async def delete_product(product_name: str):
    try:
        jc_session_id = await EndSession(jc_session_id,operator_id).run()
        return UserSessionResponse(message="success !!", status=200, data={"jc_session_id": jc_session_id})
    except ServiceException as e:
        return UserSessionResponse(message=str(e), status=404, data=None)

@router.get('/', tags=["orders"])    
async def list_products(
    product_name: Optional[str] = Query(None),
    min_quantity: Optional[int] = Query(None),
    max_quantity: Optional[int] = Query(None),  
    min_price: Optional[float] = Query(None),
    max_price: Optional[float] = Query(None),
    page: int = Query(1, ge=1),
    page_limit: int = Query(10, le=100),
):
    products = await ListProducts(
        product_name = product_name,
        min_quantity=min_quantity,
        max_quantity = max_quantity,
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


