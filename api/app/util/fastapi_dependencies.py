from typing import Annotated
from fastapi import Header, HTTPException


async def get_token_header(X_Api_Key: Annotated[str, Header()]):
    if X_Api_Key != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")


async def get_query_token(token: str):
    if token != "test":
        raise HTTPException(status_code=400, detail="No Jessica token provided")