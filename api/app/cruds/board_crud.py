from fastapi import APIRouter, Query, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from manager.useData import get_events, load_json


router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get('')
async def get_notices(request: Request, num: int = Query(...)) -> HTMLResponse:
    if get_events(num):
        items = load_json(get_events(num))
    return templates.TemplateResponse("board.html", {"request": request, "items": items})
