import streamlit as st
import numpy as np
import pandas as pd
import nlplot
import os
import datetime
from PIL import Image

def app():    
    def main():
        ico = Image.open('icon.png')
        st.image(ico)
        st.header('Stopwordsの設定')   
        #解析データの有無を確認
        exist = os.path.isfile('df.csv')
        if exist != True:
            st.header('解析データを作成してください.')
        else:
            #解析データの読み込み
            df = pd.read_csv('df.csv', encoding = 'utf-8')
            #テキストデータの指定
            npt = nlplot.NLPlot(df, target_col='words')
            
            st.write('1) 頻出上位から設定')
            top_num = st.number_input('stopword_top',0,100,help = '頻出上位何番目までをStopwordsに指定?')
            stopwords_1 = npt.get_stopword(top_n=top_num, min_freq=0)
            st.text(stopwords_1)
            
            st.text('\n')
            st.text('\n')
            st.text('\n')          
            
            st.write('2) リストの読み込み')
            stopwords_2 = []
            #ファイルの読み込み
            file = st.file_uploader("Upload file", type=['csv'], help = 'A1セルにstopwords、A2セル以降に任意のワードを記載したcsv(UTF-8)ファイルをアップロード')
            if file:
                stopwords_2_ = pd.read_csv(file, encoding = 'utf-8')
                stopwords_2.extend(list(stopwords_2_.loc[:, 'stopwords']))
                st.text(stopwords_2)
            
            st.text('\n')
            st.text('\n')
            st.text('\n')          
            
            st.write('3) 直接入力')        
            stopwords_3 = []
            stopwords_3_2 = []
            st.session_state["word"] = st.text_input('Stopwordsを入力してください.(英語のみ. 記号不可)', value = '', key = '1', help = '記号は入力できません.')

            with open('manual_s.csv', 'a') as f:
                f.write(st.session_state["word"] + '\n')
                f.close()
            
            stopwords_3_1 = pd.read_csv('manual_s.csv', encoding = 'utf-8')
            stopwords_3_2.extend(stopwords_3_1.loc[:, 'manual_words'])

            stopwords_3 = st.multiselect('入力したStopwords',
                        stopwords_3_2,
                        default = stopwords_3_2)
            
            os.remove('manual_s.csv')
            with open('manual_s.csv', 'w') as f:
                f.write('manual_words\n')
                for i in stopwords_3:
                    f.write(i + '\n')
                f.close()
            
            st.text(stopwords_3)

            st.text('\n')
            st.text('\n')
            st.text('\n')
            
            st.write('4) Stopwordsの確認')
            stopwords = []
            if stopwords_1 != [] and stopwords_2 != [] and stopwords_3 != []:
                stopwords.extend(stopwords_1)   
                stopwords.extend(stopwords_2)
                stopwords.extend(stopwords_3)
                st.code(stopwords)
            elif stopwords_1 != [] and stopwords_2 != []:
                stopwords.extend(stopwords_1)   
                stopwords.extend(stopwords_2)
                st.code(stopwords)
            elif stopwords_1 != [] and stopwords_3 != []:
                stopwords.extend(stopwords_1)   
                stopwords.extend(stopwords_3)
                st.code(stopwords)
            elif stopwords_3 != [] and stopwords_2 != []:
                stopwords.extend(stopwords_3)   
                stopwords.extend(stopwords_2)
                st.code(stopwords)            
            elif stopwords_1 != []:
                stopwords.extend(stopwords_1)
                st.code(stopwords)
            elif stopwords_2 != []:
                stopwords.extend(stopwords_2)
                st.code(stopwords)
            elif stopwords_3 != []:
                stopwords.extend(stopwords_3)
                st.code(stopwords)
            else:
                st.code(stopwords)
            
            st.text('\n')
            
            #Stopwords決定ボタン
            clicked_stop = st.button('stopwordsを決定')
        
            #stopwordの指定
            if clicked_stop:
                df_stopwords = pd.DataFrame(stopwords, columns = ['stopwords'])
                df_stopwords.to_csv('df_stopwords.csv', encoding = 'utf-8')
                st.write('stopwordsを設定しました.')
                st.header('⇒左タブ"頻出単語の可視化"へ')
                st.text('\n')
                st.text('\n')
                st.text('\n')

                col1, col2 = st.columns([3,1])
                with col1:
                    st.text('\n')
                    st.text('\n')
                    st.write('<p style="text-align: right">設定したStopwordsのダウンロードはこちら⇒</p>', unsafe_allow_html=True)
                with col2:
                    @st.cache
                    def convert_df(df):
                        # IMPORTANT: Cache the conversion to prevent computation on every rerun
                        return df.to_csv().encode('utf-8')

                    csv = convert_df(df_stopwords)
                    dt_now = datetime.datetime.now().date()
                    st.download_button(
                        label="Download Stopwords",
                        data=csv,
                        file_name = str(dt_now) + '_stopwords.csv',
                        mime='text/csv',
                    )

                os.remove('manual_s.csv')
                with open('manual_s.csv', 'w') as f:
                    f.write('manual_words\n')
                    f.close()              
            
            st.text('\n')    

            if st.session_state["word"] != '' or stopwords_3 != stopwords_3_2:
                st.session_state["page_control"] = 1
                raise st.experimental_rerun()

    def main1():
        ico = Image.open('icon.png')
        st.image(ico)
        st.header('Stopwordsの設定')
        
        #解析データの有無を確認
        exist = os.path.isfile('df.csv')
        if exist != True:
            st.header('解析データを作成してください.')
        else:
            #解析データの読み込み
            df = pd.read_csv('df.csv', encoding = 'utf-8')
            #テキストデータの指定
            npt = nlplot.NLPlot(df, target_col='words')
            

            st.write('1) 頻出上位から設定')
            top_num = st.number_input('stopword_top',0,100,help = '頻出上位何番目までをStopwordsに指定?')
            stopwords_1 = npt.get_stopword(top_n=top_num, min_freq=0)
            st.text(stopwords_1)
            
            st.text('\n')
            st.text('\n')
            st.text('\n')          
            
            st.write('2) リストの読み込み')
            stopwords_2 = []
            #ファイルの読み込み
            file = st.file_uploader("Upload file", type=['csv'], help = 'A1セルにstopwords、A2セル以降に任意のワードを記載したcsv(UTF-8)ファイルをアップロード')
            if file:
                stopwords_2_ = pd.read_csv(file, encoding = 'utf-8')
                stopwords_2.extend(list(stopwords_2_.loc[:, 'stopwords']))
                st.text(stopwords_2)
            
            st.text('\n')
            st.text('\n')
            st.text('\n')

            st.write('3) 直接入力') 
            stopwords_3 = []
            stopwords_3_2 = []
            ss = st.text_input('Stopwordsを入力してください.(英語のみ. 記号不可)', value = '', key = '2', help = '記号は入力できません.')
            
            with open('manual_s.csv', 'a') as f:
                f.write(ss + '\n')
                f.close()

            
            stopwords_3_1 = pd.read_csv('manual_s.csv', encoding = 'utf-8')
            stopwords_3_2.extend(stopwords_3_1.loc[:, 'manual_words'])

            stopwords_3 = st.multiselect('入力したStopwords',
                        stopwords_3_2,
                        default = stopwords_3_2)

            os.remove('manual_s.csv')
            with open('manual_s.csv', 'w') as f:
                f.write('manual_words\n')
                for i in stopwords_3:
                    f.write(i + '\n')
                f.close()
            
            st.text(stopwords_3)
            
            st.text('\n')
            st.text('\n')
            st.text('\n')
            
            st.write('4) Stopwordsの確認')
            stopwords = []
            if stopwords_1 != [] and stopwords_2 != [] and stopwords_3 != []:
                stopwords.extend(stopwords_1)   
                stopwords.extend(stopwords_2)
                stopwords.extend(stopwords_3)
                st.code(stopwords)
            elif stopwords_1 != [] and stopwords_2 != []:
                stopwords.extend(stopwords_1)   
                stopwords.extend(stopwords_2)
                st.code(stopwords)
            elif stopwords_1 != [] and stopwords_3 != []:
                stopwords.extend(stopwords_1)   
                stopwords.extend(stopwords_3)
                st.code(stopwords)
            elif stopwords_3 != [] and stopwords_2 != []:
                stopwords.extend(stopwords_3)   
                stopwords.extend(stopwords_2)
                st.code(stopwords)            
            elif stopwords_1 != []:
                stopwords.extend(stopwords_1)
                st.code(stopwords)
            elif stopwords_2 != []:
                stopwords.extend(stopwords_2)
                st.code(stopwords)
            elif stopwords_3 != []:
                stopwords.extend(stopwords_3)
                st.code(stopwords)
            else:
                st.code(stopwords)
            
            st.text('\n')

            #Stopwords決定ボタン
            clicked_stop = st.button('stopwordsを決定')
        
            #stopwordの指定
            if clicked_stop:
                df_stopwords = pd.DataFrame(stopwords)
                df_stopwords.to_csv('df_stopwords.csv', encoding = 'utf-8')
                st.write('stopwordsを設定しました.')
                st.header('⇒左タブ"頻出単語の可視化"へ')
                st.text('\n')
                st.text('\n')
                st.text('\n')
                
                col1, col2 = st.columns([3,1])
                with col1:
                    st.text('\n')
                    st.text('\n')
                    st.write('<p style="text-align: right">設定したStopwordsのダウンロードはこちら⇒</p>', unsafe_allow_html=True)
                with col2:
                    @st.cache
                    def convert_df(df):
                        # IMPORTANT: Cache the conversion to prevent computation on every rerun
                        return df.to_csv().encode('utf-8')

                    csv = convert_df(df_stopwords)
                    dt_now = datetime.datetime.now().date()
                    st.download_button(
                        label="Download Stopwords",
                        data=csv,
                        file_name = str(dt_now) + '_stopwords.csv',
                        mime='text/csv',
                    )

                os.remove('manual_s.csv')
                with open('manual_s.csv', 'w') as f:
                    f.write('manual_words\n')
                    f.close()                 
            
            if ss != '' or stopwords_3 != stopwords_3_2:
                st.session_state["page_control"] = 0
                raise st.experimental_rerun()


    # 状態保持する変数を作成して確認
    if ("page_control" in st.session_state and
    st.session_state["page_control"] == 1):
        main1()
    else:
        st.session_state["page_control"] = 0
        main()
            
    st.text('\n')


    
    


        
        




        
        


        
    
        

            
    
    
    
