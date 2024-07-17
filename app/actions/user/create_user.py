from app.exceptions.service_exception import ServiceException
from typing import Optional
from app.models.user import User
from app.constants.service_constants import Status
from fastapi import HTTPException
from datetime import datetime

class CreateUser:
    def __init__(self,name: str,email: str,password: str,user_type: str):
        self.name = name
        self.email = email
        self.password = password
        self.user_type = user_type

    async def run(self):
        try:
            product = await User.find_one({"email": self.email,"status":"active"})
            if product:
                raise HTTPException(status_code=404, detail="email already exists!!")
            create_user_request = {
                "name": self.name,
                "email": self.email,
                "password": self.password,
                "user_type": self.user_type,
                "status": Status.ACTIVE.value,
                "created_at": datetime.now(),
                "updated_at": datetime.now()
            }
            new_user = User(**dict(create_user_request))
            await new_user.create()
            return dict(new_user)["id"]
        except ServiceException as e:
            raise ServiceException(str(e))
        