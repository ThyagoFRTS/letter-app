from fastapi import FastAPI
from routers.routes import build_routes
from util.fastapi_dependencies import get_query_token, get_token_header

app = FastAPI()

build_routes(app)