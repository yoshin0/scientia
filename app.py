#app.py
import app0
import app1
import app2
import app3
import app4
import streamlit as st
import os

PAGES = {
    "top": app0,
    "解析データの作成": app1,
    "Stopwordsの設定": app2,
    "頻出単語の可視化": app3,
    "ナレッジグラフの作成": app4
}

st.sidebar.title('Please Select')
selection = st.sidebar.radio("Analysis items", list(PAGES.keys()))

delete_data = st.sidebar.button('Delete Data')
if delete_data:
    os.remove('df.csv')
    os.remove('df_stopwords.csv')

page = PAGES[selection]
page.app()


