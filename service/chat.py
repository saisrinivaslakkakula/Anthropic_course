from anthropic import Anthropic


def chat_service(messages, system=None):
    client = Anthropic()
    model = "claude-sonnet-4-0"
    params = {
        "model": model,
        "max_tokens": 1000,
        "messages": messages,
    }

    if system:
        params["system"] = system
    message = client.messages.create(**params)
    return message.content[0].text
