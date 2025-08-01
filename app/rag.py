from langchain_community.retrievers import ArxivRetriever

def get_arxiv_retriever(load_max_docs: int = 3, get_full_documents: bool = True):

    return ArxivRetriever(
        load_max_docs=load_max_docs,
        get_full_documents=get_full_documents
    )

