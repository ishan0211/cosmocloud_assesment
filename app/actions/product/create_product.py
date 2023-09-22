from app.models import SessionData
from app.exceptions.service_exception import ServiceException
from typing import Optional
from beanie import PydanticObjectId
from app.models.product import Product
from app.constants.service_constants import Status


class CreateProduct:
    def __init__(self,product_name: str,product_price: float,product_available_quantity: Optional[int] = 0):
        self.product_name = product_name
        self.product_price = product_price
        self.product_available_quantity = product_available_quantity

    async def run(self):
        try:
            create_product_request = {
                "product_name": self.product_name,
                "product_price": self.product_price,
                "product_available_quantity": self.product_available_quantity,
                "status": Status.ACTIVE.value
            }
            new_product = Product(**dict(create_product_request))
            await new_product.create()
            return dict(new_product)["id"]
        except ServiceException as e:
            raise ServiceException(str(e))
        