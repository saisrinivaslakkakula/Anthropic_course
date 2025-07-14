from anthropic import Anthropic

def chat_service(messages):
    client = Anthropic()
    model = "claude-sonnet-4-0"
    message = client.messages.create(
        model=model,
        max_tokens=1000,
        messages=messages
    )
    return message.content[0].text