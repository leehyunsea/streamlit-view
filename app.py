import streamlit as st
view = [150,100,50]
st.write('# Youtue view')
st.write('## chart')
view
st.write('## bar chart')
st.bar_chart(view)

import pandas as pd
sview = pd.Series(view)
sview