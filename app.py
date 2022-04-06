#app.py
import app0
import app1
import app2
import app3
import app4
import streamlit as st

PAGES = {
    "top": app0,
    "解析データの作成": app1,
    "Stopwordsの設定": app2,
    "頻出単語の可視化": app3,
    "ナレッジグラフの作成": app4
}
st.sidebar.title('Analysis items')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()

