from anthropic import Anthropic

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
'''


def chat_service(messages, system=None, temperature=1.0):
    client = Anthropic()
    model = "claude-sonnet-4-0"
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
