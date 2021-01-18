import requests
import json
import os

def get_data(image_url):
    with open('keys/RapidAPIKey.txt') as api_key:
        api_key = api_key.read()
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
    lines = data['regions'][0]['lines']
    line_index = 0
    word_index = 0
    while(True):
        try:
            line = lines[line_index]
            while(True):
                try:
                    out += line['words'][word_index]['text'] + " "
                    word_index += 1
                except:
                    word_index = 0
                    break
            line_index += 1
        except:
            line_index = 0
            break
    return out
