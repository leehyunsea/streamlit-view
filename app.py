import streamlit as st
view = [150,100,50]
st.write('# 경기서부액세스운용센터 소모용품 쇼핑몰')
st.write('## 10G 모듈')
view
st.write('## bar chart')
st.bar_chart(view)

import pandas as pd
sview = pd.Series(view)
sview