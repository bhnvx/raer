from fastapi import Depends, HTTPException, APIRouter


router = APIRouter()


@router.get('/')
async def Home():
    return "Hellow, World!"