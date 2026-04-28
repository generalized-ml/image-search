# Image-Search (Learning Project)

Objective
- Build a small image-search system using Retrieval-Augmented Generation (RAG) ideas: given a text query, retrieve relevant images and optionally produce a short text justification/summary. This repo is structured for learning and rapid prototyping over 2 months.

Contents
- `src/image_rag` — application code
- `notebooks` — experiments and walkthroughs
- `data` — raw and processed images and metadata
- `scripts` — helpers to prepare data and build index
- `examples` — simple demo clients
- `docs` — architecture and API notes

Quickstart (local)
1. Create virtualenv:
   python -m venv .venv && source .venv/bin/activate
2. Install:
   pip install -r requirements.txt
3. Prepare sample data (put images in `data/raw/`), then:
   python scripts/prepare_data.py --input data/raw --out data/processed
4. Build index:
   python scripts/build_index.py --data data/processed --index_path data/index/faiss.index
5. Run API:
   uvicorn image_rag.app:app --reload --host 0.0.0.0 --port 8000
6. Query:
   python examples/demo_query.py "a red sports car"

What this repo includes (starter)
- Minimal FastAPI server with a `/search` endpoint that accepts a text query and returns top-k image references.
- Skeletons for embedder (CLIP), indexer (FAISS), retriever and ranker modules.
- Notebooks for step-by-step learning.

Tech stack suggestion
- Python 3.10+
- PyTorch + OpenAI/CLIP or Hugging Face Transformers for image/text embeddings
- sentence-transformers for text embeddings (or CLIP text encoder)
- faiss-cpu for vector index
- FastAPI + Uvicorn for a lightweight API
- Docker for reproducible runtime

2-Month Learning Plan (weekly)
- Week 1: Environment + basic Python + dataset collection. Get familiar with CLIP and simple embedding extraction.
- Week 2: Implement embedder for images and text. Run small embeddings on sample images.
- Week 3: Learn FAISS and build a toy index. Do nearest-neighbour queries.
- Week 4: Implement retriever + run end-to-end search locally. Basic API endpoint.
- Week 5: Add ranking/filtering (e.g., metadata, cosine similarity thresholds). Notebook for evaluation metrics.
- Week 6: Integrate simple RAG-style generator (optional: small LLM or template summarizer) to produce explanations.
- Week 7: Tests, packaging, Dockerize, CI basics.
- Week 8: Polish, final demo, documentation, and prepare a short presentation.

Milestones & Deliverables
- End of Week 4: working local API that returns relevant images for a query
- End of Week 6: RAG-style responses with explanation text
- End of Week 8: Docker image, tests, and documentation

How to contribute
- See CONTRIBUTING.md for coding style, tests, and PR process.

License
- MIT