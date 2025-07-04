# v1 user endpoints
# v2 user endpoints
# app/api/v1/endpoints/user_routes.py
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_users():
    return [{"id": 1, "name": "John x"}]
