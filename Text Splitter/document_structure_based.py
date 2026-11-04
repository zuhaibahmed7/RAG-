from langchain_text_splitters import RecursiveCharacterTextSplitter, Language

text = """# Guide
## Install
Run pip install.
## Usage
Call the function.
"""

splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.MARKDOWN,
    chunk_size = 50,
    chunk_overlap = 0,
)

chunks = splitter.split_text(text)
print(len(chunks))
for i, chunk in enumerate(chunks):
    print(f"Chunk {i+1} : {chunk}")


