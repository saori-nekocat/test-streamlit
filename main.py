import streamlit as st
from PIL import Image

st.title('Streamlit 超入門')

st.write('Data Image')

img = Image.open('IMG_438922.jpg')

st.image(img, caption='KKimage', use_column_width=True)

#use_column_width 実際の横幅に合わせてくれる