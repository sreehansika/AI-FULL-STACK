import ollama 
response = ollama.chat(
    model= "llama3.2:3b",
    messages=[
        {"role": "system", "content": "imagine u are a teacher and explain the concept of AI to a 10 year old child in simple words."},
        {"role": "system", "content": "tell about cyber security and how to protect our data online."}
    ]
)
print(response["message"]["content"]) 