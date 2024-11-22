from openai import OpenAI

client = OpenAI()


def get_generation(prompt: str, model_name="gpt-4o-mini"):
    completion = client.chat.completions.create(
        model=model_name, messages=[{"role": "user", "content": prompt}]
    )

    # handle exceptions here
    return completion.choices[0].message
