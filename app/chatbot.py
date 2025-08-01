from langchain.agents import AgentType, initialize_agent
from langchain_community.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory


chat = ChatOpenAI(
    temperature = 0.3,
    model_name="google/gemma-3-12b",
    base_url="http://127.0.0.1:1234/v1",
    api_key='bekabekabeka'
)

memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True
)

agent = initialize_agent(
    tools=[],  # Tu możesz dodać narzędzia dla agenta
    llm=chat,
    agent=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION,
    memory=memory,
    verbose=True
)

def chat_with_agent(user_input: str) -> str:
    response = agent.run(user_input)
    return response


if __name__ == "__main__":
    response = chat_with_agent("test")
    print(f"Bot: {response}")
