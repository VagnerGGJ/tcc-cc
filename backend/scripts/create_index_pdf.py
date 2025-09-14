import os
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from app.config import VECTOR_DB_PATH, EMBEDDING_MODEL_NAME, PDF_FILE_PATH

def criar_vetor_db(pdf_path: str, db_path: str):
    """Cria e salva o banco vetorial a partir de um PDF."""
    if not os.path.exists(pdf_path):
        print(f"❌ Erro: Arquivo PDF não encontrado em '{pdf_path}'")
        return

    print(f"Iniciando indexação do PDF: {pdf_path}")
    loader = PyPDFLoader(pdf_path)
    docs = loader.load()
    print(f"PDF carregado. {len(docs)} páginas.")

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    documents = text_splitter.split_documents(docs)
    print(f"Documento dividido em {len(documents)} pedaços.")

    print("Carregando modelo de embeddings (pode demorar na primeira vez)...")
    embeddings = HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL_NAME,
        model_kwargs={'device': 'cpu'}
    )
    
    print("Criando e salvando o banco vetorial...")
    vector_store = FAISS.from_documents(documents, embeddings)
    vector_store.save_local(db_path)
    print(f"✅ Banco vetorial criado e salvo em '{db_path}'!")

if __name__ == "__main__":
    # Cria a pasta para o DB se ela não existir
    if not os.path.exists("vector_stores"):
        os.makedirs("vector_stores")
    
    criar_vetor_db(PDF_FILE_PATH, VECTOR_DB_PATH)