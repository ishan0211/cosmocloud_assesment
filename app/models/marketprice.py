from beanie import Document,Indexed
from datetime import datetime

class MarketPrice(Document):
    name: str
    symbol: str
    market_cap_rank: float
    current_price: float
    created_at: datetime
    updated_at: datetime