"""
FAISS indexer skeleton. Wraps index creation, save/load and search.
"""
import faiss
import numpy as np
from pathlib import Path

class Indexer:
    def __init__(self, dim=512, index_path: str | None = None):
        self.dim = dim
        self.index_path = index_path
        self.index = faiss.IndexFlatIP(dim)  # cosine w/ normalized vectors
        self.ids = []  # store ids array in memory for demo; save to disk in production

    def add(self, vectors: np.ndarray, ids: list[str]):
        # normalize for cosine similarity
        faiss.normalize_L2(vectors)
        self.index.add(vectors)
        self.ids.extend(ids)

    def search(self, query_vectors: np.ndarray, top_k: int = 10):
        faiss.normalize_L2(query_vectors)
        scores, idxs = self.index.search(query_vectors, top_k)
        results = []
        for row_idx in range(len(query_vectors)):
            row = []
            for i, idx in enumerate(idxs[row_idx]):
                if idx == -1:
                    continue
                row.append((self.ids[idx], float(scores[row_idx][i])))
            results.append(row)
        return results

    def save(self, path: str):
        Path(path).parent.mkdir(parents=True, exist_ok=True)
        faiss.write_index(self.index, path + ".faiss")
        # save ids separately (json/csv)

    def load(self, path: str):
        self.index = faiss.read_index(path + ".faiss")
        # load ids separately