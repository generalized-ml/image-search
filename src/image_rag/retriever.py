"""
Retriever skeleton that ties embedder + indexer + metadata lookup.
"""
from typing import List, Dict
from .embedder import Embedder
from .indexer import Indexer

class Retriever:
    def __init__(self):
        # lazy initialization
        self.embedder = Embedder()
        self.indexer = Indexer(dim=512)
        # metadata store: id -> metadata
        self.metadata = {}

    def load_index(self, path: str):
        self.indexer.load(path)

    def search(self, query: str, top_k: int = 5) -> List[Dict]:
        q_vec = self.embedder.embed_text([query])
        raw = self.indexer.search(q_vec, top_k)
        items = []
        for (img_id, score) in raw[0]:
            items.append({
                "image_id": img_id,
                "score": score,
                "metadata": self.metadata.get(img_id, {})
            })
        return items