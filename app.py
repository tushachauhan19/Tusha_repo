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