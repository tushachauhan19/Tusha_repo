<<<<<<< HEAD
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
=======
print("Virtual Environment is Working!")

name = input("Enter your name: ")
print(f"Welcome, {name}!")

for i in range(1, 6):
    print(f"Count: {i}")
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage

llm = ChatOllama(model="llama3.2")

response = llm.invoke([
    HumanMessage(content="Hello!")
])

print(response.content)

from langchain_ollama import ChatOllama

llm = ChatOllama(model="llama3.2")

for chunk in llm.stream("Tell me about Artificial Intelligence in 50 words."):
    print(chunk.content, end="", flush=True)


from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage

llm = ChatOllama(model="llama3.2")

messages = [
    SystemMessage(content="You are a Python teacher. Answer briefly."),
    HumanMessage(content="What is a list in Python?")
]

response = llm.invoke(messages)

print(response.content)



from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama

llm = ChatOllama(model="llama3.2")

prompt = ChatPromptTemplate.from_template(
    "Explain {topic} in simple words."
)

formatted_prompt = prompt.invoke({"topic": "Machine Learning"})

response = llm.invoke(formatted_prompt)

print(response.content)


from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage
from langchain_ollama import ChatOllama

llm = ChatOllama(model="llama3.2")

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI tutor."),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{question}")
])

history = [
    HumanMessage(content="What is Python?"),
    AIMessage(content="Python is a programming language.")
]

formatted_prompt = prompt.invoke({
    "history": history,
    "question": "Who created it?"
})

response = llm.invoke(formatted_prompt)

print(response.content)


from langchain_core.prompts import (
    ChatPromptTemplate,
    FewShotChatMessagePromptTemplate
)
from langchain_ollama import ChatOllama

llm = ChatOllama(model="llama3.2")

examples = [
    {
        "input": "2 + 2",
        "output": "4"
    },
    {
        "input": "5 + 7",
        "output": "12"
    },
    {
        "input": "10 + 15",
        "output": "25"
    }
]

example_prompt = ChatPromptTemplate.from_messages([
    ("human", "{input}"),
    ("ai", "{output}")
])

few_shot_prompt = FewShotChatMessagePromptTemplate(
    example_prompt=example_prompt,
    examples=examples,
)

final_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a math assistant."),
    few_shot_prompt,
    ("human", "{input}")
])

formatted_prompt = final_prompt.invoke({
    "input": "8 + 9"
})

response = llm.invoke(formatted_prompt)

print(response.content)
>>>>>>> 39dc64c34ead775b22f028f39c4b8c8ee0e1af0a
