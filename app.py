from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings, HuggingFacePipeline
from transformers import pipeline
from langchain.chains import RetrievalQA

# Load embedding model
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Load FAISS vector database
db = FAISS.load_local(
    "vectorstore",
    embeddings,
    allow_dangerous_deserialization=True
)

# Create retriever
retriever = db.as_retriever(search_kwargs={"k": 3})

# Load Hugging Face model
pipe = pipeline(
    "text2text-generation",
    model="google/flan-t5-base",
    max_new_tokens=256
)

llm = HuggingFacePipeline(pipeline=pipe)

# Create RetrievalQA chain
qa = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    chain_type="stuff"
)

print("=" * 50)
print("RAG Chatbot is Ready!")
print("Type 'exit' to quit.")
print("=" * 50)

while True:
    query = input("\nYou: ")

    if query.lower() == "exit":
        print("Goodbye!")
        break
 # Show retrieved documents
    docs = retriever.invoke(query)

    print("\nRetrieved Documents:\n")
    for i, doc in enumerate(docs, 1):
        print(f"Chunk {i}:")
        print(doc.page_content)
        print("-" * 50)


    result = qa.invoke({"query": query})

    print("\nBot:", result["result"])