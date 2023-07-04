import streamlit as st
view = [3,2,1]
st.write('# 경기서부A센터 소모용품 쇼핑몰')
st.write('## 10G 모듈')
view
st.write('## bar chart')
st.bar_chart(view)

import pandas as pd
sview = pd.Series(view)
sview

st.sidebar.title('종류')
st.sidebar.checkbox('10G 모듈')