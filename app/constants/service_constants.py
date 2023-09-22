from enum import Enum


class UserAction(Enum):
    LOGIN = "login"
    LOGOUT = 'logout'


class Status(Enum):
    INACTIVE = "inactive"
    ACTIVE = "active"


class JobCardStatus(Enum):
    COMPLETED = "COMPLETED"
    IN_PROGRESS = "IN_PROGRESS"
