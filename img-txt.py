import pathlib
import textwrap
import PIL.Image
from dotenv import load_dotenv
import google.generativeai as genai
from IPython.display import Markdown
import os
from IPython.display import display

load_dotenv()

GOOGLE_API_KEY=os.getenv('API_KEY')

genai.configure(api_key=GOOGLE_API_KEY)

def to_markdown(text):
    text = text.replace('•', '  *')
    return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

img = PIL.Image.open('img.png')

model = genai.GenerativeModel('gemini-1.5-flash')

response = model.generate_content(["What is present in that image", img], stream=True)
response.resolve()

to_markdown(response.text)