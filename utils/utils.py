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