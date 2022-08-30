from pydantic import BaseModel, Field


class ExternalServiceUser(BaseModel):
    username: str
    is_authenticated: bool = Field(default=False)
