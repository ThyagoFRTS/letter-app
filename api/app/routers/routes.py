from fastapi import FastAPI
from routers.health import router as health_router

def build_routes(app: FastAPI, prefix="/api/v1"):
    app.include_router(
        health_router,
        prefix=prefix
    )