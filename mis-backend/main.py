# FastAPI app entry point, registers all routes
from fastapi import FastAPI
from routers import auth, users, projects, participation, exhibition, reports

app = FastAPI(title="MIS Platform", version="1.0.0")

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(projects.router)
app.include_router(participation.router)
app.include_router(exhibition.router)
app.include_router(reports.router)

@app.get('/health')
async def health(): return {'status': 'ok', 'app': 'MIS Platform'}