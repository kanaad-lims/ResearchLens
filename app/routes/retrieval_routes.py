from fastapi import APIRouter
from fastapi import HTTPException
from app.schemas import QueryRequest, QueryResponse
from retrieval.pipeline import pipeline

router = APIRouter()

@router.post("/search", response_model=QueryResponse)
def search_papers(request: QueryRequest):

    query = request.query
    max_fetch = request.max_fetch
    top_fetch = request.top_fetch

    if top_fetch > max_fetch:
        raise HTTPException(
            status_code=400,
            detail=f"Top Fetched papers ({top_fetch}) CANNOT be greater than Maximum fetched papers ({max_fetch})."
        )

    results = pipeline(query, max_fetch, top_fetch)

    return QueryResponse(papers=results)