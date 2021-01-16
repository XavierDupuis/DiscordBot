import requests
import json

def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    quote = json.loads(response.text)[0]['q']
    author = json.loads(response.text)[0]['a']
    return quote + " - " + author