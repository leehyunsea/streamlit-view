import streamlit as st
from PIL import Image

st.write('# 경기서부A센터 소모용품 쇼핑몰')
st.write('## 소모용품 재고파악을 위한 웹사이트입니다.')
st.write('## 다양한 물건의 재고를 확인해보세요')
img = Image.open('siba.png')
img.show()

st.sidebar.title('# 종류')
st.sidebar.title('1. 10G 모듈')
st.sidebar.checkbox('15KM')
st.sidebar.checkbox('40KM')
st.sidebar.checkbox('80KM')
st.sidebar.title('2. ')
st.sidebar.title('3. ')
st.sidebar.title('4. ')
st.sidebar.title('5. ')
