import requests
import json
import os

def get_data():
    raw_image = requests.get(f'https://thispersondoesnotexist.com/image').content
    dir_check("images")
    with open(f'images/image.png', 'wb') as file:
            file.write(raw_image)

def dir_check(dir_name):
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

def get_tpdne_picture():
    get_data()
    return "images/image.png"
