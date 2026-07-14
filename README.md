# Basic Rule-Based Chatbot

A simple console-based chatbot built in Python that responds to predefined user inputs using basic conditional logic.

## Overview

This project simulates a basic conversational chatbot. It doesn't use any machine learning or external APIs — instead, it relies on simple pattern matching with `if-elif` statements to recognize common phrases like greetings, questions, and farewells, and responds with predefined replies. The chatbot runs continuously in the console until the user says goodbye.

## Features

- Recognizes common conversational inputs (e.g., "hello", "how are you", "bye")
- Responds with friendly, predefined replies
- Runs in a continuous loop for back-and-forth conversation
- Includes a `help` command to guide the user on what it understands
- Gracefully handles unrecognized input with a default response
- Ends the conversation cleanly when the user says goodbye

## Key Concepts Used

- **Functions** — response logic is organized into a reusable `get_response()` function
- **if-elif statements** — used to match user input against known phrases
- **Loops** — a `while` loop keeps the conversation going until the user exits
- **Input/Output** — takes user input from the console and prints chatbot replies

## Recognized Inputs

| User Input                          | Chatbot Response                              |
|--------------------------------------|------------------------------------------------|
| hello / hi / hey                     | Hi there!                                       |
| how are you / how are you?           | I'm fine, thanks! How about you?                |
| bye / goodbye / see you              | Goodbye! Have a great day!                      |
| what is your name / who are you      | I'm a simple rule-based chatbot.                |
| thank you / thanks                   | You're welcome!                                 |
| help                                  | Lists example phrases the chatbot understands   |
| *(anything else)*                    | Sorry, I don't understand that. Type 'help'...  |

*Input is not case-sensitive — "HELLO", "Hello", and "hello" are all treated the same.*

## How to Run

1. Make sure Python 3 is installed on your machine.
2. Save the script as `chatbot.py`.
3. Open a terminal in the folder containing the script.
4. Run the following command:

   ```
   python chatbot.py
   ```

## How to Use

1. Once the program starts, the chatbot will greet you.
2. Type a message and press Enter.
3. The chatbot will respond based on what you typed.
4. Type `help` at any time to see example phrases.
5. Type `bye`, `goodbye`, or `see you` to end the conversation.

## Example Session

```
Chatbot: Hi! I'm a simple chatbot. Type 'bye' to end the conversation.

You: hello
Chatbot: Hi there!

You: how are you
Chatbot: I'm fine, thanks! How about you?

You: what is your name
Chatbot: I'm a simple rule-based chatbot.

You: thanks
Chatbot: You're welcome!

You: bye
Chatbot: Goodbye! Have a great day!
```

## Notes

- This chatbot only recognizes exact phrase matches (after converting to lowercase and trimming whitespace) — it does not use natural language processing (NLP) or fuzzy matching.
- Responses are static and hardcoded; the chatbot does not learn or adapt over time.
- No external libraries or internet connection are required.

## Possible Future Improvements

- Add fuzzy matching or keyword detection instead of exact phrase matching
- Expand the list of recognized phrases and responses
- Integrate a natural language processing (NLP) library like `nltk` or `spaCy`
- Add a graphical or web-based interface
- Store conversation history to a file
