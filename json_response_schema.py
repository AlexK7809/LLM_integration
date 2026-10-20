from google import genai
from google.genai.types import GenerateContentConfig
from pydantic import BaseModel
#Use this to tell llm that this is the outline of the json
class Recipe(BaseModel):
    recipe_name: str
    ingredients: list[str]
    instructions: list[str]

client = genai.Client()

response = client.models.generate_content(
    model='gemini-3.8-flash',
    contents="""I have leftover chicken, cheese and broccoli. Suggest one recipe""",
    config=GenerateContentConfig(
        system_instruction='include US and metric units',
        response_mime_type='application/json',
        response_schema=Recipe
    )
)
print(response.text)
recipe = response.parsed # recipe object
print(recipe.recipe_name)

for ingredient in recipe.ingredients:
    print(ingredient)
for step in recipe.instructions:
    print(step)