import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 超入門')
st.write('プログレスバーの表示')
'Start'

latest_iteratin = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteratin.text(f'Interation {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

st.sidebar.write('Display Image')
if st.sidebar.checkbox('Show Image'):
    img = Image.open('FIREFINE.png')
    st.image(img, caption='FIREFINE', use_column_width=True)

left_column, right_column = st.beta_columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここが右カラム')

expander = st.beta_expander('問い合せ')
expander.write('問い合わせ内容を書く')