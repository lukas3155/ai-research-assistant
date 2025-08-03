from langchain.memory import ConversationBufferMemory
from langchain.agents import AgentType, initialize_agent
from langchain_community.chat_models import ChatOpenAI
from app.agent_tools import get_information
from app.const import SYSTEM_INSTRUCTION

chat = ChatOpenAI(
    temperature=0.3,
    model_name=os.getenv('LLM_MODEL_NAME', 'google/gemma-3-12b'),
    base_url=os.getenv('LLM_BASE_URL', 'http://127.0.0.1:1234/v1'),
    api_key=os.getenv('LLM_API_KEY', 'bekabekabeka')
)


memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True
)

agent = initialize_agent(
    tools=[
        get_information
    ],
    agent_kwargs={
        "system_message": SYSTEM_INSTRUCTION
    },
    llm=chat,
    agent=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION,
    memory=memory,
    verbose=True
)

def chat_with_agent(user_input: str) -> str:
    response = agent.run(user_input)
    return response