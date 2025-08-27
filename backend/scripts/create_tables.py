"""
Cria todas as tabelas do banco de dados.
Execute apenas uma vez antes de começar a usar o backend.
"""

from app.database import Base, engine
from app.models.admin_user import AdminUser

Base.metadata.create_all(bind=engine)
print("Tabelas criadas com sucesso!")