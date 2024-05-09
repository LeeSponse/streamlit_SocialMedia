import streamlit as st
import time

from home import run_home
from eda import run_eda
from ml import run_ml

def main() :

    # 로딩 텍스트와 프로그레스 바를 위한 빈 슬롯 생성
    latest_iteration = st.empty()
    bar = st.empty()

    # 0부터 100까지 로딩
    for i in range(100):
        # 각 반복마다 로딩 텍스트와 프로그레스 바 업데이트
        latest_iteration.text(f'로딩 {i+1}%')
        bar.progress(i + 1)
        time.sleep(0.01)

    # 로딩이 끝난 후 로딩 텍스트와 프로그레스 바 제거
    latest_iteration.empty()
    bar.empty()

    menu = ['메인페이지', ' EDA 분석 ', '정신건강 예측하기']
        
    choice = st.sidebar.selectbox('메뉴', menu)

    if choice == menu[0] :
        run_home()

    elif choice == menu[1]:
        run_eda()

    elif choice == menu[2]:
        run_ml()

if __name__ == '__main__' :
    main()


