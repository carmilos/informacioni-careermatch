# CareerMatch

Quick start instructions to set up and run CareerMatch on a fresh Windows development machine after cloning the repository.

Prerequisites
- Git
- Node.js (16+ recommended) and npm
- Python 3.9+ and pip
- Docker Desktop (running)

High-level services
- Backend: FastAPI (Python) — serves API on http://localhost:8000
- Frontend: Angular — serves UI on http://localhost:4200
- Database: PostgreSQL (via Docker Compose)

1) Clone the repo

```powershell
git clone <repo_url>
cd CareerMatch
```

2) Start PostgreSQL with Docker

Make sure Docker Desktop is running, then from the project root:

```powershell
docker compose up -d
```

This will start a Postgres container configured for the app and expose port 5432 on localhost.

3) Backend setup

```powershell
cd backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1   # PowerShell
pip install --upgrade pip
pip install -r requirements.txt
```

Create or review `.env` in `backend/` — example values:

```
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/careermatch
SECRET_KEY=change-me-to-a-random-string
ACCESS_TOKEN_EXPIRE_MINUTES=60
```

If you change the DB host/port or credentials, update `DATABASE_URL` accordingly.

Start the backend (development):

```powershell
# from repo root
.\.venv\Scripts\python.exe -m uvicorn backend.app.main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at `http://localhost:8000`. On first run the app will create tables in the database.

Optional: run the smoke test (after backend is up):

```powershell
cd backend
.\.venv\Scripts\python.exe smoke_test.py
```

4) Frontend setup

Open a new terminal and run:

```powershell
cd frontend
npm install
# if you get errors about missing dev builders, install them:
# npm install --save-dev @angular-devkit/build-angular @angular/cli @angular/compiler-cli
npm run start
```

If `npm run start` is not configured, run:

```powershell
npx ng serve --host 0.0.0.0 --port 4200
```

Open `http://localhost:4200` in your browser.

5) Typical workflow
- Ensure Docker Desktop is running and Postgres container is up
- Start backend (uvicorn)
- Start frontend (ng serve)

6) Notes and troubleshooting
- If the backend cannot connect to Postgres, confirm `docker compose ps` shows the postgres service and that port 5432 is available on localhost. On Windows, Docker Desktop must be running.
- If you see Angular errors about builders, run the dev-deps install command shown above from the `frontend` folder.
- JWT tokens are stored in browser `localStorage` under key `token`.
- Uploaded CVs are saved to `backend/uploads` and served by the backend under `/uploads/`.

7) Further improvements
- Add `.env.example` with sample variables
- Add scripts to automate virtualenv creation and start commands

If you want, I can also add a `.env.example` and npm scripts to the frontend and backend to simplify startup.
