import uvicorn
from fastapi import FastAPI
from api.v1.endpoints.processar_documentos import processar_documentos

app = FastAPI(
    title="MTE - SEI Inteligent Extraction",
    description="Serviço Elite para processamento de ofícios e processos do SEI."
)

app.include_router(processar_documentos)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)