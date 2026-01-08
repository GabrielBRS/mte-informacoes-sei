from fastapi import APIRouter, UploadFile, File, BackgroundTasks
import uuid
from services.model_ai import process_pipeline

router = APIRouter()
jobs_db = {}


@router.post("/processar-documento")
async def start_processing(background_tasks: BackgroundTasks, file: UploadFile = File(...)):
    job_id = str(uuid.uuid4())
    content = await file.read()

    jobs_db[job_id] = {"status": "recebido", "arquivo": file.filename}

    background_tasks.add_task(process_pipeline, job_id, content, jobs_db)

    return {"job_id": job_id, "status": "processando"}


@router.get("/status/{job_id}")
async def check_status(job_id: str):
    return jobs_db.get(job_id, {"erro": "Job não encontrado"})