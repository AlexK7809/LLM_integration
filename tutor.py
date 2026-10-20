from google import genai
from google.genai.types import GenerateContentConfig
import rich
from rich.markdown import Markdown

client = genai.Client()
chat = client.chats.create(model='gemini-3.8-flash')
while True:
    question = input('Enter a message for the tutor: ')
    response = chat.send_message(
        question,
        config=GenerateContentConfig(
            system_instruction="""You are a helpful programming tutor for Java programming students 
            You can explain concepts and programs but dont give the user the answers. If the user asks for code ask them 
            questions and explain concepts to help them write it themselves. Be Positive and Encouraging at all times"""
        )
    )
    rich.print(Markdown(response.text))