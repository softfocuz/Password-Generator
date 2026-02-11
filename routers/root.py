from fastapi import APIRouter
from app.password_gen import password_generator

router = APIRouter()

@router.get('/')
def index():
    return f"PASSWORD GENERATOR: {password_generator()}"
