from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_ollama import ChatOllama

from src.config import TOP_K
from src.prompts import RAG_PROMPT


def load_vectorstore(path="vectordb/faiss_index"):
    embedding_model = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    db = FAISS.load_local(
        path,
        embedding_model,
        allow_dangerous_deserialization=True
    )
    return db


def _format_context(docs):
    return "\n\n".join(
        f"(Page {d.metadata.get('page', 'N/A')}) {d.page_content}"
        for d in docs
    )


def answer_question(db, question: str):
    retriever = db.as_retriever(search_kwargs={"k": TOP_K})
    docs = retriever.invoke(question)

    context = _format_context(docs)

    llm = ChatOllama(
        model="phi3:mini",
        temperature=0.0
    )

    prompt = RAG_PROMPT.format(
        context=context,
        question=question
    )

    response = llm.invoke(prompt)

    return response.content, docs