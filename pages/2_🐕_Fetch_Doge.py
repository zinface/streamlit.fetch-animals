import streamlit as st
import requests
import json
from PIL import Image
import io
import time
st.title('Fetch Doge')


st.button('获取狗只')

def getImageLink():
    content = requests.get('https://dog.ceo/api/breeds/image/random').content.decode()
    return json.loads(content)['message']

def getImage(url):
    return requests.get(url).content

def getImageBytesIO():
    container = io.BytesIO()
    container.write(getImage(getImageLink()))
    return container

loading_bar = st.progress(0.0, '加载中')
time.sleep(0.1)
loading_bar.progress(0.1, '加载中')
image = getImageBytesIO()
loading_bar.progress(1.0, '加载完成')
time.sleep(0.1)
loading_bar.image(image)