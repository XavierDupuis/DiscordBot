import requests
import json
import os
import datetime

def get_data():
    with open('keys/APODkey.txt') as api_key:
        api_key = api_key.read().rstrip()
    raw_response = requests.get(f'https://api.nasa.gov/planetary/apod?api_key={api_key}').text
    response = json.loads(raw_response)
    dir_check("json")
    with open('json/APOD.json','w') as file:
       json.dump(response, file)

def get_picture_hdurl():
    with open('json/APOD.json','r') as file:
        return json.load(file)['hdurl']

def get_picture_url():
    with open('json/APOD.json','r') as file:
        return json.load(file)['url']

def get_picture_explanation():
    with open('json/APOD.json','r') as file:
        return json.load(file)['explanation']

def dir_check(dir_name):
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

def download_image_and_explanation():
    today = datetime.date.today()
    dir_check('apod')
    if os.path.isfile(f'apod/{today}.png') == False:
        data = get_data()
        url = get_picture_url()
        raw_image = requests.get(url).content
        explanation = get_picture_explanation()
        with open(f'apod/{today}.png', 'wb') as file:
            file.write(raw_image)
        with open(f'apod/{today}.txt', 'w') as file:
            file.write(explanation)
    return today

def get_picture():
    return "apod/"+str(download_image_and_explanation())+".png"

def get_explanation():
    return "apod/"+str(download_image_and_explanation())+".txt"

