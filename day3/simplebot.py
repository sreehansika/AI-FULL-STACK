import ollama 
while True:
    question = input("Enter your question: ")
    if question.lower() == "e":
        break
    response = ollama.chat(
    model= "llama3.2:3b",
    messages=[
        {"role": "system", "content": "explain in 2-3lines."},
        {"role": "user", "content": question}
    ]
    )
    print(response["message"]["content"])