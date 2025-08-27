# Routes
# Define os endpoints de autenticação do admin, incluindo login e geração de token JWT

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.admin_user import AdminUserLogin
from app.models.admin_user import AdminUser
from app.auth.security import verify_password, create_access_token
from app.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/login")
def login(user: AdminUserLogin, db: Session = Depends(get_db)):
    admin = db.query(AdminUser).filter(AdminUser.username == user.username).first()
    if not admin or not verify_password(user.password, admin.password_hash):
        raise HTTPException(status_code=401, detail="Credenciais inválidas")
    token = create_access_token({"sub": admin.username})
    return {"access_token": token, "token_type": "bearer"}
