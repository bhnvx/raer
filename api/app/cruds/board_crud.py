from fastapi import Depends, HTTPException, APIRouter

from manager.useData import get_events, load_json


router = APIRouter()


@router.get('/')
async def Home():
    if get_events(1):
        result = load_json(get_events(1))
    return result