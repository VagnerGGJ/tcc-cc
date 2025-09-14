# 📚 IA para Apoio ao Sucesso Acadêmico

<p align="center">
  <em>Uma solução inteligente para reduzir a evasão escolar e melhorar a comunicação institucional no ensino superior</em>
</p>

<p align="center">
  <a href="#">
    <img src="https://img.shields.io/badge/status-em%20desenvolvimento-yellow?style=for-the-badge" alt="Status">
  </a>
  <a href="#">
    <img src="https://img.shields.io/badge/python-3.11-blue?style=for-the-badge" alt="Python">
  </a>
  <a href="#">
    <img src="https://img.shields.io/badge/fastapi-0.111.1-009688?style=for-the-badge" alt="FastAPI">
  </a>
  <a href="#">
    <img src="https://img.shields.io/badge/postgresql-15.4-blue?style=for-the-badge" alt="PostgreSQL">
  </a>
  <a href="#">
    <img src="https://img.shields.io/badge/sqlalchemy-2.0.22-4169E1?style=for-the-badge" alt="SQLAlchemy">
  </a>
</p>

---

## 📖 Sobre o Projeto

A evasão escolar no ensino superior brasileiro é um desafio estrutural que impacta milhares de estudantes todos os anos.  
Este projeto — desenvolvido como Trabalho de Conclusão de Curso — propõe a criação de uma Inteligência Artificial modular integrada a aplicativos universitários, oferecendo respostas rápidas, orientações personalizadas e suporte contínuo.

O **backend** atual é responsável pela autenticação do usuário **admin**, que gerencia o cadastro das informações utilizadas para o treinamento da IA. Além disso, ele oferece suporte às consultas por meio do Chatbot, integrado ao modelo **Llama3** fornecido pela **Ollama**. A IA foi treinada com o Manual do Aluno da UNIP, que serve como sua principal fonte de conhecimento para gerar respostas precisas.

---

## 🏗️ Arquitetura do Backend

O backend é desenvolvido em **Python** com **FastAPI**, utilizando **SQLAlchemy** para ORM e **JWT** para autenticação.

### Estrutura de Pastas

```
backend/
├── app/
│   ├── ai/                 # Endpoints de IA
│   ├── pdf/                # Endpoints de PDF
│   ├── auth/               # Endpoints de autenticação do admin
│   │   └── routes.py
│   ├── admin/              # Endpoints administrativos protegidos
│   │   └── routes.py
│   ├── models/             # Modelos do banco de dados (AdminUser)
│   ├── schemas/            # Schemas Pydantic para validação
│   ├── deps.py             # Dependências e validação de token JWT
│   ├── security.py         # Hash de senha e criação de JWT
│   ├── database.py         # Configuração do SQLAlchemy (engine e session)
│   └── config.py           # Variáveis de ambiente e configurações
├── scripts/                # Scripts auxiliares para inicialização
│   ├── create_tables.py    # Cria tabelas do banco de dados
│   └── create_admin.py     # Cria o usuário admin inicial
├── venv/                   # Ambiente virtual
├── main.py                 # Ponto de entrada da aplicação
├── requirements.txt        # Dependências do projeto
└── README.md               # Este documento
```

## ⚙️ Configuração do ambiente

Siga os passos abaixo para preparar e rodar o projeto.

### 1. Pré-requisitos

- **Python 3.11+** instalado.
- **Ollama** instalado: [Baixar Ollama](https://ollama.com/).
- **Conta no Hugging Face** para baixar o modelo de embeddings.

### 2. Preparação Inicial

- Clone este repositório.
- Crie e ative um ambiente virtual:
  ```bash
  python -m venv venv
  # Windows: .\venv\Scripts\activate | Linux/macOS: source venv/bin/activate
  ```
- Instale todas as dependências:
  ```bash
  pip install -r requirements.txt
  ```

### 3. Configuração do `.env`

- Crie um arquivo `.env` na raiz do backend com as seguintes variáveis:
  ```env
  SECRET_KEY=sua_chave_secreta_para_jwt
  ALGORITHM=HS256
  ACCESS_TOKEN_EXPIRE_MINUTES=60
  DATABASE_URL=sqlite:///./meu_tcc.db (Usando o SQLite pois não precisa de configuração, é apenas pra rodar e testar o projeto, posteriormente configure o postgres.)
  ```

### 4. Configuração da Inteligência Artificial

- **Autentique-se no Hugging Face** (necessário apenas na primeira vez):
  ```bash
  python -m huggingface_hub.commands.huggingface_cli login
  # Cole seu token de acesso do Hugging Face
  ```
- **Baixe o modelo Llama 3** via Ollama:
  ```bash
  Com o PowerShell aberto, digite:
  ollama pull llama3:8b
  ```

---

## 💻 Como Rodar o Projeto

O sistema completo requer **três terminais** rodando em paralelo.

### Terminal 1: Banco de Dados

- Certifique-se de que seu servidor PostgreSQL está rodando (Se caso já estiver configurado, senão, se estiver usando SQLite, pule essa etapa).

### Terminal 2: Servidor de IA (Ollama)

- Inicie o servidor do Ollama.
  ```bash
  ollama serve
  ```
- Observação: Se precisar usar uma porta diferente da padrão (11434), defina a variável de ambiente `OLLAMA_BASE_URL` antes de executar o comando, a porta default aqui é: 11435.
- **Deixe este terminal aberto.**

### Terminal 3: Servidor do Backend (FastAPI)

- **(Apenas na primeira vez)** Inicialize o banco de dados e crie os índices da IA:
  ```bash
  # Navegue para a pasta `backend` e ative o venv
  python -m scripts.create_tables       # Cria as tabelas do PostgreSQL
  python -m scripts.create_admin        # Cria o usuário admin
  python -m scripts.create_index_pdf    # Processa o PDF e cria o banco vetorial
  ```
- **Inicie o servidor principal:**
  ```bash
  # Certifique-se que o venv está ativo
  uvicorn app.main:app --reload
  ```

### 6. Testar endpoints:

- **Autenticação:** `POST /auth/login` → retorna o token JWT do admin
- **Admin (Protegido):** `GET /admin/test` → endpoint protegido que retorna a mensagem de autenticação
- **IA (Saúde do Serviço):** `GET /ai/health`
- **IA (Fazer Pergunta):** `POST /ai/query` com um corpo JSON:
  ```json
  {
    "question": "Qual seria o objetivo do PIM?"
  }
  ```

> Para testar endpoints protegidos por JWT, recomenda-se usar **Postman** até configurarmos o Swagger para aceitar tokens.

---

## 📝 Observações

- O backend está preparado para integração com módulos da IA no futuro.
- Endpoints adicionais, base de conhecimento e funcionalidades administrativas serão adicionados conforme o projeto evolui.
- Todos os scripts e a estrutura estão organizados para que outros desenvolvedores possam entender rapidamente o funcionamento do sistema.
