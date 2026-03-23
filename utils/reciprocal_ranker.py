import numpy as np

def rrf_ranker(bm25_scores, dense_scores):
    k = 60

    bm25_ranks = np.argsort(np.argsort(-bm25_scores)) + 1
    dense_ranks = np.argsort(np.argsort(-dense_scores)) + 1

    rrf_bm25 = 1.0 / (k + bm25_ranks)
    rrf_dense = 1.0 / (k + dense_ranks)

    final_scores = rrf_bm25 + rrf_dense

    return final_scores
