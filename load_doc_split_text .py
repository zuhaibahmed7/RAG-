from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("sample_text_document.pdf")
documents = loader.load()
text = documents[0].page_content
splitter = CharacterTextSplitter(
    chunk_size = 50,
    chunk_overlap = 0,
    separator = ''
)

chunks = splitter.split_documents(documents)
print(len(chunks))
for i, chunk in enumerate(chunks):
    print(f" Chunk {i+1} : {chunk}")
