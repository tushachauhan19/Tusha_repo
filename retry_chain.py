from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

model = ChatOllama(model="wrong_model_name")

prompt = ChatPromptTemplate.from_template(
    "Explain {topic}"
)

parser = StrOutputParser()

chain = (
    prompt
    | model
    | parser
).with_retry()

try:
    result = chain.invoke({
        "topic":"Python"
    })
    print(result)

except Exception as e:
    print("Retry Failed")
    print(e)
