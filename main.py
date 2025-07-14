from dotenv import load_dotenv
from utils import utils
from service import chat

if __name__ == '__main__':
    load_dotenv()
    messages = []
    system = """
    you are a good programmer. your task is to generate code that is efficient,
    performant, well organized. You have to be precise and not add too much verbose comments in the code.
    """

    while True:
        user_text = input("YOU:")
        utils.add_user_message(messages, user_text)
        ai_response = chat.chat_service(messages, system)
        print(f"AI: {ai_response}")
        utils.add_assistant_message(messages, ai_response)
