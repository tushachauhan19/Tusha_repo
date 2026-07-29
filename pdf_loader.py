from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

loader = PyPDFLoader("sample.pdf")

documents = loader.load()

print("Pages Loaded:", len(documents))

splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=50
)

chunks = splitter.split_documents(documents)

print("Chunks:", len(chunks))

for i, chunk in enumerate(chunks):
    print(f"\nChunk {i+1}")
    print(chunk.page_content[:150])