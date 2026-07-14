def get_response(user_input):
    text = user_input.lower().strip()

    if text in ["hello", "hi", "hey"]:
        return "Hi there!"
    elif text in ["how are you", "how are you?"]:
        return "I'm fine, thanks! How about you?"
    elif text in ["bye", "goodbye", "see you"]:
        return "Goodbye! Have a great day!"
    elif text in ["what is your name", "what's your name", "who are you"]:
        return "I'm a simple rule-based chatbot."
    elif text in ["thank you", "thanks"]:
        return "You're welcome!"
    elif text == "help":
        return "You can try saying: hello, how are you, thank you, or bye."
    else:
        return "Sorry, I don't understand that. Type 'help' to see what I can respond to."

def chat():
    print("Chatbot: Hi! I'm a simple chatbot. Type 'bye' to end the conversation.\n")

    while True:
        user_input = input("You: ")

        if user_input.lower().strip() in ["bye", "goodbye", "see you"]:
            print("Chatbot: Goodbye! Have a great day!")
            break

        response = get_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    chat()