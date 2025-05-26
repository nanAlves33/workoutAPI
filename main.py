from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="Workout API")
app.include_router(router)