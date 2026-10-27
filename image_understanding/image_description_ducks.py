from google import genai
from google.genai import types
from google.genai.types import GenerateContentConfig
from pydantic import BaseModel

client = genai.Client()
class Ducks(BaseModel):
    name: str
    color: str
    species: str

with open('pexels-atilla-kurt-1040808608-40146076.jpg', 'rb') as f:
    image_bytes = f.read()
response = client.models.generate_content(
    model='gemini-3.6-flash',
    contents=[
        types.Part.from_bytes(data=image_bytes, mime_type='image/jpg'),
        'Give the ducks in this picture creative names and what color are they / species'

    ],
    config=GenerateContentConfig(
        response_mime_type='application/json',
        response_schema=list[Ducks]
    )
)
print(response.parsed)
for duck in response.parsed:
    print(duck.name)
