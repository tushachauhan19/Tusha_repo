from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

model = ChatOllama(model="llama3.2")

prompt = ChatPromptTemplate.from_template(
    "Explain {topic} in simple words."
)

parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({"topic": "Artificial Intelligence"})

print(result)