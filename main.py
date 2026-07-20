from fastapi import FastAPI, UploadFile, File

from app.utils import save_file
from app.config import UPLOAD_FOLDER

from app.rag import process_document
from app.rag import ask_question

app = FastAPI(
    title="Semantic Document Intelligence Platform"
)

@app.get("/")
def home():
    return {
        "message":"Semantic Document Intelligence Platform"
    }


@app.post("/upload")

async def upload(file: UploadFile = File(...)):

    filepath = save_file(file, UPLOAD_FOLDER)

    process_document(filepath)

    return {
        "status":"Document Indexed"
    }


@app.get("/ask")

def ask(question:str):

    answer = ask_question(question)

    return {
        "question":question,
        "answer":answer
    }
