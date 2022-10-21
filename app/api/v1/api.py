from fastapi import APIRouter

from app.api.v1.endpoints import cycle, touch

api_router = APIRouter()


api_router.include_router(cycle.router, prefix="/cycle")
api_router.include_router(touch.router, prefix="/touch")
