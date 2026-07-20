from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

from langchain_community.vectorstores import FAISS

from langchain_community.embeddings import SentenceTransformerEmbeddings

from langchain_community.llms import Ollama

embedding = SentenceTransformerEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

llm = Ollama(model="llama3")

vector_db = None


def process_document(filepath):

    global vector_db

    loader = PyPDFLoader(filepath)

    docs = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = splitter.split_documents(docs)

    vector_db = FAISS.from_documents(
        chunks,
        embedding
    )


def ask_question(question):

    global vector_db

    docs = vector_db.similarity_search(question, k=3)

    context = ""

    for d in docs:
        context += d.page_content + "\n"

    prompt = f"""
Context:

{context}

Question:
{question}

Answer:
"""

    return llm.invoke(prompt)
