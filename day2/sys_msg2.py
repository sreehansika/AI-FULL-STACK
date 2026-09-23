import ollama 
response = ollama.chat(
    model= "llama3.2:3b",
    messages=[
        {"role": "system", "content": "imagine u are a teacher of a 5th grade student and explain the concept of AI to a 10 year old child in simple words."},
        {"role": "system", "content": "explain in only 5 lines."}
    ]
)
print(response["message"]["content"]) 