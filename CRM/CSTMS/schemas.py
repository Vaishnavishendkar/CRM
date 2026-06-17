from pydantic import BaseModel
from typing import Optional



def Register(BaseModel):
    username: str
    email: str
    password: str
    roll: str
    created_at: Optional[str] = None
    updated_at: Optional[str] = None