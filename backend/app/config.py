# Config
# Carrega variáveis de ambiente e configurações do projeto, como JWT e banco de dados

import os
from dotenv import load_dotenv

load_dotenv()

# --- Configurações de Autenticação e JWT ---
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 60))

# --- Configuração do Banco de Dados Principal (PostgreSQL/SQLite) ---
DATABASE_URL = os.getenv("DATABASE_URL")

# --- Configurações da IA (RAG com Ollama) ---
VECTOR_DB_PATH = os.getenv("VECTOR_DB_PATH", "vector_stores/db_faiss")
EMBEDDING_MODEL_NAME = os.getenv("EMBEDDING_MODEL_NAME", "BAAI/bge-m3")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3:8b")
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11435")

# PDF
PDF_FILE_PATH = os.getenv("PDF_FILE_PATH", "app/pdf/unip.pdf") 