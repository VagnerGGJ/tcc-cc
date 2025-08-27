# Routes
# Define os endpoints administrativos, protegidos pelo login do admin

from fastapi import APIRouter, Depends
from app.deps import get_current_admin

router = APIRouter()

@router.get("/test")
def test_admin(current_admin=Depends(get_current_admin)):
    return {"message": "Admin autenticado!", "admin": current_admin["username"]}
