# app/pdf/routes.py

import os
from fastapi import APIRouter, Depends, UploadFile, File, Form, HTTPException, status
from app.deps import get_current_admin
from app import config

router = APIRouter()

# Usa o diretório vindo do config
PDF_DIR = config.PDF_DIR
os.makedirs(PDF_DIR, exist_ok=True)


@router.post("/upload")
async def upload_pdf(
    usuario: str = Form(...),
    file: UploadFile = File(...),
    current_admin: dict = Depends(get_current_admin)
):
    """
    Upload de arquivos PDF (apenas administradores).
    - Valida token JWT
    - Valida se o arquivo é PDF
    - Salva o arquivo na pasta configurada
    """

    # Valida tipo de arquivo
    if file.content_type != "application/pdf":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Apenas arquivos PDF são permitidos."
        )

    # Caminho final do arquivo
    file_path = os.path.join(PDF_DIR, file.filename)

    # Salva o arquivo
    with open(file_path, "wb") as f:
        content = await file.read()
        f.write(content)

    return {
        "message": "Arquivo PDF enviado com sucesso!",
        "usuario": usuario,
        "filename": file.filename,
        "path": file_path
    }
