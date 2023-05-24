import logging

from googletrans import Translator

char_to_replace = {
    '_': ' ',
    '/': ' ',
    '・': ' ',
    'ｰ': ' ',
    '･' : ' ' ,
    'ｰ' : ' ',
    '･': ' ',
    '･': ' ',
    '*': ' ',
    '[': ' ',
    ']': ' ',
    '?': ' ',
    }


def translate(text: str, src: str, dest:str) -> str:
    """
    Base function for handling translation phrases.

    NOTE:
    Google Translate is blocked by TME.
    """  
    try:
        # There a few characters allowed in excel that break Google Translate's API
        # So first, need to remove any instances of these, and replace with a space
        for key, value in char_to_replace.items():
            new_text = text.replace(key, value)


        translator = Translator()
        translation = translator.translate(text=new_text, dest=dest, src=src)

        return translation.text
    
    except:
        logging.warning(f'Translation failed for {text}')
