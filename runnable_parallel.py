from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

model = ChatOllama(model="llama3.2")
parser = StrOutputParser()

summary_prompt = ChatPromptTemplate.from_template(
    "Summarize this:\n{text}"
)

translation_prompt = ChatPromptTemplate.from_template(
    "Translate this into Hindi:\n{text}"
)

summary_chain = summary_prompt | model | parser
translation_chain = translation_prompt | model | parser

parallel_chain = RunnableParallel(
    summary=summary_chain,
    translation=translation_chain
)

result = parallel_chain.invoke({
    "text":"Artificial Intelligence is changing the world rapidly."
})

print(result)
