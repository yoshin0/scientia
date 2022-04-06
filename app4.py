import streamlit as st
import pandas as pd
import nlplot
import os
import streamlit.components.v1 as components
import re
from PIL import Image
import datetime


def app():
    ico = Image.open('icon.png')
    st.image(ico)
    st.header('ナレッジグラフの可視化')
    
    #解析データとstopwordsの有無の確認
    exist = os.path.isfile('df.csv')
    exist_s = os.path.isfile('df_stopwords.csv') 
    if exist != True:
        st.header('解析データを作成してください.')
    elif exist_s != True:
        st.header('Stopwordsを指定してください.')
    elif exist != True and exist_s != True:
        st.header('解析データを作成してください.')
        st.header('Stopwordsを指定してください.')    
    else:
        #解析データの読み込み
        df = pd.read_csv('df.csv', encoding = 'utf-8')
        #テキストデータの指定
        npt = nlplot.NLPlot(df, target_col='words')
        #stopwordsの読み込み
        stopwords_ = pd.read_csv('df_stopwords.csv', encoding = 'utf-8')
        stopwords = list(stopwords_.iloc[:,1])

        st.write('1) ナレッジグラフ')
        st.text('\n')
        
        #初期値の読み込み
        Html_nFile = open("hist_n.html", 'r', encoding='utf-8')
        source_code = Html_nFile.read()
        n = re.findall(r'(?<=\"text\":\[).+?(?=\.)', source_code)
        if n ==[]:
            n = re.findall(r'(?<=\"text\": \[).+?(?=\.)', source_code)
            n = int(n[0])
        n = int(n[0])
        
        set_num= st.number_input('関連度を指定してください.', min_value=10, max_value=1000, value=n, step=1,
                                 help = '関連度が大きいとグラフが作成できません.小さいと作成に時間がかかります.')
        get_kg = st.button('ナレッジグラフを作成する')
        st.text('\n')
        
        if get_kg:
            dt_now = datetime.datetime.now().date()            
            npt.build_graph(stopwords=stopwords, min_edge_frequency=set_num)
            net = npt.co_network(title='Co-occurrence network', save = True, width=700, height=500)
            CoFile = open(str(dt_now) + "_Co-occurrence network.html", 'r', encoding='utf-8')
            Co_source_code = CoFile.read() 
            components.html(Co_source_code, height = 500)
            btn = st.download_button(label="Download html", data=CoFile, file_name = str(dt_now) + "_Co-occurrence network.html", mime="text/html")

            st.write('2) クラス分類')
            st.text('\n')
            sun = npt.sunburst(title='All sentiment sunburst chart', colorscale=True,
                color_continuous_scale='Oryel', width=780, height=550)

            sun.write_html("sun.html")
            SunFile = open("sun.html", 'r', encoding='utf-8')
            source_code = SunFile.read() 
            components.html(source_code, height = 600)
            
            
            
            
            
            
            
            
   
