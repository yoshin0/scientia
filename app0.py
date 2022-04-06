import streamlit as st
from PIL import Image
import subprocess

def app():
    ico = Image.open('icon.png')
    st.image(ico)
    st.header('How to Use')
    
    option = st.selectbox(
     '参照したいマニュアルを選択してください.',
     ('', 'Step1 : データの準備', 'Step2 : Stopwordsの設定', 'Step3 : テキスト解析'))
    if option == 'Step1 : データの準備':
        for i in ['1', '2', '3', '4']:            
            manual = Image.open('Scientia_step1_' + str(i) + '.jpg')
            st.image(manual, use_column_width = 'always')
    elif option == 'Step2 : Stopwordsの設定':
        for i in ['1', '2']:            
            manual = Image.open('Scientia_step2_' + str(i) + '.jpg')
            st.image(manual, use_column_width = 'always')
    elif option == 'Step3 : テキスト解析':
        for i in ['1']:            
            manual = Image.open('Scientia_step3_' + str(i) + '.jpg')
            st.image(manual, use_column_width = 'always')
    else:        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown('Step1 : データの準備')
            top1 = Image.open('top1.png')
            st.image(top1, use_column_width = 'always')

        with col2:
            st.markdown('Step2 : Stopwordsの設定')
            top2 = Image.open('top2.png')
            st.image(top2, use_column_width = 'always')
        with col3:
            st.markdown('Step3 : テキスト解析')
            top3 = Image.open('top3.png')
            st.image(top3, use_column_width = 'always')

    st.text('\n')
    st.text('\n')
    st.text('\n')

    st.write('<hr color="#C9C9C9">', unsafe_allow_html=True)
    st.write('<p color = "#C9C9C9">©2022<a href="https://outlook.office.com/owa/?subject=Scientiaに関する問い合わせ&body=問い合わせ内容を記載ください.&to=453L03@dks-web.co.jp&path=/mail/action/compose">MI Promotion Department.</a> All Rights Reserved.</p>', unsafe_allow_html=True)


if __name__ == '__main__':
    app()

