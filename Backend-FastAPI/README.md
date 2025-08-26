## 🚀 API – Curso FastAPI

API desenvolvida com FastAPI. Utiliza PostgreSQL como banco de dados e Alembic para controle de migrações com base nos vídeos do bootcamp

---

### 📦 Requisitos

- Python 3.11+
- [Poetry](https://python-poetry.org/docs/)
- Docker e Docker Compose

---

### 📁 Clonar o projeto

```bash
git clone https://github.com/seu-usuario/curso_api.git
cd curso_api
```

---

### ⚙️ Instalar dependências

```bash
poetry install
```

---

### 🔐 Configurar variáveis de ambiente

Crie um arquivo `.env` na raiz com as seguintes variáveis para desenvolvimento:

```env
DB_URL=postgresql+asyncpg://admin:admin@localhost:5432/doceria
HASH_PEPPER=gY8nZkXvLzQ9eJvU5wT1mA3sKx7cQp9dZr2fGv6hT0sY
```

---

### 🐳 Subir o banco com Docker

```bash
docker compose -f postgres.yml up -d
```

Isso irá iniciar um container PostgreSQL com as configurações definidas no `postgres.yml`.

---

### 🛠️ Aplicar migrações

```bash
poetry alembic upgrade head
```

---

### 🚀 Rodar a API

```bash
poetry run task run
```

Acesse a documentação interativa: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
