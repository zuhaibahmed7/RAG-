import os
os.environ["USER_AGENT"] = "my-rag-test"

from langchain_community.document_loaders import WebBaseLoader

urls = [
    "https://en.wikipedia.org/wiki/Artificial_intelligence",
    "https://en.wikipedia.org/wiki/Retrieval-augmented_generation",
    "https://python.langchain.com/docs/introduction/",
    "https://www.python.org/about/",
    "https://www.microsoft.com/en-us/research/project/retrieval-augmented-generation/",
]

loader = WebBaseLoader(urls, continue_on_failure=True)
docs = loader.load()

print(len(docs))                      # one Document per URL that loaded
for d in docs:
    print(d.metadata.get("source"), "->", len(d.page_content), "characters")

print(docs[0].metadata)
print(docs[0].page_content[:500])     # first 500 characters only