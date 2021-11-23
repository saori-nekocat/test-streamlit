from numpy import right_shift
import streamlit as st
import pandas as pd
from PIL import Image
import graphviz as graphviz

st.title('かわいい猫')
st.balloons()

col1, col2 = st.columns(2)

with col1:
    st.header("Kitten Photo")
    img = Image.open('IMG_438922.jpg')
    st.image(img, caption='子供の頃のクリスティ')
with col2:
    st.header("Photo Download")
    with open("IMG_438922.jpg", "rb") as file:
        btn = st.download_button(
                label="Download image",
                data=file,
                file_name="IMG_438922.jpg",
                mime="image/png"
            )

df = pd.DataFrame({
    'dami': [2500, 3000, 3500, 4000, 4500, 5000, 4500],
    'wari': [1500, 2000, 2500, 3300, 5500, 6000, 6500]
})

df.index = ['2019-12', '2020-02','2020-05','2020-09','2021-01','2021-06','2021-11']


st.write('Changes in his weight')
st.line_chart(data = df)

#use_column_width 実際の横幅に合わせてくれる


# Create a graphlib graph object
graph = graphviz.Digraph()
graph.edge('saori', 'damie')
graph.edge('saori', 'warith')
graph.edge('damie', 'gohan')
graph.edge('warith', 'oyatsu')
graph.edge('gohan', 'white')
graph.edge('damie', 'blue')
graph.edge('warith', 'white')
graph.edge('gohan', 'brown')
graph.edge('blue', 'gohan')
graph.edge('saori', 'chu-ru')
graph.edge('oyatsu', 'chu-ru')

st.graphviz_chart(graph)