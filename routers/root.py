from fastapi import APIRouter
from app.password_gen import password_generator

router = APIRouter()

@router.get("/password")
def get_password():
    return {"result": password_generator()}
