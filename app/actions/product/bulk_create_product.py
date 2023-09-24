from app.models.product import Product
from app.constants.service_constants import BulkCreate
from datetime import datetime
from app.constants.service_constants import Status
from app.exceptions.service_exception import ServiceException

class BulkCreateProducts():
    def __init__(self) -> None:
        pass

    async def run(self):
        try:
            products_data = BulkCreate.PRODUCTS_DATA.value
            products_ids = []
            for product in products_data:
                product["status"] = Status.ACTIVE.value
                product["created_at"] = datetime.now()
                product["updated_at"] = datetime.now()
                product = Product(**product)
                await product.create()
                products_ids.append(str(dict(product)["id"]))
            return products_ids
        except ServiceException as e:
            raise ServiceException(str(e))

