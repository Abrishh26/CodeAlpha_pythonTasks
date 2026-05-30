def get_response(msg):
    msg = msg.lower().strip()
    
    if "hello" in msg or "hi" in msg or "hey" in msg:
        return "Hey! How can I help you today?"
    elif "how are you" in msg:
        return "I'm doing great, thanks for asking!"
    elif "your name" in msg or "who are you" in msg:
        return "I'm PyBot, a simple Python chatbot!"
    elif "what can you do" in msg or "help" in msg:
        return "I can answer basic questions. Try asking my name or how I am!"
    elif "time" in msg:
        import datetime
        return f"Current time is: {datetime.datetime.now().strftime('%H:%M:%S')}"
    elif "date" in msg:
        import datetime
        return f"Today's date is: {datetime.datetime.now().strftime('%d-%m-%Y')}"
    elif "joke" in msg:
        return "Why do programmers prefer dark mode? Because light attracts bugs!"
    elif "bye" in msg or "exit" in msg or "quit" in msg:
        return "Goodbye! Have a great day!"
    else:
        return "I'm not sure about that. Try asking something else!"

print("=== PyBot Chatbot ===")
print("Type 'bye' to exit.\n")

while True:
    user = input("You: ")
    if not user.strip():
        continue
    response = get_response(user)
    print(f"PyBot: {response}\n")
    if any(word in user.lower() for word in ["bye", "exit", "quit"]):
        break