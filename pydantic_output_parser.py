import json

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import ChatOllama

prompt = ChatPromptTemplate.from_template("""
Return ONLY valid JSON.

Example:

{{
"title":"...",
"ingredients":["..."],
"steps":["..."]
}}

Recipe: {dish}
""")

model = ChatOllama(model="llama3.2")

chain = prompt | model | StrOutputParser()

result = chain.invoke({"dish":"Paneer Butter Masala"})

print(result)

recipe = json.loads(result)

print(recipe["title"])