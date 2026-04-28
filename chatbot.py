def chatbot():
    print("🤖 Chatbot: Hello! Type 'exit' to quit.")

    while True:
        user = input("You: ").lower()

        if user == "exit":
            print("Chatbot: Goodbye!")
            break

        elif "hello" in user or "hi" in user:
            print("Chatbot: Hello there!")

        elif "how are you" in user:
            print("Chatbot: I'm just a program, but I'm doing great!")

        elif "your name" in user:
            print("Chatbot: I'm a Python chatbot.")

        elif "python" in user:
            print("Chatbot: Python is a powerful programming language.")

        elif "bye" in user:
            print("Chatbot: Bye! Have a nice day!")
            break

        else:
            print("Chatbot: Sorry, I don't understand.")

chatbot()
