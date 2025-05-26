# Workout API - Projeto Exemplo

Este projeto é uma API básica em FastAPI com SQLAlchemy para cadastro e atualização de produtos.

Funcionalidades implementadas:
- Criar produto (tratamento de exceções)
- Atualizar produto (PATCH) com tratamento de Not Found
- Filtro por preço usando query params

Para rodar:
1. Ative seu ambiente virtual (Pyenv + Poetry recomendado)
2. Instale dependências: `poetry install`
3. Rode a aplicação: `poetry run uvicorn app.main:app --reload`