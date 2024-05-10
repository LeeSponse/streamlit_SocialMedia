import streamlit as st

from home import run_home
from eda import run_eda
from ml import run_ml
from tkinter.tix import COLUMN
from pyparsing import empty

def main() :

    st.set_page_config(layout="wide")


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


