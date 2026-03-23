# Testing the end to end pipeline as written in the retrieval/pipeline.py file

from retrieval.pipeline import pipeline

query = "Quantum Computing"

ranked_results = pipeline(query, max_fetch=5, top_fetch=3)

print("\n\nTop 3 Search Results: ")
for i, paper in enumerate(ranked_results):
    print(f"\nPaper {i+1}")
    print("Title:", paper["title"])
    print("Date:", paper["date"])
    print("Score:", paper["score"])