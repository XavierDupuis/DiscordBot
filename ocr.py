import requests
import json
import os

def get_data(image_url):
    with open('keys/RapidAPIKey.txt') as api_key:
        api_key = api_key.read().rstrip()
    url = "https://microsoft-computer-vision3.p.rapidapi.com/ocr"
    querystring = {"detectOrientation":"true","language":"unk"}
    payload = "{\r \"url\": \"" + image_url + "\" \r }"
    headers = {
        'content-type': "application/json",
        'x-rapidapi-key': api_key,
        'x-rapidapi-host': "microsoft-computer-vision3.p.rapidapi.com"
        }
    raw_response = requests.request("POST", url, data=payload, headers=headers, params=querystring)
    #print(raw_response)
    response = json.loads(raw_response.text)
    dir_check("json")
    with open('json/OCR.json','w') as file:
       json.dump(response, file)
    raw_image = requests.get(image_url).content
    dir_check("images")
    with open(f'images/ocr.png', 'wb') as file:
            file.write(raw_image)

def dir_check(dir_name):
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

def get_ocr_text(image_url):
    get_data(image_url)
    with open('json/OCR.json','r') as file:
        data = json.load(file)
    try:
        out = data['language'] + " : "
    except:
        return "Invalide image URL"
    if data['language'] == "unk":
        return "No text found in image"

    for region in data['regions']:
        out += "\n"
        for line in region['lines']:
            for word in line['words']:
                out += word['text'] + " "

    return out
