def preprocess_paper(papers):
    """
    Combinig the title and abstract into single text field.

    Args: (papers) List of dicts with keys - title, abstract, link, date.

    Returns: List of dicts with keys - title, abstract, text, link, date.
    """

    preprocessed = []
    for paper in papers:
        text = (paper["title"] + " " + paper["abstract"]).strip()
        preprocessed.append({
            "title": paper["title"],
            "abstract": paper["abstract"],
            "text": text,
            "link": paper["link"],
            "date": paper["date"]
        })
    return preprocessed

