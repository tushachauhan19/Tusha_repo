from ollama import chat

response = chat(
    model="llama3.2",
    messages=[
        {
            "role": "user",
            "content": "Explain Artificial Intelligence in simple words."
        }
    ]
)

print(response["message"]["content"])
from ollama import chat

print("=" * 50)
print("      Local AI Chatbot")
print("Type 'exit' to quit")
print("=" * 50)

while True:
    user = input("\nYou: ")

    if user.lower() == "exit":
        print("Goodbye!")
        break

    response = chat(
        model="llama3.2",
        messages=[
            {
                "role": "user",
                "content": user
            }
        ]
    )

    print("\nAI:", response["message"]["content"])