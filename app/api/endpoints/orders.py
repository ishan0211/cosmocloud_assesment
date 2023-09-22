from fastapi import APIRouter
from beanie import PydanticObjectId
from uuid import UUID
from fastapi import HTTPException
from app.exceptions.service_exception import ServiceException
from app.api.schema.create_product_request import CreateProductRequest

router = APIRouter(prefix="/orderes")

@router.post("/", tags=['jc_sessions'])
async def create_new_product(create_request: CreateProductRequest):
    try:
        jc_session_id = await StartSession(operator_id,desk_id).run()
        return UserSessionResponse(message="success !!", status=200, data={"jc_session_id": jc_session_id})
    except ServiceException as e:
        return UserSessionResponse(message=str(e), status=404, data=None)

@router.delete("/", tags=['jc_sessions'])
async def end_session(jc_session_id: PydanticObjectId,operator_id: UUID):
    try:
        jc_session_id = await EndSession(jc_session_id,operator_id).run()
        return UserSessionResponse(message="success !!", status=200, data={"jc_session_id": jc_session_id})
    except ServiceException as e:
        return UserSessionResponse(message=str(e), status=404, data=None)


