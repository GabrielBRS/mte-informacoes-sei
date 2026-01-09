from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# from api.v1.router import api_router
from core.config import settings
# from core.logging import setup_logging

# setup_logging()

async def lifespan(app: FastAPI):
    print(f"Iniciando {settings.PROJECT_NAME} no Python 3.13...")
    yield
    print("Encerrando sistema...")

app = FastAPI(
    title=settings.PROJECT_NAME,
    version="0.1.0",
    lifespan=lifespan,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# app.include_router(api_router, prefix=settings.API_V1_STR)

@app.get("/health", tags=["Health"])
async def health_check():
    return {
        "status": "ok",
        "project": settings.PROJECT_NAME,
        "engine": "Python 3.13"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)