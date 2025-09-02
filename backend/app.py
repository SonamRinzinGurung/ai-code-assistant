from fastapi import FastAPI

app = FastAPI(title="AI Code Buddy")


@app.get("/")
def root():
    return {"message": "Welcome to AI Code Buddy!"}
