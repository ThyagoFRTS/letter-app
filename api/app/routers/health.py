from fastapi import APIRouter, Depends, HTTPException
from util.fastapi_dependencies import get_token_header

router = APIRouter(
    prefix="/health", 
    tags=["healthly"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},

)

@router.get("/status")
async def check_status():
    return { "status": "healthly" }