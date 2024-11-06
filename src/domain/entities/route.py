from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime

class RouteModel(BaseModel):
    id: Optional[int]
    name: str
    latitude: int
    longitude: int
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    model_config = ConfigDict(from_attributes=True)