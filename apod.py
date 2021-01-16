import requests
import json
import os
import datetime

def get_data(api_key="DEMO_KEY"):
    raw_response = requests.get(f'https://api.nasa.gov/planetary/apod?api_key={api_key}').text
    response = json.loads(raw_response)
    return response

def get_picture_url():
    return get_data()['url']

def dir_check(dir_name):
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

def download_image_and_explanation():
    today = datetime.date.today()
    dir_check('apod')
    if os.path.isfile(f'apod/{today}.png') == False:
        data = get_data()
        url = data['url']
        raw_image = requests.get(url).content
        explanation = data['explanation']
        with open(f'apod/{today}.png', 'wb') as file:
            file.write(raw_image)
        with open(f'apod/{today}.txt', 'w') as file:
            file.write(explanation)
    return today

def get_picture():
    return "apod/"+str(download_image_and_explanation())+".png"

def get_explanation():
    return "apod/"+str(download_image_and_explanation())+".txt"

