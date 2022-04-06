import streamlit as st
import pandas as pd

def app():
   st.title('解析データの作成')
   st.write('1) データのアップロード')
    
   #ファイルの読み込み
   file = st.file_uploader("Upload file", type=['csv'])
   if file:
      text = pd.read_csv(file, encoding = 'utf-8')
      st.dataframe(text, width = 1000)
      
      st.text('\n')
      st.text('\n')
      st.text('\n')
      #解析する列の指定
      st.write('2) 解析する項目の指定')
      columns = text.columns
      column = st.selectbox('解析する項目(列)を選択してください.', columns)
      
      #解析する項目だけのdfの表示
      df_select = text.loc[:,column]
      st.dataframe(df_select, width = 2000)
      
      st.text('\n')
      st.text('\n')      
      #解析開始ボタン
      clicked = st.button('解析データ作成')
      if clicked:
         #テキストの形式整理
         text_abstract = [str(i) for i in text.loc[:,column].to_list() if i != 'nan']
         text_abstract = ' '.join(text_abstract).split('. ')
         text_abstract = [i.split() for i in text_abstract]

         #不用語(stop words)の削除
         #sklearn.feature_extractionおよびnltk.corpus.stopwordsの不用語を検討
         f = open('stop_words.txt','r', encoding = 'utf-8')
         stop_words = f.read()
         f.close()

         stop_words = eval(stop_words)

         text_abstract_ = []

         for i in range(len(text_abstract)):
            text_ = []
            for n in range(len(text_abstract[i])):
                  word = text_abstract[i][n].lower()
                  c = 0
                  for j in stop_words:
                     if word != j:
                        c += 1
                  if c == len(stop_words):          
                     text_.append(word)
            text_abstract_.append(text_)

         #入力ファイルの作成
         text_abstract_nl = []
         for i in range(len(text_abstract_)):
            string = ' '.join(text_abstract_[i])
            text_abstract_nl.append(string)
         text_abstract_nl2 = []
         for i in text_abstract_nl:
            text_abstract_nl2.append(str(i))
         df = pd.DataFrame(text_abstract_nl, columns = ['words'])
         df.to_csv('df.csv', encoding = 'utf-8')

         st.write('解析データを作成しました.')
         st.header('⇒左タブ"Stopwordsの設定"へ')