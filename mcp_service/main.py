from fastapi import FastAPI

from .routes import models as models_routes

app = FastAPI(title="MCP Service")

app.include_router(models_routes.router)
