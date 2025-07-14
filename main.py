
from dotenv import load_dotenv
from anthropic import Anthropic

def add_user_message(messages:list, text):
    user_message = {
        "role": "user",
        "content": text
    }
    messages.append(user_message)

def add_assistant_message(messages:list, text):
    assistant_message = {
        "role": "assistant",
        "content": text
    }
    messages.append(assistant_message)

def chat(messages):
    message = client.messages.create(
        model=model,
        max_tokens=1000,
        messages=messages
    )

    return message.content[0].text


if __name__ == '__main__':
    load_dotenv()
    client = Anthropic()
    model = "claude-sonnet-4-0"

    messages = []

    while True:
        user_text = input("YOU:")
        add_user_message(messages, user_text)
        ai_response = chat(messages)
        print(f"AI: {ai_response}")
        add_assistant_message(messages, ai_response)



