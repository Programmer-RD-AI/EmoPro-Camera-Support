from picamera import PiCamera
from time import sleep
import time
from PIL import Image
from tqdm import tqdm
from flask import *
import requests
import datetime
from werkzeug.utils import header_property
camera = PiCamera()
camera.start_preview()
for _ in tqdm(range(100)):
    camera.annotate_text = f'{_}'
    camera.capture('test.jpg')
    start_time = [datetime.datetime.now().minute, datetime.datetime.now().second]
    file = {'file': open('./test.jpg', 'rb')}
    requests.get('http://:/hdhf', {'user_name': 'Ranuga', 'name_of_product': 'biscuit','password': 'Ranuga', 'email': 'go2ranuga@gmail.com'}, files=file).json()['result']
    end_time = [datetime.datetime.now().minute, datetime.datetime.now().second]
    print(
        f'\n Mins : {end_time[0]-start_time[0]} \n Secs : {end_time[1]-start_time[1]}')
sleep(5)
camera.capture('test.jpg')
camera.stop_preview()
