from fastapi import APIRouter, Query

from manager.useData import get_events, load_json


router = APIRouter()


@router.get('')
async def get_10notices(num: int = Query(...)):
    if get_events(num):
        result = load_json(get_events(num))
    return result
