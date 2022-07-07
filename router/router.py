from fastapi import APIRouter

from api.app.cruds import board_crud


api = APIRouter()

api.include_router(board_crud.router, prefix="/board", tags=["Board"])