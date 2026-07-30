from pydantic import BaseModel
from typing import List
from langchain_ollama import ChatOllama

class Recipe(BaseModel):
    title: str
    ingredients: List[str]
    steps: List[str]

model = ChatOllama(model="llama3.2")

structured_model = model.with_structured_output(Recipe)

try:

    result = structured_model.invoke(
        "Say Hello only."
    )

    print(result)

except Exception as e:

    print("Parsing Failed!")

    print(e)