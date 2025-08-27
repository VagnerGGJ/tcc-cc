"""
Cria um usuário admin inicial no banco.
Execute apenas uma vez, depois do init_db.py.
"""

from app.database import SessionLocal
from app.models.admin_user import AdminUser
from app.auth.security import hash_password

db = SessionLocal()

admin = AdminUser(
    username="admin",
    email="admin@tcc.com",
    password_hash=hash_password("123456")
)

db.add(admin)
db.commit()
db.close()
print("Admin criado com sucesso!")
