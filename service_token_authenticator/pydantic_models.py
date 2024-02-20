from pydantic import BaseModel


class ExternalServiceUser(BaseModel):
    username: str
    is_authenticated: bool = False
