from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class RouteModel(BaseModel):
    id: Optional[int]
    name: str
    latitude: int
    longitude: int
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    class Config:
        from_attributes = True