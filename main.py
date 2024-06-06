import pathlib
import textwrap

import google.generativeai as genai
from IPython.display import Markdown

from IPython.display import display


def to_markdown(text):
    text = text.replace('•', '  *')
    return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))
