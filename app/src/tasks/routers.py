from fastapi import APIRouter
from fastapi.responses import JSONResponse
from celery.result import AsyncResult
from ..core.worker import celery
from ..core.worker import get_ip_info

router_task = APIRouter(
    prefix="/api/v1/tasks",
    tags=["tasks"]
)

@router_task.get("", summary="Get Task ID regarding to IP info task", status_code=201)
async def get_ip_info_task(ip: str):
    task = get_ip_info.delay(ip)
    print(task)
    return JSONResponse({
        "task_id": task.id,
    })

@router_task.get("/status/{task_id}")
def get_status(task_id):
    task = AsyncResult(task_id, app=celery)
    return JSONResponse({
        "task_id": task.id,
        "task_status": task.status,
        "task_result": task.result
    })
