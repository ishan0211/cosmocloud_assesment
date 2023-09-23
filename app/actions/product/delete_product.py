from datetime import datetime
from app.exceptions.service_exception import ServiceException
from app.constants.service_constants import Status
from app.models.product import Product
from fastapi import HTTPException

class DeleteOperatorSession:
    def __init__(self,product_name: str):
        self.product_name = product_name
    
    async def delete_product(self):
        product_to_be_deleted = await Product.find_one({"product_name": self.product_name,"status":"active"})
        if not product_to_be_deleted:
            raise HTTPException(status_code=404, detail="product doesn't exists!!")
        product_to_be_deleted.status = Status.INACTIVE.value
        product_to_be_deleted.updated_at = datetime.now()
        await product_to_be_deleted.save()
        return str(dict(product_to_be_deleted)["id"])

    async def run(self):
        try:
            return await self.delete_product()
        except ServiceException as e:
            raise ServiceException(str(e))
