from langchain_experimental.text_splitter import SemanticChunker
from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

text_splitter = SemanticChunker(
    embeddings,
    breakpoint_threshold_type="standard_deviation",
    breakpoint_threshold_amount=2,
)

sample = """
Farmers in Sindh begin sowing wheat in November, when the weather turns cooler.
The crop needs regular irrigation, and yields depend heavily on canal water supply.
Fertilizer use and seed quality also affect how much wheat each acre produces.

Cricket is the most popular sport in Pakistan, and matches draw huge crowds.
The national team plays Test matches, one-day internationals and T20 games.
Young players often start in local clubs before joining domestic tournaments.

Neural networks learn patterns by adjusting weights during training.
Large language models are trained on huge text datasets using the transformer architecture.
Retrieval-augmented generation lets a model answer using documents it was not trained on.
"""

chunks = text_splitter.split_text(sample)

print(len(chunks), "chunks")
for i, chunk in enumerate(chunks):
    print(f"\nChunk {i+1}:\n{chunk}")
