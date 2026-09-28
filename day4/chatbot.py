import ollama
msgs = [
     {
          "role" : "system" ,
              "content" : "imagine u r alien from mars."   }
]
while True:
    question = input("enter the question ?")
    if question.lower() == "e":
        break
    msgs.append(
        {
            
            "role" : "user" ,
            "content" : question
        }
    )
    response = ollama.chat(
    model="llama3.2:3b",
    messages=msgs
    )
    msgs.append(
        {
            "role" : "assistant",
            "content" : response["message"]["content"]
        }
    )
    print("AI:",response["message"]["content"])
print("--------chat history------\n")
for msg in msgs:
    if msg["role"] == "system":
        break
    print(msg["role"], ":", msg["content"])