```markdown
# 📘 Assignment: Construindo APIs REST com FastAPI

## 🎯 Objective

Os estudantes vão construir uma API REST simples usando o framework FastAPI. A tarefa foca em endpoints CRUD, validação com Pydantic e execução com Uvicorn.

## 📝 Tasks

### 🛠️  Implementar API de Notas (Notes API)

#### Description
Crie uma API que permita criar, listar, atualizar e remover notas. Cada nota deve ter um `id`, `title` e `content`.

#### Requirements
Completed program should:

- Expor endpoints: `GET /notes`, `GET /notes/{id}`, `POST /notes`, `PUT /notes/{id}`, `DELETE /notes/{id}`
- Validar payloads usando modelos Pydantic
- Usar armazenamento em memória (dicionário ou lista) — persistência não é necessária
- Retornar códigos HTTP apropriados (200, 201, 404, 400)
- Incluir instruções para executar a API localmente usando Uvicorn

### 🛠️  Extensões (Opcional)

#### Description
Adicionar paginação, pesquisa por título, ou persistência simples em arquivo JSON.

#### Requirements

- Implementar pelo menos uma extensão opcional
- Documentar como testar a funcionalidade adicional

```
