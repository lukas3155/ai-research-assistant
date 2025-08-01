from langchain.tools import tool
from app.rag import get_arxiv_retriever


@tool
def get_information(information: str):
    """Searches for scientific information in the arXiv database based on a query.

    Args:
        information: Query or topic to search for in the arXiv database

    Returns:
        Documents containing information on the specified topic
    """
    retriever = get_arxiv_retriever()
    docs = retriever.invoke(information)
    return docs