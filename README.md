# Semantic Document Intelligence Platform

AI-powered document intelligence system using FastAPI and Retrieval-Augmented Generation (RAG).

## Features

- Upload PDF documents
- Automatic document chunking
- SentenceTransformer embeddings
- FAISS vector database
- Semantic search
- LLM-powered question answering
- REST APIs using FastAPI

## Technologies

- Python
- FastAPI
- LangChain
- FAISS
- Sentence Transformers
- Ollama (Llama 3)
- Postman

## Installation

```bash
git clone https://github.com/yourusername/semantic-document-intelligence.git
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run

```bash
python run.py
```

Open

```
http://localhost:8000/docs
```

## API Endpoints

### Upload PDF

```
POST /upload
```

### Ask Question

```
GET /ask?question=What is the document about?
```
