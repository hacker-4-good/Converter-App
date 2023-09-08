import streamlit as st
import pandas as pd
import numpy as np


imageList = [
    'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.GyxUgOOyXbk3dsnM79il0AHaEK%26pid%3DApi%26h%3D160&f=1&ipt=b187a2957235e297fb27144e3dccb8b61cd111b4a86576d4e18663faa12720c5&ipo=images',
    'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.8bOtZeJyiE03WEm-67vqTQHaFu%26pid%3DApi%26h%3D160&f=1&ipt=0e21f195d321784b9b9fd025f55ce37a9a4075d66b6258f7d939b22ca28cd0cc&ipo=images',
    'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi.ytimg.com%2Fvi%2FyT-RtaEDXxY%2Fmaxresdefault.jpg&f=1&nofb=1&ipt=e9a54434d63f18c002b02e475ee792ee9c5ac3bba8d988474b7de9eac1dc205d&ipo=images'
]

if 'stage' not in st.session_state:
    st.session_state.stage = 0

def set_state(i):
    st.session_state.stage = i

@st.cache_resource
def create_list():
    l = []
    return l

arr = create_list()

if st.session_state.stage < len(imageList):
    st.image(imageList[st.session_state.stage])
    ans = st.slider('Rate the picture', min_value=0, max_value=10, on_change=set_state, args=[st.session_state.stage])
    if st.button('Next', on_click=set_state, args=[st.session_state.stage+1]):
        arr.append([ans, st.session_state.stage-1])

if st.session_state.stage == len(imageList):
    st.text('empty')

st.write(arr)

count = 0
if st.button('Save') and count==0:
    if st.session_state.stage==(len(imageList)-1) and count==0:
        count += 1
        narray = np.array(arr)
        df = pd.DataFrame(arr, columns=['Rate','Image'])
        df.to_csv('rate.csv', mode='a', index=False, header=False)
    else:
        st.error('Too early pressing')

if st.button('Clear History'):
    st.cache_resource.clear()