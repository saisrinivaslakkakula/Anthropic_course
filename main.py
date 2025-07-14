from dotenv import load_dotenv
from utils import utils
from service import chat

if __name__ == '__main__':
    load_dotenv()
    messages = []
    system = """
    You are a patient math tutor.
    Do not directly answer a student's questions.
    Guide them to a solution step by step.
    """

    while True:
        user_text = input("YOU:")
        utils.add_user_message(messages, user_text)
        ai_response = chat.chat_service(messages, system)
        print(f"AI: {ai_response}")
        utils.add_assistant_message(messages, ai_response)
