# FastAPI app entry point, registers all routes
from fastapi import FastAPI
from app.api import auth_api, users_api, projects_api, participation_api, reports_api
from routers import exhibition

app = FastAPI(title="MIS Platform", version="1.0.0")

app.include_router(auth_api.router)
app.include_router(users_api.router)
app.include_router(projects_api.router)
app.include_router(participation_api.router)
app.include_router(exhibition.router)
app.include_router(reports_api.router)

@app.get('/health')
async def health(): return {'status': 'ok', 'app': 'MIS Platform'}