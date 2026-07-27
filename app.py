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