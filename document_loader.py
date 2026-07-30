from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# -----------------------------
# Load Local TXT File
# -----------------------------

loader = TextLoader("sample.txt")

documents = loader.load()

print("=" * 60)
print("DOCUMENT LOADED")
print("=" * 60)

print("Number of Documents:", len(documents))
print()

print(documents[0].page_content)

print("\n")

# -----------------------------
# Experiment 1
# -----------------------------

splitter = RecursiveCharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=50
)

chunks = splitter.split_documents(documents)

print("=" * 60)
print("EXPERIMENT 1")
print("=" * 60)

print("Chunk Size = 200")
print("Chunk Overlap = 50")
print()

print("Total Chunks:", len(chunks))

for i, chunk in enumerate(chunks):
    print(f"\nChunk {i+1}")
    print("-" * 40)
    print(chunk.page_content)
    print("Characters:", len(chunk.page_content))

print("\n")

# -----------------------------
# Experiment 2
# -----------------------------

splitter2 = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=20
)

chunks2 = splitter2.split_documents(documents)

print("=" * 60)
print("EXPERIMENT 2")
print("=" * 60)

print("Chunk Size = 100")
print("Chunk Overlap = 20")
print()

print("Total Chunks:", len(chunks2))

for i, chunk in enumerate(chunks2):
    print(f"\nChunk {i+1}")
    print("-" * 40)
    print(chunk.page_content)
    print("Characters:", len(chunk.page_content))