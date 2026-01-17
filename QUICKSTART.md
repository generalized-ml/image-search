# Quick Start Guide

## Project Structure Overview

Your semantic image search repository is now set up with the following structure:

```
image-search/
├── .github/
│   └── copilot-instructions.md    # GitHub Copilot instructions
├── backend/                         # Core application backend
│   ├── api/                        # REST API endpoints
│   │   ├── routes.py              # API route handlers
│   │   └── schemas.py             # Pydantic request/response models
│   ├── core/                       # Core functionality
│   │   ├── config.py              # Configuration management
│   │   ├── embeddings.py          # CLIP embedding generation
│   │   └── search.py              # FAISS vector search
│   ├── services/                   # Business logic
│   │   ├── image_processor.py     # Image handling and validation
│   │   └── indexer.py             # Image indexing service
│   ├── utils/                      # Utility functions
│   │   └── helpers.py             # Helper functions
│   └── main.py                     # FastAPI application entry point
├── frontend/                        # Web interface
│   ├── static/
│   │   ├── css/style.css          # Styling
│   │   └── js/app.js              # JavaScript functionality
│   └── templates/
│       └── index.html             # Main HTML page
├── data/
│   ├── images/                     # Place your images here
│   └── index/                      # Search index storage
├── tests/                          # Unit tests
│   ├── test_embeddings.py
│   ├── test_search.py
│   └── test_api.py
├── notebooks/
│   └── explore_embeddings.ipynb   # Jupyter notebook for exploration
├── scripts/
│   ├── index_images.py            # CLI script to index images
│   └── setup_demo.py              # Demo setup script
├── .env.example                    # Environment variables template
├── .gitignore
├── requirements.txt                # Python dependencies
├── setup.py                        # Package setup
└── README.md                       # Main documentation
```

## Getting Started

### 1. Set Up Environment

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On macOS/Linux

# Install dependencies
pip install -r requirements.txt
```

### 2. Configure Settings

```bash
# Copy environment template
cp .env.example .env

# Edit .env if needed (default settings work for most cases)
```

### 3. Add Your Images

```bash
# Place images in the data/images directory
cp /path/to/your/images/* data/images/
```

### 4. Index Your Images

```bash
# Run the indexing script
python scripts/index_images.py --image-dir data/images
```

### 5. Start the Server

```bash
# Start the FastAPI server
python backend/main.py

# Server will start at http://localhost:8000
```

### 6. Use the Web Interface

Open your browser and navigate to: `http://localhost:8000`

- Enter natural language queries (e.g., "a sunset over mountains")
- Adjust the number of results and similarity threshold
- Click "Search" to find matching images

## Using the API

### Search Endpoint

```bash
curl -X POST "http://localhost:8000/api/search" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "a dog playing in the park",
    "top_k": 10,
    "threshold": 0.3
  }'
```

### Index Endpoint

```bash
curl -X POST "http://localhost:8000/api/index" \
  -H "Content-Type: application/json" \
  -d '{
    "directory": "data/images",
    "rebuild": false
  }'
```

### Health Check

```bash
curl "http://localhost:8000/api/health"
```

## Running Tests

```bash
# Run all tests
pytest tests/

# Run specific test file
pytest tests/test_embeddings.py

# Run with coverage
pytest --cov=backend tests/
```

## Using the Jupyter Notebook

```bash
# Start Jupyter
jupyter notebook notebooks/explore_embeddings.ipynb
```

The notebook includes:
- CLIP model exploration
- Embedding visualization
- Similarity analysis
- Search demonstrations

## Key Features

### 1. **Semantic Search**
- Uses CLIP (Contrastive Language-Image Pre-training) for embeddings
- Understands natural language queries
- Finds semantically similar images

### 2. **Fast Vector Search**
- FAISS (Facebook AI Similarity Search) for efficient similarity search
- Handles large image collections
- Normalized cosine similarity scoring

### 3. **Web Interface**
- Clean, modern UI
- Real-time search
- Index management
- Result visualization

### 4. **REST API**
- FastAPI framework
- Interactive documentation at `/docs`
- JSON request/response format

## Customization

### Change the Model

Edit `.env` file:
```bash
MODEL_NAME=ViT-L/14  # Use larger model for better accuracy
```

### Adjust Search Parameters

Edit `.env` file:
```bash
TOP_K=20                    # Return more results
SIMILARITY_THRESHOLD=0.5    # Higher threshold = stricter matches
```

### Enable GPU

Edit `.env` file:
```bash
DEVICE=cuda  # Use GPU if available
```

## Troubleshooting

### Issue: No images found
- Check that images are in `data/images/`
- Verify image formats (jpg, png, etc.)
- Check file permissions

### Issue: Search returns no results
- Lower the similarity threshold
- Rebuild the index
- Verify index was created successfully

### Issue: Out of memory
- Reduce batch size in `.env`
- Use smaller model (ViT-B/32 instead of ViT-L/14)
- Process images in smaller batches

## Next Steps

1. **Add your own images** to `data/images/`
2. **Run indexing** to build the search index
3. **Test searches** with various queries
4. **Explore the notebook** to understand embeddings
5. **Customize** the UI or API as needed

## Resources

- [CLIP Paper](https://arxiv.org/abs/2103.00020)
- [FAISS Documentation](https://github.com/facebookresearch/faiss)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)

---

**Need help?** Check [README.md](README.md) for detailed documentation.
