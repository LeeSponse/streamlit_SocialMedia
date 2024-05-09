import streamlit as st
import webbrowser

def run_home() :
        st.header('소셜미디어 중독은 심각한 질병입니다.')
        st.image('./image/social_image.jpg', use_column_width= True)
        st.text('소셜미디어 중독은 ADHD, 불안장애, 자존감하락, 우울증에 영향을 끼칩니다.')
        st.text('소셜미디어 사용시간 및 여러 질문항목을 통해 소셜미디어 중독을 확인할 수 있습니다.')
        st.text('데이터는 캐글에 있는 Smmh.csv 파일을 사용하였습니다.')

        # 버튼을 누르면 URL로 이동
        if st.button('Kaggle에서 데이터셋 보기'):
            # 이동할 URL
            url = 'https://www.kaggle.com/datasets/souvikahmed071/social-media-and-mental-health'
            # 새 탭에서 URL 열기
            webbrowser.open_new_tab(url)
