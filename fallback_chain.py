from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Invalid model
bad_model = ChatOllama(model="wrong_model_name")

# Valid fallback model
good_model = ChatOllama(model="llama3.2")

prompt = ChatPromptTemplate.from_template(
    "Explain {topic}"
)

parser = StrOutputParser()

primary_chain = prompt | bad_model | parser
fallback_chain = prompt | good_model | parser

chain = primary_chain.with_fallbacks([fallback_chain])

result = chain.invoke({
    "topic":"Neural Networks"
})

print(result)
