from dotenv import load_dotenv
from utils import utils
from service import chat

if __name__ == '__main__':
    load_dotenv()
    messages = []

    while True:
        user_text = input("YOU:")
        utils.add_user_message(messages, user_text)
        ai_response = chat.chat_service(messages,None, 0.0)
        print(f"AI: {ai_response}")
        utils.add_assistant_message(messages, ai_response)
