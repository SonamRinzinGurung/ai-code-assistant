from fastapi import FastAPI
from routers import explain
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="AI Code Buddy")

origins = ["http://localhost:5173"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(explain.router, prefix="/api", tags=["explain"])

@app.get("/")
def root():
    return {"message": "Welcome to AI Code Buddy!"}
