from langchain_core.runnables import RunnableLambda
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser

model = ChatOllama(model="llama3.2")
parser = StrOutputParser()

# Custom Python Function
def uppercase(data):
    data["topic"] = data["topic"].upper()
    return data

lambda_step = RunnableLambda(uppercase)

prompt = ChatPromptTemplate.from_template(
    "Explain {topic}"
)

chain = (
    lambda_step
    | prompt
    | model
    | parser
)

result = chain.invoke({
    "topic":"artificial intelligence"
})

print(result)