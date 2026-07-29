from pydantic import BaseModel
from typing import List
from langchain_ollama import ChatOllama

class Recipe(BaseModel):
    title: str
    ingredients: List[str]
    steps: List[str]

model = ChatOllama(model="llama3.2")

structured_model = model.with_structured_output(Recipe)

prompt = "Say Hello only."

for attempt in range(2):

    try:

        result = structured_model.invoke(prompt)

        print(result)

        break

    except Exception:

        print("Retry", attempt + 1)

        prompt = "Return a proper recipe for Pasta."