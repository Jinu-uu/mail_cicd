import streamlit as st
from datetime import datetime

age = st.slider('나이는?', 0, 100, 25)  # 0, 100 : 입력허용 구간 / 25 : 최초 세팅 값
st.write('나는 ',age,'살')

# 날짜 구간
slider_date = st.slider(
    '날짜 구간 선택하세요',
    datetime(2023,1,1), datetime(2023,12,31),
    value=(datetime(2023,10,1), datetime(2023,10,31)),
    format='YY/MM/DD')
st.write('slider date :', slider_date)