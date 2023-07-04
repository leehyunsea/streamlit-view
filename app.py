import streamlit as st

st.write('# 경기서부A센터 소모용품 쇼핑몰')
st.write('## 소모용품 재고파악을 위한 웹사이트입니다.')
st.write('## 다양한 물건의 재고를 확인해보세요')
img_url = 'https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMjAxMTBfMTcx%2FMDAxNjQxNzgwMDU0NTY5.OJMgmEy7VjYhIS_hekPQy2UsVFBPc7qPNzIxcu2wJsIg.w6akJNkeRVlv5_61H4VOin4EJYQ-x0MOxf1dE-4vMj0g.PNG.whgusrb8989%2F%25B5%25B5%25C1%25F6.png&type=sc960_832'
st.image(img_url)

st.sidebar.title('# 종류')

st.sidebar.title('1. 10G 모듈')
st.sidebar.button('15km')
st.sidebar.button('40km')
st.sidebar.button('80km')
st.sidebar.title('2. 2.5G 모듈')
st.sidebar.title('3. ')
st.sidebar.title('4. ')
st.sidebar.title('5. ')
