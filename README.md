# ResearchLens

<p align="center">
  <img src="https://img.shields.io/badge/FastAPI-0.115.0-009688?style=for-the-badge&logo=fastapi&logoColor=white" />
  <img src="https://img.shields.io/badge/Groq-Llama_3.3_70B-F55036?style=for-the-badge" />
  <img src="https://img.shields.io/badge/SentenceTransformers-3.1.1-FFB300?style=for-the-badge" />
  <img src="https://img.shields.io/badge/arXiv-API-B31B1B?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/License-Apache_2.0-blue?style=for-the-badge" />
  <br>
  <img src="https://img.shields.io/github/stars/kanaad-lims/ResearchLens?style=for-the-badge" />
  <img src="https://img.shields.io/github/forks/kanaad-lims/ResearchLens?style=for-the-badge" />
</p>

> AI-powered academic paper discovery — search arXiv using natural language and get the most relevant research papers ranked by a hybrid retrieval engine.

---

</p>
<p align="center">
<img src="https://github.com/kanaad-lims/ResearchLens/blob/b6a925477eb423323b10e26aeee11faace229de9/researchlens_logo-removebg-preview.png" 
       alt="ResearchLens flowchart" width="300">
</p>

## What is ResearchLens?

ResearchLens is a backend-first research assistant that lets users search for academic papers using plain, conversational language. Instead of crafting precise arXiv queries, users can say things like *"get me papers on reinforcement learning for warehouse robotics"* or *"how is AI being used in hospitals"* — and get back highly relevant, ranked research papers.

Under the hood, an LLM expands the user's casual query into rich technical keywords, which are then used to fetch and rank papers from arXiv using a hybrid search engine combining BM25 and dense semantic search.

<p align="center">
  <video src=""
         width="720"
         controls
         muted>
  </video>
</p>


---

## Features

- **Conversational search** — no need to know arXiv query syntax
- **LLM query enhancement** — expands casual queries into technical keywords using Groq (Llama 3.3 70B)
- **Hybrid retrieval** — combines BM25 keyword search + dense semantic search via `all-MiniLM-L6-v2`
- **Reciprocal Rank Fusion** — merges BM25 and semantic rankings into a single score
- **Clean REST API** — FastAPI backend with Pydantic schemas
- **Frontend UI** — minimal dark-theme HTML/JS interface, no framework needed

---

## Project Structure

```
ResearchLens/
│
├── app/                        # FastAPI application
│   ├── main.py                 # App entry point, middleware
│   ├── config.py               # Environment config
│   ├── schemas.py              # Pydantic request/response models
│   └── routes/
│       └── retrieval_routes.py # /search endpoint
│
├── LLM/
│   └── query_llm.py            # Groq LLM query enhancement
│
├── retrieval/
│   ├── pipeline.py             # End-to-end retrieval pipeline
│   ├── arxiv_fetch.py          # arXiv paper fetching
│   ├── preprocess.py           # Title + abstract merging
│   ├── hybrid_search.py        # BM25 + semantic search
│
├── models/
│   └── embedding_model.py      # all-MiniLM-L6-v2 embedding model
│
├── utils/
│   ├── tokenizer.py            # Text tokenizer for BM25
│   └── reciprocal_ranker.py    # Reciprocal Rank Fusion (RRF)
│
├── frontend/
│   └── index.html              # UI (served via FastAPI static files)
│
├── tests/
│   ├── pipeline_test.py
│   ├── llm_call_test.py
│   ├── test_arxiv.py
│   └── embedding_model_test.py
│
├── .gitignore
└── README.md
```

---

## How It Works

</p>
<p align="center">
<img src="https://github.com/kanaad-lims/ResearchLens/blob/3130d5cf97aef922db040e8ec2d136ee644d0645/researchlens_flowchart.png" 
       alt="ResearchLens flowchart" width="700" height=700>
</p>

---

## API Reference

### `POST /search`

Search for research papers using natural language.

**Request Body:**
```json
{
  "query": "Papers on deep reinforcement learning for self-driving cars",
  "max_fetch": 20,
  "top_fetch": 5
}
```

| Field | Type | Description |
|-------|------|-------------|
| `query` | `string` | Natural language or technical search query |
| `max_fetch` | `int` | Number of papers to fetch from arXiv |
| `top_fetch` | `int` | Number of top papers to return after reranking. Must be ≤ `max_fetch` |

**Response:**
```json
{
  "papers": [
    {
      "title": "Multi-Agent Connected Autonomous Driving using Deep Reinforcement Learning",
      "abstract": "The capability to learn and adapt to changes in the driving environment...",
      "date": "2019-11-11",
      "link": "http://arxiv.org/abs/1911.04175v1"
    },
]
}
```

---

## Tech Stack

| Layer | Technology |
|-------|------------|
| API Framework | FastAPI |
| LLM | Groq API — Llama 3.3 70B Versatile |
| Embeddings | `sentence-transformers/all-MiniLM-L6-v2` |
| Keyword Search | BM25 (`rank-bm25`) |
| Semantic Search | Cosine similarity (`scikit-learn`) |
| Rank Fusion | Reciprocal Rank Fusion (RRF) |
| Paper Source | arXiv API (`arxiv` Python library) |
| Frontend | Vanilla HTML + CSS + JS |

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/kanaad-lims/ResearchLens.git
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows
```
```bash
# Anaconda environment creation
conda create --name venv
conda activate venv
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

Create a `.env` file in the root directory:

```env
GROQ_API_KEY=your_groq_api_key_here
```

### 5. Run the server

```bash
uvicorn app.main:app --reload
```

### 6. Open the UI

Navigate to `http://127.0.0.1:8000` in your browser.

Or test the API directly at `http://127.0.0.1:8000/docs` (Swagger UI).

---

## Usage Examples

**Conversational queries work:**
```
"I want to learn how AI is being used in hospitals"
"something about making LLMs faster and cheaper"
"papers on Alzheimer's detection using brain scans"
```

**Technical queries also work:**
```
"transformer architecture optimization"
"quantum computing QAOA combinatorial optimization"
"diffusion models image synthesis 2024"
```

---

## Configuration

| Parameter | Recommended Range | Notes |
|-----------|------------------|-------|
| `max_fetch` | 10 – 25 | Keep low during dev to avoid arXiv rate limits |
| `top_fetch` | 3 – 10 | Must be ≤ `max_fetch` |

> **Note on arXiv rate limits:** arXiv enforces a soft limit of ~1 request per 3 seconds. Avoid sending rapid consecutive requests during development. The arXiv client is configured with `delay_seconds=3` and `num_retries=3` to handle this automatically.

---

## Running Tests

```bash
pytest tests/
```

---

## Known Limitations

- arXiv API can return HTTP 429 (rate limit) under rapid consecutive requests — space out your queries during testing
- `all-MiniLM-L6-v2` is downloaded on first run (~100MB) — expect a slight delay on cold start
- Embeddings are computed fresh per request — no caching implemented yet (planned)
- Paper results depend on arXiv's own relevance ranking at the fetch stage

---

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you'd like to change.

---

## License

[MIT](LICENSE)
