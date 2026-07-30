from pydantic import BaseModel
from typing import List
from langchain_ollama import ChatOllama

class Recipe(BaseModel):
    title: str
    ingredients: List[str]
    steps: List[str]

model = ChatOllama(model="llama3.2")

structured_model = model.with_structured_output(Recipe)

result = structured_model.invoke(
    "Give me a recipe for Veg Fried Rice."
)

print(result)

print("\nTitle:")
print(result.title)

print("\nIngredients:")
for item in result.ingredients:
    print("-", item)

print("\nSteps:")
for step in result.steps:
    print("-", step)