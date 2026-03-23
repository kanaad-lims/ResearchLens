from retrieval.arxiv_fetch import fetch_papers
from retrieval.preprocess import preprocess_paper
from retrieval.hybrid_search import hybrid_search
from LLM.query_llm import enhance_query

query = "Quantum Computing for optimization problems between 2023 and 2025"

# 0. Enhance the user query using groq LLM.
query = enhance_query(query)

# 1. Fetch paper from arxiv
papers = fetch_papers(query, max_results=5)

# 2. Preprocess the papers
processed = preprocess_paper(papers)

# 3. Perform hybrid search by embedding Query and paper texts
# Return top 3 papers based on the user query.
results = hybrid_search(query, processed, top_k=3)

# Results of Step 1.
for i, paper in enumerate(papers):
    print(f"\nPaper {i+1}")
    print("Title:", paper["title"])
    print("Abstract:", paper["abstract"])
    print("Link:", paper["link"])
    print("Date:", paper["date"])


for i, p in enumerate(processed):
    print(f"\nTEXT: {i+1}\n", p["text"][:200])


print("\n\nTop 3 Search Results: ")
for r in results:
    print("\nTitle:", r["title"])
    print("Date:", r["date"])
    #print("Score:", r["score"])