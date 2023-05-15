# Standard imports
import logging

# External Imports
from googletrans import Translator

# Local Imports
from app.data import data, char_to_replace



"""
Base Class for handling translation phrases.

NOTE:
Google Translate is blocked by TME.
"""

def translate(text: str) -> str:
    try:
        # There a few characters allowed in excel that break Google Translate's API
        # So first, need to remove any instances of these, and replace with a space
        for key, value in char_to_replace.items():
            new_text = text.replace(key, value)


        translator = Translator()
        translation = translator.translate(text=new_text, dest=data['dest'], src=data['src'])

        return translation.text
    
    except:
        logging.warning(f'Translation failed for {text}')

