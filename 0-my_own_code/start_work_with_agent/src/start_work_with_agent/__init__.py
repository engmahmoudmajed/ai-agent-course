from os import getenv

from dotenv import load_dotenv
load_dotenv()  # loads .env into environment variables
from openrouter import OpenRouter

from IPython.display import Markdown,display

def main() -> None:
    api_key = getenv("OPENROUTER_API_KEY")
    if not api_key:
        raise SystemExit("OPENROUTER_API_KEY not found. Check your .env file.")

    with OpenRouter(api_key=api_key) as client:
        res = client.chat.send(
            model="openrouter/free",
            messages=[
                {"role": "user", "content": "What is the capital of France?"},
            ],
            stream=False,
        )
    # Print only the model's answer, not the whole response object
    answer = res.choices[0].message.content
    print(answer)
    # 
    display(Markdown(answer))









