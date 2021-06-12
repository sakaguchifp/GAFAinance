import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('Streamlit 超入門')

st.write('Display Image')
if st.checkbox('Show Image'):
    img = Image.open('FIREFINE.png')
    st.image(img, caption='FIREFINE', use_column_width=True)

option = st.selectbox(
    'あなたの好きな数字は？',
    list(range(1, 11))
)
'あなたの好きな数字は', option, ' です。'

hobby = st.text_input('あなたの趣味を教えてください。')
'あなたの趣味は', hobby,  ' です。'

condition =st.slider('あなたの今の調子は？', 0 ,100, 50)
'あなたのコンディションは', condition,  ' です。'