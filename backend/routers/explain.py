from fastapi import APIRouter
from models.schemas import CodeSnippet
from services.inference import explain_code

router = APIRouter()


@router.post("/explain")
def explain(snippet: CodeSnippet):
    return {"explanation": explain_code(snippet.code)}
