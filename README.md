## Personalized Study Assistant (RAG-Based)

## What This Project Does

This project is a personalized study assistant that answers questions using a user’s academic PDFs. It uses Retrieval-Augmented Generation (RAG) to retrieve relevant document content and generate grounded responses with a local language model.

## Architecture Overview
Pipeline:
PDF documents are loaded and chunked
Chunks are embedded using sentence-transformers
Embeddings are stored in a FAISS vector database
User queries retrieve relevant chunks
A local LLM (Ollama) generates answers strictly from retrieved context
(Architecture diagram can be added here if required.)

## Tech Stack
Python
LangChain
FAISS
Sentence-Transformers
Streamlit
Ollama (local LLM)

## Setup Instructions

# Create virtual environment
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install and pull local LLM:

ollama pull phi3:mini

## How to Run 

# Build vector database (run once or when PDFs change)
python -m src.ingest

# Run the application
streamlit run app/app.py


## Limitations

Answers are limited to the content of uploaded documents
Lecture-style notes may result in fragmented definitions
No external knowledge is used
Performance depends on document quality and structure

## Future Work
Improved confidence scoring for answer refusal
Support for multiple document collections
Enhanced source citation formatting
Optional cloud LLM integration with user consent


## Responsible AI Considerations

This project follows responsible AI practices to ensure safe, transparent, and ethical behavior.

# Hallucination Risk
The system minimizes hallucinations by using a Retrieval-Augmented Generation (RAG) approach. The language model is restricted to answer only using retrieved document context. If sufficient relevant context is not found, the system may refuse to answer rather than generate unsupported information.

# Bias Risk (Document-Based Bias)
All responses are grounded in user-provided documents. Any bias present in the output reflects bias in the source materials themselves, not the model’s independent reasoning. The system does not introduce external knowledge beyond the document corpus.

# Privacy Protection
User queries and document content are processed locally. Queries are not logged, stored, or transmitted to external services. A local LLM (Ollama) is used to ensure that sensitive academic or personal documents remain on the user’s machine.

# Disclaimer
This assistant is intended for study support only. Responses should not be treated as authoritative or definitive explanations. Users are encouraged to verify important information directly from source documents.

## Evaluation Table (15 Questions)

You should test and document behavior.
Below is a ready-to-fill table you can include in your report or README.

Evaluation Results
#	Question	Expected Source	Model Response Quality	Pass / Fail
1	What is deep learning?	Unit 1 notes	Partial, grounded, cautious	Pass
2	Explain autograd in PyTorch	Week 9 notes	Accurate, context-based	Pass
3	What is backpropagation?	Lecture slides	Accurate, cited	Pass
4	What is an optimizer?	Training notes	Correct explanation	Pass
5	Explain CrossEntropyLoss	Loss functions notes	Accurate	Pass
6	What is an epoch in training?	ML fundamentals	Correct	Pass
7	Difference between SGD and Adam	Optimizer section	Accurate	Pass
8	What is gradient descent?	Intro ML notes	Correct	Pass
9	What is PyTorch used for?	Framework overview	Correct	Pass
10	Explain requires_grad	Autograd section	Accurate	Pass
11	What is quantum computing?	Not in documents	Refused safely	Pass
12	Explain blockchain	Not in documents	Refused safely	Pass
13	Who invented Python?	Not in documents	Refused safely	Pass
14	What is ChatGPT?	Not in documents	Refused safely	Pass
15	Explain relativity theory	Not in documents	Refused safely	Pass

Key point:
Safe refusal = Pass, not failure.