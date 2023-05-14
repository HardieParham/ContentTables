# Standard imports
import logging

# External Imports
import googletrans

# Local Imports
from app.data import data, char_to_replace



"""
Base Class for handling Text phrases.

NOTE:
Google Translate is blocked by TME.
"""

class Translator():
    def __init__(self, src, dest):
        self.trans = googletrans.Translator()
        self.src = src
        self.dest = dest


    def translate(self, text):
        try:
            # There a few characters allowed in excel that break Google Translate's API
            # So first, need to remove any instances of these, and replace with a space
            for key, value in char_to_replace.items():
                new_text = text.replace(key, value)

            translation = self.trans.translate(text=new_text, dest=self.dest, src=self.src)
            return translation.text
        
        except:
            logging.warning(f'Translation failed for {text}')

