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

O **backend** atual foca na autenticação do usuário **admin**, responsável por cadastrar informações que a IA utilizará para treinamento e consultas.

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

---

## 🗂️ Scripts Úteis

- `scripts/init_db.py` → Cria todas as tabelas no banco de dados. Deve ser executado uma vez antes de rodar a aplicação.  
- `scripts/create_admin_user.py` → Cria o usuário admin inicial para login. Deve ser executado após `init_db.py`.

---

## ⚙️ Configuração do .env

Crie um arquivo **.env** na raiz do backend com as seguintes variáveis:

```
SECRET_KEY=sua_chave_secreta
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
DATABASE_URL=postgresql://usuario:senha@localhost:5432/nome_do_banco
```

- **SECRET_KEY** → chave secreta para gerar JWT  
- **ALGORITHM** → algoritmo de criptografia do JWT (ex: HS256)  
- **ACCESS_TOKEN_EXPIRE_MINUTES** → tempo de expiração do token  
- **DATABASE_URL** → URL de conexão com o banco PostgreSQL  

---

## 💻 Como Rodar o Projeto

### 1. Criar e ativar o ambiente virtual:

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

### 2. Instalar dependências:

```bash
pip install -r requirements.txt
```

### 3. Inicializar o banco e criar o admin:

```bash
python scripts/init_db.py
python scripts/create_admin_user.py
```

### 4. Rodar o backend:

```bash
uvicorn main:app --reload
```

### 5. Testar endpoints:

- `POST /auth/login` → retorna o token JWT do admin  
- `GET /admin/test` → endpoint protegido que retorna a mensagem de autenticação  

> Para testar endpoints protegidos por JWT, recomenda-se usar **Postman** até configurarmos o Swagger para aceitar tokens.

---

## 📝 Observações

- O backend está preparado para integração com módulos da IA no futuro.  
- Endpoints adicionais, base de conhecimento e funcionalidades administrativas serão adicionados conforme o projeto evolui.  
- Todos os scripts e a estrutura estão organizados para que outros desenvolvedores possam entender rapidamente o funcionamento do sistema.  
