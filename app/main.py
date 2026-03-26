from fastapi import FastAPI
from app.routes.retrieval_routes import router
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="AI Research Assistant")

# Download the nltk stopwords required for tokenizer in BM25.
# One time download, then ignores.
nltk.download('stopwords', quiet=True)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="frontend"), name="static")

@app.get("/")
def home():
    return FileResponse("frontend/index.html")

app.include_router(router)
