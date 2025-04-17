from config.database import db
from bson.objectid import ObjectId

collection = db["tasks"]

async def create_task(task: dict):
    result = await collection.insert_one(task)
    return str(result.inserted_id)

async def get_task(task_id: str):
    task = await collection.find_one({"_id": ObjectId(task_id)})
    if task:
        task["_id"] = str(task["_id"])
    return task

async def delete_task(task_id: str):
    result = await collection.delete_one({"_id": ObjectId(task_id)})
    return result.deleted_count