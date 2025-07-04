# v1 router
# app/api/v1/router.py
from fastapi import APIRouter
from app.api.v1.endpoints import users

router = APIRouter()
router.include_router(users.router, prefix="/users", tags=["Users"])
