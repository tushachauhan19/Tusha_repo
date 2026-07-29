from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load Model
model = ChatOllama(model="llama3.2")

# Prompt
prompt = ChatPromptTemplate.from_template(
    "Explain {topic} in simple words."
)

# Output Parser
parser = StrOutputParser()

# LCEL Chain
chain = prompt | model | parser

# Invoke
result = chain.invoke({"topic": "Machine Learning"})

print(result)