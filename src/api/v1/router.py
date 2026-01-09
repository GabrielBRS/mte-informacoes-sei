# src/api/v1/router.py
from fastapi import APIRouter
from api.v1.controllers import processar_documentos

api_router = APIRouter()
api_router.include_router(processar_documentos.router, tags=["Documentos"])
# api_router.include_router(usuarios.router, tags=["Usuários"])
# ... aqui você pode ter 1000 módulos sem poluir o main