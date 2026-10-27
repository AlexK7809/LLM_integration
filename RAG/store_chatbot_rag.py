import sys
from google import genai
from google.genai import types
from google.genai.types import GenerateContentConfig
import rich
from rich.markdown import Markdown
import os
import chromadb
from chromadb import Documents, EmbeddingFunction, Embeddings
import pandas
client = genai.Client()

class GeminiEmbeddingFunction(EmbeddingFunction):
    document_mode = True # True = generate embeddings, False = Searching for embeddings in db

    def __call__(self, input: Documents):
        if self.document_mode:
            embedding_task = 'retrieval_document'
        else:
            embedding_task = 'retrieval_query'
        response = client.models.embed_content(
            model='gemini-embedding-001',
            contents=input,
            config=types.EmbedContentConfig(
                task_type=embedding_task
            )

        )

        return [e.values for e in response.embeddings]  #list comprehension

embed_function = GeminiEmbeddingFunction()
embed_function.document_mode = True

chroma_client = chromadb.PersistentClient()
db = chroma_client.get_or_create_collection(name='zoomies_clothes', embedding_function=embed_function)
with open('zoomies_products.csv', 'r') as file:
    clothing_data = pandas.read_csv(file)
    ids = list(clothing_data.style_code)
    documents = list(clothing_data.description)
db.upsert(
    ids=ids,
    documents=documents
)

embed_function.document_mode = False # query the database

#query = 'Can you suggest lightweight yoga pants'
#result = db.query(query_texts=[query], n_results=5) # how man results to return
#[all_items] = result ['documents']
#print(all_items)


chat = client.chats.create(model='gemini-3.8-flash')
try:
    with open('chat_system_instruction.txt', 'r') as f:
        system_instruction = f.read()
except:
        print('Missing system instruction')
        sys.exit()
while True:
    question = input('> ')
    result = db.query(query_texts=[question], n_results=5) # how man results to return
    [all_items] = result ['documents']
    print(all_items)

    prompt_with_rag = f"""The user has the following question
    USER_QUESTION: {question}
    
    Here is the information from the product database that may help the user's question.
    """
    for item in all_items:
        item_one_line = item.replace('\n', '')
        prompt_with_rag += f"""PRODUCT: {item_one_line}"""
    print(prompt_with_rag)
    response = chat.send_message(
        prompt_with_rag,
        config=GenerateContentConfig(
            system_instruction=system_instruction
        )
    )
    rich.print(Markdown(response.text))