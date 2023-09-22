from pydantic import BaseModel

class ListProductRequest(BaseModel):
    product_name: str = None
    min_quantity: int = None
    max_quantity: int = None
    min_price: float = None
    max_price: float = None