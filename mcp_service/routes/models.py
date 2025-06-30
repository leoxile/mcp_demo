from typing import List
from fastapi import APIRouter

from ..models import ModelInfo

router = APIRouter()

models: List[ModelInfo] = []

@router.post('/models', response_model=ModelInfo)
def register_model(model: ModelInfo) -> ModelInfo:
    models.append(model)
    return model

@router.get('/models', response_model=List[ModelInfo])
def list_models() -> List[ModelInfo]:
    return models
