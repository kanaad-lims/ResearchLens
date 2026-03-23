from retrieval.arxiv_fetch import fetch_papers
from retrieval.preprocess import preprocess_paper
from retrieval.hybrid_search import hybrid_search
from LLM.query_llm import enhance_query
 

def pipeline(query: str, max_fetch: int, top_fetch: int):

    """
    end to end paper retrieval pipeline implementation
    test cases written in tests/test_arxiv.py
    """

    query = enhance_query(query)

    # 1. Fetching papers from the arxiv.
    try:
        papers = fetch_papers(query, max_results=max_fetch)
    except Exception as e:
        print("error fetching papers: ", e)
        return []
    
    # 2. Preprocess the papers.
    try:
        processed = preprocess_paper(papers)
    except Exception as e:
        print("Error processing papers: ", e)
        return []
    
    # 3. Using hybrid search to find most relevant papers.
    try:
        results = hybrid_search(query, processed, top_k=top_fetch)
    except Exception as e:
        print("Error performing hybrid search: ", e)
        return []

    return results