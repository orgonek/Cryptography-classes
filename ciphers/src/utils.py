import requests
from enchant.checker import SpellChecker

RANDOM_WORD_URL = "https://random-word-api.herokuapp.com/word?number=1"
RANDOM_QUOTE_URL = "https://api.quotable.io/random"

def get_random_word():
    response = requests.get(RANDOM_WORD_URL)
    return response.json()[0]

def get_random_quote():
    response = requests.get(RANDOM_QUOTE_URL)
    return response.json()['content']

def count_errors(word):
    """ Counts the number of errors, in the sentence """
    chkr = SpellChecker("en")
    chkr.set_text(word)

    count = 0
    for _err in chkr:
        count += 1
    
    return count
