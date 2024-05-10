import streamlit as st
import webbrowser

def run_home() :
        st.header('소셜미디어 중독은 심각한 질병입니다!')
        st.write('##### 소셜미디어 사용시간에 따라 중독여부와 각종 정신건강에 미치는 영향을 예측하는 앱입니다.')
        st.image('./image/social.gif')
        st.write('- 소셜미디어 중독은 **ADHD,** **불안장애,** **자존감하락,** **우울증**에 영향을 끼칩니다.')
        st.write('- 소셜미디어 사용시간 및 각종 질문 을 통해 **소셜미디어** **중독**을 확인할 수 있습니다.')
        st.write('데이터는 캐글에 있는 Smmh.csv 파일을 사용하였습니다.')

        show_button = st.checkbox('Kaggle에서 데이터셋 보러가기')  # 체크박스를 이용하여 버튼 보이기/숨기기

        if show_button:

        # 버튼을 누르면 URL로 이동
            if st.button('Kaggle 데이터셋 링크', key='button1'):
                # 이동할 URL
                url = 'https://www.kaggle.com/datasets/souvikahmed071/social-media-and-mental-health'
                # 새 탭에서 URL 열기
                webbrowser.open_new_tab(url)


        show_button1 = st.checkbox('소셜미디어 중독에 관련된 기사 보러가기')  # 체크박스를 이용하여 버튼 보이기/숨기기

        if show_button1:

            # 셀렉트 안에 버튼 할당하기
            selected_option = st.radio("소셜 미디어 중독관련 기사 선택", ('1.소셜미디어로 인한 극단적 선택 기사', '2.가장 많이 사용하는 SNS 중독 기사', '3.SNS 중독이 되는 이유 기사'))

            if selected_option == '1.소셜미디어로 인한 극단적 선택 기사' :
                if st.button('기사 링크로 이동'):
                # 이동할 URL
                    url = 'https://www.yna.co.kr/view/AKR20220122042400009'
                    # 새 탭에서 URL 열기
                    webbrowser.open_new_tab(url)

            elif selected_option == '2.가장 많이 사용하는 SNS 중독 기사':
                if st.button('기사 링크로 이동'):
                # 이동할 URL
                    url = 'https://www.kyongbuk.co.kr/news/articleView.html?idxno=1059831'
                    # 새 탭에서 URL 열기
                    webbrowser.open_new_tab(url)

            elif selected_option == '3.SNS 중독이 되는 이유 기사':
                if st.button('기사 링크로 이동'):
                # 이동할 URL
                    url = 'https://www.ohmynews.com/NWS_Web/View/at_pg.aspx?CNTN_CD=A0002963549'
                    # 새 탭에서 URL 열기
                    webbrowser.open_new_tab(url)


