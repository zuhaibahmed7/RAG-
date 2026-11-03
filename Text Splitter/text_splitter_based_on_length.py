from langchain_text_splitters import CharacterTextSplitter

text = """ 
        hi, this is a sample text that we will use to demonstrate the functionality of the CharacterTextSplitter class. 
        The CharacterTextSplitter class is designed to split a given text into smaller 
        chunks based on a specified character limit. This can be useful for processing large texts or 
        for preparing data for machine learning models that have input size constraints. 
        In this example, we will set a character limit of 50 characters and see how the text is split 
        into smaller segments. Each segment will contain up to 50 characters, and we will print out 
        the resulting chunks to observe the output.
"""

splitter = CharacterTextSplitter(
    chunk_size = 50,
    chunk_overlap = 0,
    separator = ''
)

chunks = splitter.split_text(text)
print(len(chunks))
for i, chunk in enumerate(chunks):
    print(f" Chunk {i+1} : {chunk}")
