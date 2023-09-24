from fastapi import APIRouter,Query
from beanie import PydanticObjectId
from app.exceptions.service_exception import ServiceException
from app.api.schema.service_response import SessionResponse
from app.api.schema.create_order_request import CreateOrderRequest
from app.actions.order.create_order import CreateOrder
from app.actions.order.get_order_by_id import GetOrderById
from app.actions.order.list_orders import ListOrders
from app.actions.order.cancel_order import CancelOrder

router = APIRouter(prefix="/orders")

@router.post("/", tags=['orders'])
async def create_order(create_request: CreateOrderRequest):
    try:
        product_id = await CreateOrder(**dict(create_request)).run()
        return SessionResponse(message="success !!", status=200, data={"product_id": str(product_id)})
    except ServiceException as e:
        return SessionResponse(message=str(e), status=404, data=None)

@router.get('/', tags=["orders"])    
async def list_orders(page: int = Query(1, ge=1),page_limit: int = Query(10)):
    try:
        orders = await ListOrders(page=page,page_limit=page_limit).run()
        return SessionResponse(message="success !!", status=200, data={"orders": orders})
    except ServiceException as e:
        return SessionResponse(message=str(e), status=404, data=None)

@router.get('/{order_id}', tags=["orders"])
async def get_order_by_id(order_id: PydanticObjectId):
    try:
        order = await GetOrderById(order_id).run()
        return SessionResponse(message="success !!", status=200, data={"order_details":order})
    except ServiceException as e:
        return SessionResponse(message=str(e), status=404, data=None)
    
@router.delete('/', tags=["orders"])
async def cancel_order(order_id: PydanticObjectId):
    try:
        order = await CancelOrder(order_id).run()
        return SessionResponse(message="success !!", status=200, data={"order_details":order})
    except ServiceException as e:
        return SessionResponse(message=str(e), status=404, data=None)

