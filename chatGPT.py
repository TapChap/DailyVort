from openai import OpenAI as chatGPT
from GPTconfig import *

# OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
# print(OPENAI_API_KEY)
# print(os.environ.get("OPENAI_API_KEY"))

client = chatGPT()

def chatGPT(prompt: CompositePrompt, config = config):
    response = client.chat.completions.create(
        model = config.model,
        max_tokens= config.max_tokens,
        messages = prompt.toJson()
    )

    return response.choices[0].message.content