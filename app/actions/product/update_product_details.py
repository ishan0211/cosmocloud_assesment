from typing import Optional
from app.models.product import Product
from datetime import datetime
from fastapi import HTTPException
from app.exceptions.service_exception import ServiceException

class UpdateProductDetails():
    def __init__(self,product_name: str,product_price: Optional[float] = None,product_available_quantity: Optional[int] = None):
        self.product_name = product_name
        self.product_price = product_price
        self.product_available_quantity = product_available_quantity

    async def run(self):
        try:
            product = await Product.find_one({"product_name": self.product_name,"status":"active"})
            
            if not product:
                raise HTTPException(status_code=404, detail="product not found!!")
            
            if self.product_available_quantity:
                product.product_available_quantity = self.product_available_quantity
            if self.product_price:
                product.product_price = self.product_price
            product.updated_at = datetime.now()
            await product.save()
            return dict(product)["id"]
        except ServiceException as e:
            raise ServiceException(str(e))

        

