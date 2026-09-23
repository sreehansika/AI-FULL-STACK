import ollama 
response = ollama.chat(
    model= "llama3.2:3b",
    messages=[
        {"role": "system", "content": "what is definition of AI?how ai is used in real life?.is ai dangerous?"}
    ]
)
print(response["message"]["content"]) 