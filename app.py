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

delete = st.srider.button('Data delete')
if delete:
    os.remove('df.csv')
    os.remone('df_stopwords.csv')

page = PAGES[selection]
page.app()


