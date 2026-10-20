import sys

from google import genai
from google.genai.types import GenerateContentConfig
import rich
from rich.markdown import Markdown

client = genai.Client()
chat = client.chats.create(model='gemini-3.8-flash')
try:
    with open('chat_system_instruction.txt', 'r') as f:
        system_instruction = f.read()
except:
        print('Missing system instruction')
        sys.exit()
while True:
    question = input('> ')
    response = chat.send_message(
        question,
        config=GenerateContentConfig(
            system_instruction=system_instruction
        )
    )
    rich.print(Markdown(response.text))