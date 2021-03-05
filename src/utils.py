import requests

RANDOM_WORD_URL = "https://random-words-api.vercel.app/word"
RANDOM_QUOTE_URL = "https://api.quotable.io/random"

def get_random_word():
    response = requests.get(RANDOM_WORD_URL)
    return response.json()[0]['word']

def get_random_quote():
    response = requests.get(RANDOM_QUOTE_URL)
    return response.json()['content']
