import sys
from pathlib import Path

# --- add project root to Python path ---
PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

import streamlit as st
from src.rag import load_vectorstore, answer_question


st.title("📘 Study Assistant (RAG Bot)")

@st.cache_resource
def load_db():
    return load_vectorstore()

db = load_db()

question = st.text_input("Ask a question from your PDFs:")

if question:
    with st.spinner("Thinking..."):
        answer, docs = answer_question(db, question)

    st.subheader("🧠 Answer")
    st.write(answer)

    st.subheader("📚 Sources")
    for i, d in enumerate(docs):
        st.write(f"**Chunk {i+1}** (Page: {d.metadata.get('page', 'N/A')})")
        st.write(d.page_content[:400])
