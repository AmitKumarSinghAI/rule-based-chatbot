print("🤖 Chatbot: Hello! I’m your friendly chatbot. Type 'exit' anytime to quit.")

while True:
    user_input = input("You: ").lower()  # Convert to lowercase for easy matching
    
    # Exit condition
    if user_input == "exit":
        print("🤖 Chatbot: Goodbye! Have a great day! 👋")
        break
    
    # Greeting responses
    elif user_input in ["hi", "hello", "hey"]:
        print("🤖 Chatbot: Hi there! How can I help you today?")
    
    # Asking about the chatbot
    elif "your name" in user_input:
        print("🤖 Chatbot: I’m a simple rule-based chatbot created in Python.")
    
    # Asking about the weather
    elif "weather" in user_input:
        print("🤖 Chatbot: I can’t check live weather yet, but I hope it’s sunny where you are! ☀️")
    
    # Asking about the chatbot's purpose
    elif "what can you do" in user_input or "help" in user_input:
        print("🤖 Chatbot: I can chat with you and answer basic questions!")
    
    # Asking about Python
    elif "python" in user_input or "py" in user_input:
        print("🤖 Chatbot: Python is a powerful programming language, great for AI, data science, and more!")
    
    # Asking about time
    elif "time" in user_input :
        from datetime import datetime
        print(f"🤖 Chatbot: The current time is {datetime.now().strftime('%H:%M:%S')}")
    
    # Asking about day/date
    elif "date" in user_input:
        from datetime import datetime
        print(f"🤖 Chatbot: Today’s date is {datetime.now().strftime('%Y-%m-%d')}")
    
    # Unknown responses
    else:
        print("🤖 Chatbot: Sorry, I didn’t understand that. Can you try rephrasing?")
