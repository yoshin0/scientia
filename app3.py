import streamlit as st
import pandas as pd
import nlplot
import os
import streamlit.components.v1 as components


def app():
    st.title('頻出単語の可視化')
    
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

        st.write('1) 出現頻度ヒストグラム')
        st.text('\n')
        
        dis = npt.word_distribution(
        title='number of words distribution',
        xaxis_label='count',
        width=780, height=550)
        dis.write_html("dis.html")
        DisFile = open("dis.html", 'r', encoding='utf-8')
        source_code = DisFile.read() 
        components.html(source_code, height = 550)
        
        st.text('\n')
        st.text('\n')
        st.text('\n')    
        
        st.write('2) 棒グラフ')
        st.text('\n')
        col1, col2 = st.columns(2)
        with col1:
            words = st.number_input('単語数を指定してください.', min_value=1, max_value=5, value=1, step=1)
        with col2:
            num = st.number_input('表示数を指定してください.', min_value=10, max_value=50, value=30, step=10)
                
        hist = npt.bar_ngram(title='uni-gram', xaxis_label='word_count', yaxis_label='word', ngram=words, top_n=num, stopwords=stopwords, width=750, height=1000)
        hist.write_html("hist.html")
        HtmlFile = open("hist.html", 'r', encoding='utf-8')
        source_code = HtmlFile.read() 
        components.html(source_code, height= 1000)        
        
        ##ナレッジグラフの初期設定値抽出
        #頻出トップ500番目の出現回数
        hist_n = npt.bar_ngram(ngram = 1, top_n = 500)
        hist_n.write_html("hist_n.html")
        
        
