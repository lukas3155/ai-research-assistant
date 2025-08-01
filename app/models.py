from pydantic import BaseModel, Field

class AgentInput(BaseModel):
    query: str = Field(..., description="The user's input query to process")
