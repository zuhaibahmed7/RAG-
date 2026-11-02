# RAG

This repository contains introductory material and sample code for **Retrieval-Augmented Generation (RAG)**.

## What is RAG?

RAG combines:
- **Retrieval**: fetch relevant context from a knowledge source (documents, vector database, etc.)
- **Generation**: use an LLM to answer using the retrieved context

This helps improve factuality, relevance, and grounding in source data.

## Typical RAG pipeline

1. Collect and chunk source documents
2. Create embeddings for chunks
3. Store embeddings in a vector index
4. Retrieve top-k relevant chunks for a user question
5. Build a prompt with the retrieved context
6. Generate the final answer with an LLM

## Minimal Python example

```python
def simple_rag(question, retriever, llm, k=3):
    # 1) retrieve supporting context
    docs = retriever.search(question, top_k=k)
    context = "\n\n".join(doc["text"] for doc in docs)

    # 2) build grounded prompt
    prompt = f"""
You are a helpful assistant. Use only the context below.

Context:
{context}

Question:
{question}

Answer:
"""

    # 3) generate answer
    return llm.generate(prompt)
```

## Notes

- Keep chunks small enough for precise retrieval.
- Include source attribution in answers when possible.
- Evaluate retrieval quality separately from generation quality.