import random
from os import listdir, path

import requests
from faker import Faker

fake = Faker()
CREDENTIALS = {
    'username': 'Admin',
    'password': '12345'
}

# HOST = 'http://localhost:5000/'
HOST = "http://95.213.199.248/"


def create_user(s):
    url = HOST + 'signup'
    payload = CREDENTIALS
    s.post(url, data=payload)


def login_user(s):
    url = HOST + 'login'
    payload = CREDENTIALS
    s.post(url, data=payload)


def load_images(s):
    base_dir = "images"
    url = HOST + 'image/new'
    filepaths = listdir(base_dir)
    for i in range(0, 9):
        files = {'file': open(path.join(base_dir, filepaths[i % len(filepaths)]), 'rb')}
        s.post(url, files=files)


def get_image_ids(s):
    url = HOST + 'image/list'
    images = s.get(url).json()
    return [image['id'] for image in images]


def create_comment(s, image_id):
    url = HOST + 'comment/new'
    for i in range(random.randrange(5, 10)):
        comment = s.post(url, data={
            'image_id': image_id,
            'text': fake.text(),
        })


def create_comments(s):
    image_ids = get_image_ids(s)
    for image_id in image_ids:
        create_comment(s, image_id)


if __name__ == '__main__':
    s = requests.session()
    create_user(s)
    login_user(s)
    load_images(s)
    create_comments(s)
