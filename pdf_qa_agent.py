import document_utils
import openai_api
import prompt_template
import vector_store


def get_answers(file_path: str, questions: list[str]) -> dict:

    result = dict()

    docs = document_utils.load_pdf_doc(file_path)

    # split the document to match relevant chunks with the query
    splits = document_utils.split_docs(docs)

    vectorstore = vector_store.get_vector_store("in_memory")

    vectorstore.add_documents(splits)

    for question in questions:
        similar_docs = vectorstore.similarity_search(question)

        prompt = prompt_template.create_rag_prompt(question, similar_docs)

        answer = openai_api.get_generation(prompt)
        result[question] = answer.content

    return result
