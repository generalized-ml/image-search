# Semantic Image Search

A powerful semantic image search application that allows you to search for images using natural language queries. The application uses CLIP (Contrastive Language-Image Pre-training) to generate embeddings and perform semantic similarity search.

## Features

- 🔍 Semantic search: Search images using natural language descriptions
- 🖼️ Support for multiple image formats (JPG, PNG, JPEG, BMP, GIF)
- ⚡ Fast vector similarity search using FAISS
- 🌐 REST API for integration
- 💻 Web-based user interface
- 📊 Batch image processing and indexing

## Project Structure

```
image-search/
├── backend/
│   ├── api/
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   └── schemas.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py
│   │   ├── embeddings.py
│   │   └── search.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── image_processor.py
│   │   └── indexer.py
│   ├── utils/
│   │   ├── __init__.py
│   │   └── helpers.py
│   ├── __init__.py
│   └── main.py
├── frontend/
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css
│   │   └── js/
│   │       └── app.js
│   ├── templates/
│   │   └── index.html
│   └── __init__.py
├── data/
│   ├── images/
│   │   └── .gitkeep
│   └── index/
│       └── .gitkeep
├── tests/
│   ├── __init__.py
│   ├── test_embeddings.py
│   ├── test_search.py
│   └── test_api.py
├── notebooks/
│   └── explore_embeddings.ipynb
├── scripts/
│   ├── index_images.py
│   └── setup_demo.py
├── .env.example
├── .gitignore
├── requirements.txt
├── setup.py
└── README.md
```

## Installation

### Prerequisites

- Python 3.8+
- pip
- Virtual environment (recommended)

### Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd image-search
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure environment variables:
```bash
cp .env.example .env
# Edit .env with your settings
```

5. Index your images:
```bash
python scripts/index_images.py --image-dir data/images
```

## Usage

### Starting the Server

```bash
python backend/main.py
```

The server will start at `http://localhost:8000`

### API Endpoints

- `GET /`: Web interface
- `POST /api/search`: Search images by text query
- `POST /api/index`: Index new images
- `GET /api/health`: Health check

### Example Search Request

```bash
curl -X POST "http://localhost:8000/api/search" \
  -H "Content-Type: application/json" \
  -d '{"query": "a dog playing in the park", "top_k": 5}'
```

## Development

### Running Tests

```bash
pytest tests/
```

### Code Style

```bash
black backend/ frontend/ tests/
flake8 backend/ frontend/ tests/
```

## Technologies Used

- **CLIP**: OpenAI's vision-language model for embeddings
- **FAISS**: Facebook AI Similarity Search for fast vector search
- **FastAPI**: Modern web framework for building APIs
- **PyTorch**: Deep learning framework
- **Pillow**: Image processing library

## Configuration

Edit `.env` file to configure:

- `IMAGE_DIR`: Directory containing images to search
- `INDEX_DIR`: Directory to store index files
- `MODEL_NAME`: CLIP model to use (default: ViT-B/32)
- `DEVICE`: CPU or CUDA
- `TOP_K`: Default number of results to return

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT License

## Acknowledgments

- OpenAI CLIP model
- Facebook AI Similarity Search (FAISS)
