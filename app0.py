import streamlit as st
from PIL import Image
import subprocess


def app():
    ico = Image.open('.\\img\\icon.png')
    st.image(ico)
#    st.title("Scientia")
    st.header('How to Use')

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('Step1 :')
        step1 = st.button('データの準備')
        #st.write('<p>Step1 : <a href="\\manual\\Scientia_step1.pdf">データの準備</a></p>', unsafe_allow_html = True)
        if step1:
            subprocess.Popen(["start", "", r".\\manual\\Scientia_step1.pdf"], shell=True)
        top1 = Image.open('.\\img\\top1.png')
        st.image(top1, use_column_width = 'always')

    with col2:
        st.markdown('Step2 :')
        step2 = st.button('Stopwordsの設定')
        #st.write('<p>Step2 : <a href="\\manual\\Scientia_step2.pdf">Stopwordsの設定</a></p>', unsafe_allow_html = True)
        if step2:
            subprocess.Popen(["start", "", r".\\manual\\Scientia_step2.pdf"], shell=True)        
        top2 = Image.open('.\\img\\top2.png')
        st.image(top2, use_column_width = 'always')

    with col3:
        st.markdown('Step3 :')
        step3 = st.button('テキスト解析')
        #st.write('<p>Step3 : <a href="\\manual\\Scientia_step3.pdf">テキスト解析</a></p>', unsafe_allow_html = True)
        if step3:
            subprocess.Popen(["start", "", r".\\manual\\Scientia_step3.pdf"], shell=True)
        top3 = Image.open('.\\img\\top3.png')
        st.image(top3, use_column_width = 'always')

    st.text('\n')
    st.text('\n')
    st.text('\n')
    
    st.write('<hr color="#C9C9C9">', unsafe_allow_html=True)
    st.write('<p color = "#C9C9C9">©2022<a href="https://outlook.office.com/owa/?subject=Scientiaに関する問い合わせ&body=問い合わせ内容を記載ください.&to=453L03@dks-web.co.jp&path=/mail/action/compose">MI Promotion Department.</a> All Rights Reserved.</p>', unsafe_allow_html=True)


if __name__ == '__main__':
    app()

