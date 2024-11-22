# PDF QA Agent

Application for answering questions from a PDF.
It uses Retrieval Augmented Generation to add context to the questions before calling your LLM of choice.
Vector Store is used to store the document embeddings. Documents closer in similarity to the query is retrieved from the vector stores.
Along with the user query, docuemnts from the vector store are added to the prompt and sent to llm chat api.
The output is printed on the command line.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)

## Installation

1. Clone the repository:

```bash
 git clone https://github.com/ashwin8618/pdf-qa-agent.git
```

2. Install dependencies:

```bash
 pip install poetry
 poetry install
```

## Usage

To run the project, use the following command on linux:

```bash
export OPENAI_API_KEY = "{YOUR-API-KEY-HERE}"
poetry run python main.py
```

add the pdf document to the docs/ directory

## Design

### VectorStore

There are different types of Vector stores like in-memory stores, Pinecone, QDrant, etc.
To make it vendor agnostic, VectorStore class is abstract and each vendor will have it own subclass.
Main public methods exposed for this abstract class are
add_documents: to add embeddings of the documents to the store
similarity_search: retrieve the relevant documents based on the query text

factory method create_vector_store is added to separate creation logic

## Prompt Template

Base PromptTemplate class which generate the prompt string from the template provided by subclasses
Different use cases can have different prompt templates like RAG, JSON output, translation, etc

factory methods create_x_prompt are added for different usecases

## agent chain

Simple linear agent code is implemented.
In the future, frameworks like langchain could be leveraged to add callbacks, logging, etc

## Extensibility of the system

There are some dependencies with langchain specific functions and classes:
langchain_core.documents.Document: We can implement our own document class to decouple with any specific agentic library
langchain_core.vectorstores: Even though this is abstracted using composition, but still the vector store logic can be implemented in house
