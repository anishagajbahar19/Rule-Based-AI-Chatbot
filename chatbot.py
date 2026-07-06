# ===========================================
# Rule-Based AI Chatbot
# DecodeLabs Internship - Project 1
# Created by: Anisha Gajbahar
# ===========================================

print("=" * 50)
print("🤖 Welcome to DecodeBot")
print("=" * 50)
print("Type 'bye', 'exit' or 'quit' to end the chat.\n")

# Dictionary of responses
responses = {

    "hello": "Hi! Welcome to DecodeLabs.",

    "hi": "Hello! Nice to meet you.",

    "hey": "Hey! How can I help you?",

    "good morning": "Good Morning! Have a wonderful day.",

    "good afternoon": "Good Afternoon!",

    "good evening": "Good Evening!",

    "how are you": "I'm doing great! Thanks for asking.",

    "what is your name": "My name is DecodeBot.",

    "who created you": "I was created by Anisha for the DecodeLabs Internship.",

    "what is ai": "Artificial Intelligence enables machines to mimic human intelligence.",

    "what is python": "Python is a simple and powerful programming language.",

    "thank you": "You're welcome!",

    "thanks": "Happy to help!",

    "help": """I can answer:
- hello
- hi
- hey
- how are you
- what is your name
- what is ai
- what is python
- thank you
- bye"""
}

# Infinite loop
while True:

    user = input("\nYou : ")

    # Input Sanitization
    user = user.lower().strip()

    # Exit Commands
    if user in ["bye", "exit", "quit"]:

        print("\nBot : Goodbye! Have a great day! 👋")

        break

    # Dictionary Lookup
    reply = responses.get(
        user,
        "Sorry, I don't understand that. Type 'help' to see what I can do."
    )

    print("\nBot :", reply)