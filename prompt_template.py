from langchain_core.documents import Document
from abc import ABC, abstractmethod


class PromptTemplate(ABC):
    def __init__(self):
        self.system_prompt = ""
        self._context = "context"
        self._human_input = "input"

    def add_human_input(self, input: str):
        self.human_input = input

    def add_context(self, context: str):
        self.context = context

    def get_prompt(self) -> str:
        prompt = self.system_prompt.replace("{input}", self.human_input).replace(
            "{context}", self.context
        )
        return prompt


class RAGPromptTemplate(PromptTemplate):
    def __init__(self):
        self.system_prompt = """
    Use the following pieces of context to answer the question at the end. If you 
    don't know the answer, just say that you don't know, don't try to make up an 
    answer.
    
    {context}
    
    Question: {input}
    Helpful Answer:
    """


def create_rag_prompt(question: str, context: list[Document]):
    template = RAGPromptTemplate()
    template.add_human_input(question)
    context = "\n\n".join([doc.page_content for doc in context])
    template.add_context(context)
    return template.get_prompt()
