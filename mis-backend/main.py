# FastAPI app entry point, registers all routes
from fastapi import FastAPI
from app.routers import auth, users, projects, participations, exhibitions, reports

app = FastAPI(title="MIS Platform", version="1.0.0")

app.include_router(auth.router,            prefix="/api/v1")
app.include_router(users.router,           prefix="/api/v1")
app.include_router(projects.router,        prefix="/api/v1")
app.include_router(participations.router,  prefix="/api/v1")
app.include_router(exhibitions.router,     prefix="/api/v1")
app.include_router(reports.router,         prefix="/api/v1")

@app.get('/health')
async def health(): return {'status': 'ok', 'app': 'MIS Platform'}