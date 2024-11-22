import os

import pdf_qa_agent
import warnings

warnings.filterwarnings("ignore")

if __name__ == "__main__":
    questions = []
    document_name = input(
        "Add the document to /docs directory and mention the name of the file here, example: handbook.pdf: "
    )
    while True:
        question = input("Please enter your question or q to quit: ")
        if question == "q":
            break
        questions.append(question)

    if questions:
        answers = pdf_qa_agent.get_answers(f"docs/{document_name}", questions)
        for question in answers:
            print("question: " + question)
            print("answers: " + answers[question])

    print("Bye")
