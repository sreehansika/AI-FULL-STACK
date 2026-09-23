import ollama 
response = ollama.chat(
    model= "llama3.2:3b",
    messages=[
        {"role": "system", "content": "tell intresting facts about space and planets."}
    ]
)
print(response["message"]["content"]) 