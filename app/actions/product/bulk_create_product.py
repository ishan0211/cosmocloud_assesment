from app.models.product import Product
from app.constants.service_constants import BulkCreate
from datetime import datetime
from app.constants.service_constants import Status

class BulkCreateProducts():
    def __init__(self) -> None:
        pass

    async def run(self):
        products_data = BulkCreate.PRODUCTS_DATA.value
        products_ids = []
        for product in products_data:
            product["status"] = Status.ACTIVE.value
            product["created_at"] = datetime.now()
            product["updated_at"] = datetime.now()
            print(product)
            product = Product(**product)
            await product.create()
            products_ids.append(str(dict(product)["id"]))
        return products_ids


