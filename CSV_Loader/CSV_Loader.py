import langchain
from langchain_community.document_loaders import CSVLoader



loader = CSVLoader("sample_text_document.csv", encoding="utf-8")
docs = loader.load()
print(docs[0])
print(len(docs))