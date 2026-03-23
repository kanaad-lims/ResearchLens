from pydantic import BaseModel
from typing import List

# 1. Schema for query request
class QueryRequest(BaseModel):
    query: str
    max_fetch: int
    top_fetch: int

# 2. Schema for Paper metadata
class PaperMetadata(BaseModel):
    title: str
    abstract: str
    date: str
    link: str
    #score: float

# 3. Schema for query response
class QueryResponse(BaseModel):
    papers: List[PaperMetadata]