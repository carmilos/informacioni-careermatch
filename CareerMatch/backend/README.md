# CareerMatch Backend (FastAPI)

Basic FastAPI backend for CareerMatch: JWT auth, Postgres (SQLAlchemy), CV upload handling.

Install (create venv) and run:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

Run Postgres with docker-compose:

```bash
docker compose up -d
```

Start the API:

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Notes:
- Environment is read from `.env` in this folder. Adjust `DATABASE_URL` when not using docker-compose.
- The Angular frontend is expected to call endpoints at `http://localhost:8000`.
