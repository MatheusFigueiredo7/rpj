# API - Gerenciamento de Processos Jurídicos

API REST desenvolvida em Django para gerenciar processos jurídicos e os advogados responsáveis por eles. O sistema permite cadastrar advogados, vincular processos e realizar filtros avançados.

## Tecnologias utilizadas
- Python 3.12
- Django
- PostgreSQL
- Docker

## Como executar localmente

1. Clone este repositório no seu computador.
2. Certifique-se de ter o Docker Desktop instalado e rodando.
3. No terminal, na raiz do projeto, execute o comando para subir os contêineres:
   ```bash
   docker compose up --build
A API estará disponível em http://127.0.0.1:8000/.

## Endpoints Principais

## Advogados

GET /api/advogados/ : Lista todos os advogados.

POST /api/advogados/ : Cria um novo advogado.

GET /api/advogados/<id>/ : Retorna um advogado específico pelo ID.

GET /api/advogados/ativos/ : Lista apenas os advogados ativos.

## Processos

GET /api/processos/ : Lista todos os processos.

POST /api/processos/ : Cria um novo processo vinculado a um advogado.

PUT /api/processos/<id>/atualizar/ : Atualiza um processo existente.

DELETE /api/processos/<id>/remover/ : Remove um processo.

GET /api/processos/<id>/ : Retorna um processo específico pelo ID.

GET /api/processos/advogado/<advogado_id>/ : Lista todos os processos de um advogado específico.

GET /api/processos/status/<status>/ : Filtra processos por status (ex: ABERTO, CONCLUIDO).

GET /api/processos/prioridade/<prioridade>/ : Filtra processos por prioridade (ex: URGENTE).
