from utils import utils
from service import chat


def example_structure_data(messages):
    '''
    NOTES:
        When you need Claude to generate structured data like JSON, Python code,
        or bulleted lists, you'll often run into a common problem: Claude wants to be helpful
        and add explanatory text around your content. While this is usually great,
        sometimes you need just the raw data with nothing else.

        Consider building a web app that generates AWS EventBridge rules.
        Users enter a description, click generate, and expect to see clean JSON they can
        immediately copy and use. If Claude returns the JSON wrapped in markdown code blocks
        with explanatory text, users can't simply copy the entire response - they have to manually
         select just the JSON portion.

         The Solution: Assistant Message Prefilling + Stop Sequences.
         We can combine assistant message prefilling with stop sequences
         to get exactly the content you want.

         In this example, we have used ```json as assistant message to provide start context to the next assistant
         generated message and provided ``` as stop sequence to control and print out the exact message
         we wanted.

         Lecture: https://anthropic.skilljar.com/claude-with-the-anthropic-api/287732
    '''
    utils.add_user_message(messages, "Generate event bridge rule for EC2")
    utils.add_assistant_message(messages, "```json")
    response = chat.chat_service(messages, None, 0.0, ["```"])
    print(response)