from utils import utils
from service import chat


def exercise_system_prompt_and_temperature(messages):
    while True:
        user_text = input("YOU:")
        utils.add_user_message(messages, user_text)
        ai_response = chat.chat_service(messages, None, 0.0)
        print(f"AI: {ai_response}")
        utils.add_assistant_message(messages, ai_response)


def exercise_message_streaming(messages):
    utils.add_user_message(messages, input("YOU:"))
    stream = chat.chat_service_with_stream(messages)
    with stream as stream:
        for text in stream.text_stream:
            print(text, end="")


def exercise_structure_data(messages):
    prompt = """
    Generate three different AWS CLI commands. Each should be very short.
    """
    utils.add_user_message(messages, prompt)
    utils.add_assistant_message(messages,
                                "Here are the three commands in single line without any "
                                "comments:\n```bash")
    response = chat.chat_service(messages, None, 0.0, ["```"])
    print(response)
