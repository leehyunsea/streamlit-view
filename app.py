import streamlit as st
import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as html
from  PIL import Image
import numpy as np
import pandas as pd
import plotly.express as px
import io

st.write('# 경기서부A센터 소모용품 쇼핑몰')
st.write('## 소모용품 재고파악을 위한 웹사이트입니다.')
st.write('## 다양한 물건의 재고를 확인해보세요')
img_url = 'https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMjAxMTBfMTcx%2FMDAxNjQxNzgwMDU0NTY5.OJMgmEy7VjYhIS_hekPQy2UsVFBPc7qPNzIxcu2wJsIg.w6akJNkeRVlv5_61H4VOin4EJYQ-x0MOxf1dE-4vMj0g.PNG.whgusrb8989%2F%25B5%25B5%25C1%25F6.png&type=sc960_832'
st.image(img_url)

st.sidebar.title('# 종류')
with st.sidebar:
    choose = option_menu("App Gallery", ["About", "Photo Editing", "Project Planning"],
                         icons=['house', 'camera fill', 'kanban'],
                         menu_icon="app-indicator", default_index=0,
                         styles={
        "container": {"padding": "5!important", "background-color": "#fafafa"},
        "icon": {"color": "orange", "font-size": "25px"}, 
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#02ab21"},
    }
    )