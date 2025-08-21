# Budgify - Backend

API desenvolvida em Django para gerenciamento e controle de finanças pessoais. Esta aplicação gerencia usuários, receitas, despesas, categorias e fornece endpoints RESTful para comunicação com o frontend.

---

## Funcionalidades

- Cadastro e autenticação de usuários
- Controle de receitas e despesas
- Gerenciamento de categorias financeiras
- Cálculo de saldo e relatórios básicos
- API RESTful para integração com frontend

---

## Tecnologias

- Python 3.x
- Django 4.x
- Django REST Framework
- SQLite (por padrão, pode ser alterado para PostgreSQL ou outro banco)
- Outros pacotes conforme requirements.txt

---

## Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/seu-usuario/budgify-backend.git
   cd budgify-backend
   ```

2. Crie e ative o ambiente virtual (recomendado):

   ```bash
   uv venv
   source .venv/bin/activate  # Linux/Mac
   .venv\Scripts\activate     # Windows
   ```

3. Instale as dependências:

   ```bash
   uv pip install -r requirements.txt
   ```

4. Execute as migrações:

   ```bash
   uv run manage.py migrate
   ```

5. Inicie o servidor de desenvolvimento:

   ```bash
   uv run manage.py runserver
   ```

---

## Criar novos apps

Este projeto possui um comando customizado para criar novos apps no Django:

```bash
cd bugdify
uv run ../manage.py newapp <app_name>
```

Substitua `<app_name>` pelo nome do app que deseja criar.

---