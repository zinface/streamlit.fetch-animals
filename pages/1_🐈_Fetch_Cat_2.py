import streamlit as st
import requests
import json
from PIL import Image
import io
import time
st.title('Fetch CAT')


st.button('获取 CAT')

def getImageLink():
    '''
    {
        "code": 200,
        "msg": "获取成功",
        "imgurl": "https://cdn2.thecatapi.com/images/aaq.jpg",
        "api_source": "官方API网:https://api.pearktrue.cn/"
    }
    '''
    content = requests.get('https://api.pearktrue.cn/api/animal/index.php?type=json&anime=bird').content.decode()
    return json.loads(content)['imgurl']

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