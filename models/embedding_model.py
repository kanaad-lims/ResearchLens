
"""
This function embeds the paper metadata and text using All-MiniLM-L6-v2 model
Used in hybrid_search.py for embedding logic.
"""

from sentence_transformers import SentenceTransformer

embed_model = SentenceTransformer('all-MiniLM-L6-v2')