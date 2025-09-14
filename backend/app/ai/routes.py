# Routes
# Define os endpoints de AI para consulta baseada em documentos PDF

from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from .service import RAGService, get_rag_service

router = APIRouter()

class QueryRequest(BaseModel):
    question: str

class QueryResponse(BaseModel):
    answer: str

@router.post("/query", response_model=QueryResponse)
def ask_question_endpoint(
    request: QueryRequest,
    rag_service: RAGService = Depends(get_rag_service)
):
    """
    Recebe uma pergunta e retorna a resposta baseada no documento PDF.
    """
    try:
        answer = rag_service.ask_question(request.question)
        return QueryResponse(answer=answer)
    except Exception as e:
        print(f"Erro no endpoint de query: {e}")
        raise HTTPException(status_code=500, detail="Ocorreu um erro ao processar sua pergunta.")

@router.get("/health")
def health_check():
    """Endpoint para verificar se o serviço está funcionando"""
    return {"status": "OK", "message": "Serviço de IA funcionando!"}
