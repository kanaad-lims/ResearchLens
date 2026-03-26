from models.embedding_model import embed_model
from utils.tokenizer import tokenize
from rank_bm25 import BM25Okapi
from sklearn.metrics.pairwise import cosine_similarity
from utils.reciprocal_ranker import rrf_ranker


def hybrid_search(query, papers, top_k=5):
    """
    Performs hybrid search comprising of semantic vector search abd BM25 keyword search.
    
    Args: query (str): User query string
          papers (list): List of paper dicts with 'text' field for embedding
          top_k (int): Number of top results to return
    
    Returns: List of top_k ranked papers
    """

    # Extracting texts for embedding
    texts = [paper["text"] for paper in papers]

    """
    BM25 Keyword Search
    Tokenize paper txt and query, then calculate BM25 scores.
    """
    tokenized_corpus = [tokenize(text) for text in texts]
    bm25 = BM25Okapi(tokenized_corpus)

    tokenized_query = tokenize(query)
    bm25_scores = bm25.get_scores(tokenized_query)
    
    """
    Semantic search (Dense vector search)
    """
    query_emb = embed_model.encode([query])
    paper_emb = embed_model.encode(texts)

    # Calculating cosine similarity
    dense_scores = cosine_similarity(query_emb, paper_emb).flatten()


    """
    combine BM25 and Dense (Hybrid Search Strategy)
    used reciprocal rank fusion (rrf) for combined score.
    """
    # alpha = 0.5 # default, will change prolly.
    # final_scores = alpha * bm25_scores + (1 - alpha) * dense_scores
    final_scores = rrf_ranker(bm25_scores, dense_scores)


    # Attach scores to papers
    scored_papers = []
    for paper, score in zip(papers, final_scores):
        paper_copy = paper.copy()
        paper_copy["score"] = float(score)
        scored_papers.append(paper_copy)
    
    # Sort by score (descending)
    ranked = sorted(scored_papers, key=lambda x: x["score"], reverse=True)

    return ranked[:top_k]

