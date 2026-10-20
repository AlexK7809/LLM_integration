from google import genai

client = genai.Client()
# One shot is where we provide one example # Zero shot is no examples # few is a couple these are meant to guide the LLM
response = client.models.generate_content(
    model='gemini-3.8-flash',
    contents="""We are a business selling logging and monitoring products what are good products to give away at out booth at pycon?
    last year we gave away tote bags and they were very popular and met our budget and they year before that we gave away pens but not popular"""
)
print(response.text)