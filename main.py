from fastapi import FastAPI
from rag import RAG

app = FastAPI()

rag = RAG("data")
rag.build_index() 

@app.get("/")
def root():
    return {"message": "RAG API is running"}

@app.get("/ask")
def ask(query: str):
    return {"answer": rag.generate(query)}







