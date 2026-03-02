from fastapi import FastAPI
from app.api import routes

app = FastAPI(title="Stock Reposición API")

app.include_router(routes.router)

@app.get("/health")
def health_check():
    return {"status": "ok"}