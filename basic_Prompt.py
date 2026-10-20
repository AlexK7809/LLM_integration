from google import genai
import rich
from rich.markdown import Markdown

client = genai.Client()

response = client.models.generate_content(
    model='gemini-3.8-flash',
    contents='Why is the sky blue? Can you explain in simple terms?'
)
rich.print(Markdown(response.text))
print(response.usage_metadata)