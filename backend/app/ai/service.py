import os
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.llms import Ollama
from langchain.prompts import ChatPromptTemplate
from app.config import (
    VECTOR_DB_PATH,
    EMBEDDING_MODEL_NAME,
    OLLAMA_MODEL,
    OLLAMA_BASE_URL
)

class RAGService:
    def __init__(self):
        self.rag_chain = self._load_rag_chain()
        print("✅ Serviço de RAG iniciado e pronto para receber perguntas.")

    def _load_rag_chain(self):
        if not os.path.exists(VECTOR_DB_PATH):
            raise FileNotFoundError(
                f"Banco de dados vetorial não encontrado em '{VECTOR_DB_PATH}'. "
                "Execute o script de indexação primeiro."
            )

        embeddings = HuggingFaceEmbeddings(
            model_name=EMBEDDING_MODEL_NAME,
            model_kwargs={'device': 'cpu'}
        )
        
        vector_store = FAISS.load_local(
            VECTOR_DB_PATH, 
            embeddings, 
            allow_dangerous_deserialization=True
        )

        llm = Ollama(
            model=OLLAMA_MODEL,
            temperature=0.2,
            base_url=OLLAMA_BASE_URL
        )
        
        retriever = vector_store.as_retriever(search_kwargs={"k": 6})
        
        prompt = ChatPromptTemplate.from_template("""
Você é um assistente especialista, focado em extrair informações do manual da UNIP de forma direta e precisa para responder a perguntas.
                                                  
Baseie sua resposta estritamente no contexto fornecido.
                                                  
- Para perguntas sobre siglas (como "o que é SEPI?"), sempre comece fornecendo o nome completo da sigla e depois explique seu significado com base no texto.
- Responda de forma natural e objetiva, sem adicionar frases desnecessárias como "A pergunta é clara" ou repetir as instruções.
- Se a informação não estiver no contexto, simplesmente afirme: "Não encontrei essa informação no documento."

Contexto:
{context}
                                                  
Pergunta:
{input}
                                                  
Resposta em Português:
""")
        
        document_chain = create_stuff_documents_chain(llm, prompt)
        return create_retrieval_chain(retriever, document_chain)

    def ask_question(self, query: str) -> str:
        if not self.rag_chain:
            return "Erro: A cadeia de RAG não foi inicializada."
        
        response = self.rag_chain.invoke({"input": query})
        return response.get("answer", "Não foi possível gerar uma resposta.")

rag_service_instance = None

def get_rag_service() -> RAGService:
    global rag_service_instance
    if rag_service_instance is None:
        rag_service_instance = RAGService()
    return rag_service_instance