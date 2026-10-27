from google import genai
from google.genai import types

client = genai.Client()

with open('F1TEST.jpg', 'rb') as f:
    image_bytes = f.read()
response = client.models.generate_content(
    model='gemini-3.8-flash',
    contents=[
        types.Part.from_bytes(data=image_bytes, mime_type='image/jpg'),
        'What is this a picture of?'

    ]
)
print(response.text)
