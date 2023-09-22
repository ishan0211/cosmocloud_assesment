from beanie import Document

class UserAddress(Document):
    city: str
    country: str
    zip_code: str