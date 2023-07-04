import streamlit as st
view = [150,100,50]
st.write('# 췌테이얌')
st.write('## 와꾸순위')
view
st.write('## bar chart')
st.bar_chart(view)

import pandas as pd
sview = pd.Series(view)
sview