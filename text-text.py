import pathlib
import textwrap
from dotenv import load_dotenv
import google.generativeai as genai
from IPython.display import Markdown
import os

from IPython.display import display

load_dotenv()

GOOGLE_API_KEY=os.getenv('API_KEY')

genai.configure(api_key=GOOGLE_API_KEY)
# Path: main.py

def to_markdown(text):
    text = text.replace('•', '  *')
    return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

model = genai.GenerativeModel('gemini-1.5-flash')
response = model.generate_content("What is the meaning of life?", stream=True)

for chunk in response:
  print(chunk.text)
  print("_"*80)