import arxiv

def fetch_papers(query: str, max_results: int):
    """
    Fetch papers from arXiv based on query.

    Returns:
        List[dict]: Each dict contains title, abstract, link
    """
    try:
        search = arxiv.Search(
            query=query,
            max_results=max_results,
            sort_by=arxiv.SortCriterion.Relevance
        )

        papers = []

        for result in search.results():
            paper = {
                "title": result.title.strip(),
                "abstract": result.summary.strip(),
                "link": result.entry_id,
                "date": result.published.strftime("%Y-%m-%d")
            }
            papers.append(paper)

        return papers

    except Exception as e:
        print(f"[ERROR] arXiv fetch failed: {e}")
        return []