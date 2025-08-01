from app.agent import chat_with_agent


if __name__ == "__main__":
    response = chat_with_agent("test")
    print(f"Bot: {response}")