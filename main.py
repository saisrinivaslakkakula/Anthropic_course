from utils import utils
from service import chat


def exercise_system_prompt_and_temperature():
    while True:
        user_text = input("YOU:")
        utils.add_user_message(messages, user_text)
        ai_response = chat.chat_service(messages,None, 0.0)
        print(f"AI: {ai_response}")
        utils.add_assistant_message(messages, ai_response)


def exercise_message_streaming():
    utils.add_user_message(messages, input("YOU:"))
    stream = chat.chat_service_with_stream(messages)
    with stream as stream:
        for text in stream.text_stream:
            print(text, end="")


if __name__ == '__main__':
    messages = []
    exercise_message_streaming()


