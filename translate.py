import requests
import json

def get_data(message, target="en"):
    url = "https://google-translate1.p.rapidapi.com/language/translate/v2"
    formatted_message = message.replace(' ','%20')
    payload = f"q={formatted_message}&target={target}"
    with open('keys/RapidAPIKey.txt') as api_key:
        api_key = api_key.read()
    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'accept-encoding': "application/gzip",
        'x-rapidapi-key': api_key,
        'x-rapidapi-host': "google-translate1.p.rapidapi.com"
        }
    raw_response = requests.request("POST", url, data=payload, headers=headers)
    response = json.loads(raw_response.text)
    try:
        out = response['data']['translations'][0]['translatedText']
    except:
        try:
            out = "ERROR : " + response['error']['message']
        except:
            out = "ERROR : Unexpected error" 
    return out

def get_translate(message, target="en"):
    return get_data(message, target)
