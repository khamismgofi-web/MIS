# FastAPI app entry point, registers all routes
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import auth_api, users_api, projects_api, participation_api, reports_api
from routers import exhibition

app = FastAPI(title="MIS Platform", version="1.0.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(auth_api.router)
app.include_router(users_api.router)
app.include_router(projects_api.router)
app.include_router(participation_api.router)
app.include_router(exhibition.router)
app.include_router(reports_api.router)

@app.post("/login")
@app.get('/health')
async def health(): return {'status': 'ok', 'app': 'MIS Platform'}

