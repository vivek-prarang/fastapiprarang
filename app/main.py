# app/main.py
from fastapi import FastAPI
from app.config.settings import settings
from app.api.v1.router import router as api_v1_router
from app.api.v2.router import router as api_v2_router

app = FastAPI(
    title=settings.app_name,
    debug=settings.debug
)

# Include routers
app.include_router(api_v1_router, prefix="/api/v1")
app.include_router(api_v2_router, prefix="/api/v2")

"""
! The root endpoint returns a simple message with a welcome message to the
* application. This endpoint is not included in the API documentation.
"""




@app.get("/")
def root():
    return {"message": "Welcome to FAPIN!"}

