# Main
# Arquivo principal da aplicação FastAPI.
# Responsável por inicializar a instância do FastAPI e incluir todas as rotas da aplicação.
# ...

from fastapi import FastAPI
from app.auth.routes import router as auth_router
from app.admin.routes import router as admin_router
from app.ai.routes import router as ai_router

app = FastAPI(title="IA para Apoio ao Sucesso Acadêmico")

app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(admin_router, prefix="/admin", tags=["admin"])
app.include_router(ai_router, prefix="/ai", tags=["IA - RAG Chatbot"])
