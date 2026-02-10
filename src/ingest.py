from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

from src.config import CHUNK_SIZE, CHUNK_OVERLAP


def load_pdfs(folder_path: str):
    docs = []
    for pdf_file in Path(folder_path).glob("*.pdf"):
        loader = PyPDFLoader(str(pdf_file))
        docs.extend(loader.load())
    return docs


def chunk_docs(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    )
    return splitter.split_documents(documents)


def build_and_save_vectorstore(chunks, path="vectordb/faiss_index"):
    embedding_model = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    db = FAISS.from_documents(chunks, embedding_model)
    db.save_local(path)


if __name__ == "__main__":
    documents = load_pdfs("data/docs")
    print("Total pages loaded:", len(documents))

    chunks = chunk_docs(documents)
    print("Total chunks created:", len(chunks))

    build_and_save_vectorstore(chunks)
    print("Vector store created and saved.")
