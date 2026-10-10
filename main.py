from src.chat import ChatSession


def main():
    print("🤖 Groq Chat — type 'exit' to quit\n")
    session = ChatSession()

    while True:
        try:
            user_input = input("You: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nGoodbye!")
            break

        if not user_input:
            continue

        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        if user_input.lower() == "clear":
            print("Conversation cleared!")
            session = ChatSession()
            continue

        if user_input.lower() == "save":
            path = session.save()
            print(f"💾 Saved to {path}\n")
            continue

        try:
            reply = session.send(user_input)
            print(f"AI: {reply}\n")
        except Exception as e:
            print(f"⚠️  Error: {e}\n")


if __name__ == "__main__":
    main()