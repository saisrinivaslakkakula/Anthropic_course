from anthropic import Anthropic
from dotenv import load_dotenv
'''
NOTES:
System: a system prompt can be passed to the chat function if necessary. Example coud be, 
you are an intelligent math tutor helping a 5th grader kid. Do not give solution right away, instead help 
them to understand and encourage them into solving the problem on their own.

Temperature:

A very important concept in case of LLMs. As we know, LLMs tokenize the txt, mark them with embeddings,
process them with a layer of attention heads and then predict the next word based on the probability distribution

Now, the temperature parameter is used to adjust the probability of next word pic

lower the temperature, picks the most probable word, 
higher the temp pics, the word of more lineament choice
Not essentially it pics the lower probability word in case of high temperature. just that it pics 
lenient probable word

use cases could be,
if we want factual info, coding assistant, data extraction etc, we prefer lower temp.

if we have tasks like summarization, grammar correction etc, we prefer medium temp

if we have more creative tasks like brain storming, idea generation, or joke generation we prefer higher temp.

temperature value is a decimal value ranging from 0-1 (similar to probability)

Need consistent, factual responses? Use low temperature
Want creative brainstorming? Dial up the temperature
Somewhere in between? Medium temperatures work well for most general tasks

Lecture link: https://anthropic.skilljar.com/claude-with-the-anthropic-api/287728

Streaming:
There comes a scenario when we are building a real world chat bot application where in an user asks for a query,
the model takes time to generate text and send back the response to the client.

We could add a loder until the whole generation happns. But that may not be a right UX.

Instead, UX would be better if the generation looks seamless and continuous. For that purpose, we have something called streaming
in Anthropic SDK. streaming API returns events in chunks. Notable event types are ,
MessageStart - A new message is being sent
ContentBlockStart - Start of a new block containing text, tool use, or other content
ContentBlockDelta - Chunks of the actual generated text
ContentBlockStop - The current content block has been completed
MessageDelta - The current message is complete
MessageStop - End of information about the current message

The actual text streaming events we concentrate more on is `ContentBlockDelta`. We keep streaming and receive
the message content blocks and display them in almost real time seamless way.

To understand this concept better, we have written a new service method called chat_service_with_stream.
This service returns back a streaming event of the content. which then streamed using python code and displayed the chunks
as they become available. 

lecture: https://anthropic.skilljar.com/claude-with-the-anthropic-api/287734
'''

load_dotenv()
client = Anthropic()
model = "claude-sonnet-4-0"


def chat_service(messages, system=None, temperature=1.0):
    params = {
        "model": model,
        "max_tokens": 1000,
        "messages": messages,
        "temperature": temperature
    }

    if system:
        params["system"] = system
    message = client.messages.create(**params)
    return message.content[0].text


def chat_service_with_stream(messages):
    params = {
        "model": model,
        "max_tokens": 1000,
        "messages": messages,
    }
    return client.messages.stream(**params)
