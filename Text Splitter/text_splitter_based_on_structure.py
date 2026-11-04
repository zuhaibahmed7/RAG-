from langchain_text_splitters import RecursiveCharacterTextSplitter

text = """
        hi, this is a sample text that we will use to demonstrate the 
        functionality of the RecursiveCharacterTextSplitter class.

        The RecursiveCharacterTextSplitter class is designed to split a given text into smaller
        chunks based on a specified character limit. This can be useful for processing large texts or
        for creating more manageable pieces of text for further analysis or processing.
        """

splitter = RecursiveCharacterTextSplitter(
    chunk_size = 55,
    chunk_overlap = 0,
)

chunks = splitter.split_text(text)
print(len(chunks))
print(chunks)

for i, chunk in enumerate(chunks):
    print(f"Chunk {i+1} : {chunk}")
