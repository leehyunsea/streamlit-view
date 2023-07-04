import streamlit as st

st.write('# 경기서부A센터 소모용품 쇼핑몰')
st.write('## 소모용품 재고파악을 위한 웹사이트입니다.')
st.write('## 다양한 물건의 재고를 확인해보세요')
img_url = 'https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMjAxMTBfMTcx%2FMDAxNjQxNzgwMDU0NTY5.OJMgmEy7VjYhIS_hekPQy2UsVFBPc7qPNzIxcu2wJsIg.w6akJNkeRVlv5_61H4VOin4EJYQ-x0MOxf1dE-4vMj0g.PNG.whgusrb8989%2F%25B5%25B5%25C1%25F6.png&type=sc960_832'
st.image(img_url)

with st.sidebar:
    choice = option_menu("Menu", ["페이지1", "페이지2", "페이지3"],
                         icons=['house', 'kanban', 'bi bi-robot'],
                         menu_icon="app-indicator", default_index=0,
                         styles={
        "container": {"padding": "4!important", "background-color": "#fafafa"},
        "icon": {"color": "black", "font-size": "25px"},
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#fafafa"},
        "nav-link-selected": {"background-color": "#08c7b4"},
    }
    )
