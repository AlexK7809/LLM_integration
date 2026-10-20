from google import genai
import rich
from rich.markdown import Markdown

client = genai.Client()
chat = client.chats.create(model='gemini-3.8-flash')

while True:
    prompt = input('Enter your message:')
    response = chat.send_message(prompt + ' Answer in a short sentence.')



    rich.print(Markdown(response.text))
    print(response.usage_metadata.total_token_count)