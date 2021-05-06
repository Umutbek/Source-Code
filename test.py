import pyrebase
import os
import time
import requests
import json

config = {
'apiKey': "AIzaSyD9n7WYx4TW3ai9yPwJotElIvrLfhNMn2k",
'authDomain': "uigo-2ff4b.firebaseapp.com",
'projectId': "uigo-2ff4b",
'storageBucket': "uigo-2ff4b.appspot.com",
'messagingSenderId': "615940310561",
};

firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
storage = firebase.storage()

allimages = os.listdir('C:/Users/User/Downloads/ОсОО АкбарсАзия/Фото Тынчтык/')

for images in allimages:
    path_on_cloud = images
    storage.child(path_on_cloud).put(images)
    t=1
    img = images.split('.')[0]

    imglarge = 'https://firebasestorage.googleapis.com/v0/b/uigo-2ff4b.appspot.com/o/ProductsUygo%2F'+img+'_1200x1200.png?alt=media'
    imgmedium = 'https://firebasestorage.googleapis.com/v0/b/uigo-2ff4b.appspot.com/o/ProductsUygo%2F'+img+'_500x500.png?alt=media'
    imgsmall = 'https://firebasestorage.googleapis.com/v0/b/uigo-2ff4b.appspot.com/o/ProductsUygo%2F'+img+'_100x100.png?alt=media'

    url = f"http://165.22.93.189/myapps/venv/api/item/updateitem/{img}"
    data = {'imglarge': imglarge, 'imgmedium': imgmedium, 'imgsmall': imgsmall}
    r = requests.patch(url, json=data)
    print(r, data, img)
    time.sleep(t)
