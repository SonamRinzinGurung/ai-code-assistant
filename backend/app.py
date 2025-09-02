from fastapi import FastAPI
from routers import explain

app = FastAPI(title="AI Code Buddy")

app.include_router(explain.router, prefix="/api", tags=["explain"])

@app.get("/")
def root():
    return {"message": "Welcome to AI Code Buddy!"}
