from fastapi import APIRouter,Query
from beanie import PydanticObjectId
from app.exceptions.service_exception import ServiceException
from app.api.schema.service_response import SessionResponse
from app.api.schema.signup_user_request import CreateSignupRequest
from app.actions.user.create_user import CreateUser
from app.actions.user.add_market_data import AddMarketData
from app.actions.user.list_market_price import ListMarketPrice 
from typing import Optional

router = APIRouter(prefix="/users")

# @router.post("/", tags=["users"])
# async def login_user(email: email,password: password):
#     try:
#         product_id = await CreateOrder(**dict(create_request)).run()
#         return SessionResponse(message="success !!", status=200, data={"product_id": str(product_id)})
#     except ServiceException as e:
#         return SessionResponse(message=str(e), status=404, data=None)

@router.post('/', tags=["users"])    
async def signup_user(create_request: CreateSignupRequest):
    try:
        id = await CreateUser(**dict(create_request)).run()
        return SessionResponse(message="success !!", status=200, data={"id": str(id)})
    except ServiceException as e:
        return SessionResponse(message=str(e), status=404, data=None)

@router.post('/fill_data',tags=["users"])
async def fill_market_data():
    try:
        await AddMarketData().run()
        return SessionResponse(message="success !!", status=200, data={})
    except ServiceException as e:
        return SessionResponse(message=str(e), status=404, data=None)

@router.get('/', tags=["users"])    
async def list_market_price(
    name: Optional[str] = Query(None),
    page: int = Query(1, ge=1),
    page_limit: int = Query(20, le=100),
):
    prices = await ListMarketPrice(
        name = name,
        page=page,
        page_limit=page_limit
    ).run()

    return prices
