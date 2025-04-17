from fastapi import FastAPI
from routers import task
import uvicorn

app = FastAPI()

app.include_router(task.router)

@app.on_event("startup")
async def startup_db():
    from config.database import ping_db
    await ping_db()

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
