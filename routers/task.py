from fastapi import APIRouter, HTTPException
from models.task import Task, TaskInDB
from controllers import task as task_controller

router = APIRouter()

@router.post("/tasks", response_model=dict)
async def create(task: Task):
    task_id = await task_controller.create_task(task.dict())
    return {"id": task_id}

@router.get("/tasks/{task_id}", response_model=TaskInDB)
async def read(task_id: str):
    task = await task_controller.get_task(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.delete("/tasks/{task_id}", response_model=dict)
async def delete(task_id: str):
    deleted_count = await task_controller.delete_task(task_id)
    if deleted_count == 0:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"deleted": deleted_count}
