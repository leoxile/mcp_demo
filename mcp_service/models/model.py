from pydantic import BaseModel
from typing import Optional

class ModelInfo(BaseModel):
    name: str
    version: str
    description: Optional[str] = None
