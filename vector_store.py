from langchain_core.vectorstores import InMemoryVectorStore as LCInMemoryVectorStore
from langchain_openai import OpenAIEmbeddings
from langchain_core.documents import Document
from abc import ABC, abstractmethod


class VectorStore(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def add_documents(
        self,
        docs: list[Document],
        index_name="",
    ):
        pass

    @abstractmethod
    def similarity_search(self, query: str):
        pass


class InMemoryVectorStore(VectorStore):
    def __init__(self, embeddings_provider=OpenAIEmbeddings()):
        self._vector_store = LCInMemoryVectorStore(embeddings_provider)

    def add_documents(
        self,
        docs: list[Document],
        index_name="",
    ):
        self._vector_store.add_documents(docs)

    def similarity_search(self, query: str):
        return self._vector_store.similarity_search(query)


class FAISSVectorStore(VectorStore):
    pass


class PineconeVectorStore(VectorStore):
    pass


def get_vector_store(
    store_name="in_memory", embeddings_provider="openai"
) -> VectorStore:
    if store_name == "in_memory":
        if embeddings_provider == "openai":
            return InMemoryVectorStore(embeddings_provider=OpenAIEmbeddings())

    # handle other llms and vector stores here
