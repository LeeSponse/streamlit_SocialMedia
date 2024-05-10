import streamlit as st
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
import numpy as np
import platform

import platform
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
plt.rcParams['axes.unicode_minus'] = False
if platform.system() == 'Linux':
    rc('font', family='NanumGothic')

# 운영체제별 한글 폰트 설정
if platform.system() == 'Darwin': # Mac 환경 폰트 설정
    plt.rc('font', family='AppleGothic')
elif platform.system() == 'Windows': # Windows 환경 폰트 설정
    plt.rc('font', family='Malgun Gothic')

plt.rc('axes', unicode_minus=False) # 마이너스 폰트 설정

def run_eda() :
    
    st.subheader('소셜미디어 사용시간과 관련된 여러가지 EDA를 분석하여 보여드립니다.')

    st.write('**데이터프레임 및 통계치와 다양한 정보를 확인 할 수 있습니다.**')

    df = pd.read_csv('./data/SoCialMediaEDA.csv')

    df1 = pd.read_csv('./data/SocialMediaML.csv')

    print(df)

    select_menu = ['데이터프레임 보기', '통계치 보기', '그래프 보기', '점수 보기', '상관계수 및 히트맵']

    choice_select = st.selectbox('**원하시는 항목을 선택하세요.**', select_menu)

    if choice_select == select_menu[0] :
        st.write('- 최소 13세부터 최대 91세 까지의 소셜미디어 중독을 검사한 데이터입니다.')
        st.write('- 4가지 점수를 기반으로 중독수준을 0(중독이 아님), 1(중독 의심), 2(중독) 으로 나누었습니다.')
        st.write('- 또한 나이, 성별, 결혼여부, 직업, 사용시간이 소셜미디어 중독여부에 영향을 끼치는지 확인하였습니다.')
        st.dataframe(df)

    elif choice_select == select_menu[1] :
        st.write('- 나이 및 각 점수의 **최소값,   평균값,   최대값,** 을 확인할 수 있습니다.')
        st.dataframe( df.describe() )

    elif choice_select == select_menu[2] :
        radio_menu = ['하루 평균 사용시간', '성별에 따른 사용여부', '직업별 사용 여부','사용시간이 정신건강에 미치는 영향']
        sc_select = st.radio(
        "**원하시는 항목을 선택하시면 %비율 및 그래프로 보여줍니다.**",
        (radio_menu))
        
        if sc_select == radio_menu[0] :

            # 사용시간 컬럼의 각각 갯수를 내림차순으로 df_time 라는 변수로  저장.
            df_time = df['하루 평균 소셜미디어 사용 시간'].value_counts()

            # 파이차트 색상 추출
            pie_colors = plt.cm.tab10(range(len(df_time)))

            # 두 개의 데이터프레임을 이용하여 파이차트와 바차트 그리기
            fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

            # 첫 번째 서브플롯에 파이차트 그리기
            ax1.pie(df_time, labels=df_time.index, autopct='%1.1f%%', startangle=140, colors=pie_colors)
            ax1.set_title('하루 평균 소셜 미디어 사용 시간')

            # 두 번째 서브플롯에 바차트 그리기 (파이차트와 동일한 색상 적용)
            df_time.plot(kind='bar', ax=ax2, color=pie_colors)
            plt.xlabel('사용시간')
            plt.ylabel('사용인원')
            ax2.set_title('하루 평균 소셜 미디어 사용 시간')
            st.pyplot(plt)

        elif sc_select == radio_menu[1] :

            # 성별 컬럼의 각각 갯수를 내림차순으로 df_gender 라는 변수로  저장.
            df_gender = df['성별'].value_counts()

            # 파이차트 색상 추출
            pie_colors = plt.cm.tab10(range(len(df_gender)))

            # 두 개의 데이터프레임을 이용하여 파이차트와 바차트 그리기
            fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

            # 첫 번째 서브플롯에 파이차트 그리기
            ax1.pie(df_gender, labels=df_gender.index, autopct='%1.1f%%', startangle=140, colors=pie_colors)
            ax1.set_title('성별에 따른 소셜미디어 사용 여부')

            # 두 번째 서브플롯에 바차트 그리기 (파이차트와 동일한 색상 적용)
            df_gender.plot(kind='bar', ax=ax2, color=pie_colors)
            ax2.set_title('성별에 따른 소셜미디어 사용 여부')
            st.pyplot(plt)

        elif sc_select == radio_menu[2] :

            # 직업현황 컬럼의 각각 갯수를 내림차순으로 df_job 이라는 변수로 저장.
            df_job = df['직업현황'].value_counts()

            # 파이차트 색상 추출
            pie_colors = plt.cm.tab10(range(len(df_job)))

            # 두 개의 데이터프레임을 이용하여 파이차트와 바차트 그리기
            fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

            # 첫 번째 서브플롯에 파이차트 그리기
            ax1.pie(df_job, labels=df_job.index, autopct='%1.1f%%', startangle=140, colors=pie_colors)
            ax1.set_title('직업별 소셜미디어 사용 여부')

            # 두 번째 서브플롯에 바차트 그리기 (파이차트와 동일한 색상 적용)
            df_job.plot(kind='bar', ax=ax2, color=pie_colors)
            ax2.set_title('직업별 소셜미디어 사용 여부')
            st.pyplot(plt)

        elif sc_select == radio_menu[3] :

            st.text(" 여기서 0은 영향이 없음. 1은 영향이 있을수 있음. 2는 영향이 매우큼을 나타냅니다.")

            # 결과 컬럼의 각각 갯수를 내림차순으로 df_oc 라는 변수로  저장.
            df_oc = df['결과'].value_counts()

            # 파이차트 색상 추출
            pie_colors = plt.cm.tab10(range(len(df_oc)))

            # 두 개의 데이터프레임을 이용하여 파이차트와 바차트 그리기
            fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

            # 첫 번째 서브플롯에 파이차트 그리기
            ax1.pie(df_oc, labels=df_oc.index, autopct='%1.1f%%', startangle=140, colors=pie_colors)
            ax1.set_title('사용시간이 정신건강에 대해 미치는 결과')

            # 두 번째 서브플롯에 바차트 그리기 (파이차트와 동일한 색상 적용)
            df_oc.plot(kind='bar', ax=ax2, color=pie_colors)
            ax2.set_title('사용시간이 정신건강에 대해 미치는 결과')
            st.pyplot(plt)

    elif choice_select == select_menu[3] :
        radio_menu = ['ADHD 점수', '불안장애 점수', '자존감(열등감) 점수','우울증 점수', '총합계 점수']
        sc_choice = st.radio(
        "**소셜미디어 사용시간에 따른 점수를 보여줍니다.**",
        (radio_menu))
        
        if sc_choice == radio_menu[0] :

            # 사용시간 과 ADHD 점수를 평균으로 나눈 뒤 저장.
            mean_adhd = df.groupby('하루 평균 소셜미디어 사용 시간')['ADHD 점수'].mean().sort_values(ascending=True)

            # 파이차트 색상 추출
            pie_colors = plt.cm.tab10(range(len(mean_adhd)))

            # 두 개의 데이터프레임을 이용하여 파이차트와 바차트 그리기
            fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

            # 첫 번째 서브플롯에 파이차트 그리기
            ax1.pie(mean_adhd, labels=mean_adhd.index, autopct='%1.1f%%', startangle=140, colors=pie_colors)
            ax1.set_title('소셜미디어 사용 시간에 따른 ADHD 점수')

            # 두 번째 서브플롯에 바차트 그리기 (파이차트와 동일한 색상 적용)
            mean_adhd.plot(kind='bar', ax=ax2, color=pie_colors)
            plt.xlabel('사용시간')
            plt.ylabel('ADHD 점수')
            ax2.set_title('평균 ADHD 점수')
            st.pyplot(plt)

        elif sc_choice == radio_menu[1] :

            # 사용시간 과 불안장애 점수를 평균으로 나눈 뒤 저장.
            mean_anx = df.groupby('하루 평균 소셜미디어 사용 시간')['불안장애 점수'].mean().sort_values(ascending=True)

            # 파이차트 색상 추출
            pie_colors = plt.cm.tab10(range(len(mean_anx)))

            # 두 개의 데이터프레임을 이용하여 파이차트와 바차트 그리기
            fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

            # 첫 번째 서브플롯에 파이차트 그리기
            ax1.pie(mean_anx, labels=mean_anx.index, autopct='%1.1f%%', startangle=140, colors=pie_colors)
            ax1.set_title('소셜미디어 사용 시간에 따른 불안장애 점수')

            # 두 번째 서브플롯에 바차트 그리기 (파이차트와 동일한 색상 적용)
            mean_anx.plot(kind='bar', ax=ax2, color=pie_colors)
            plt.xlabel('사용시간')
            plt.ylabel('불안장애 점수')
            ax2.set_title('평균 불안장애 점수')
            st.pyplot(plt)

        elif sc_choice == radio_menu[2] :

            # 사용시간과 자존감(열등감) 점수를 평균으로 나눈 뒤 저장.
            mean_sf = df.groupby('하루 평균 소셜미디어 사용 시간')['자존감 점수'].mean().sort_values(ascending=True)

            # 파이차트 색상 추출
            pie_colors = plt.cm.tab10(range(len(mean_sf)))

            # 두 개의 데이터프레임을 이용하여 파이차트와 바차트 그리기
            fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

            # 첫 번째 서브플롯에 파이차트 그리기
            ax1.pie(mean_sf, labels=mean_sf.index, autopct='%1.1f%%', startangle=140, colors=pie_colors)
            ax1.set_title('소셜미디어 사용 시간에 따른 자존감(열등감) 점수')

            # 두 번째 서브플롯에 바차트 그리기 (파이차트와 동일한 색상 적용)
            mean_sf.plot(kind='bar', ax=ax2, color=pie_colors)
            plt.xlabel('사용시간')
            plt.ylabel('자존감(열등감) 점수')
            ax2.set_title('평균 자존감(열등감) 점수')
            st.pyplot(plt)

        elif sc_choice == radio_menu[3] :

            # 사용시간과 우울증 점수를 평균으로 나눈뒤 저장.
            mean_de = df.groupby('하루 평균 소셜미디어 사용 시간')['우울증 점수'].mean().sort_values(ascending=True)

            # 파이차트 색상 추출
            pie_colors = plt.cm.tab10(range(len(mean_de)))

            # 두 개의 데이터프레임을 이용하여 파이차트와 바차트 그리기
            fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

            # 첫 번째 서브플롯에 파이차트 그리기
            ax1.pie(mean_de, labels=mean_de.index, autopct='%1.1f%%', startangle=140, colors=pie_colors)
            ax1.set_title('소셜미디어 사용 시간에 따른 우울증 점수')

            # 두 번째 서브플롯에 바차트 그리기 (파이차트와 동일한 색상 적용)
            mean_de.plot(kind='bar', ax=ax2, color=pie_colors)
            plt.xlabel('사용시간')
            plt.ylabel('우울증 점수')
            ax2.set_title('평균 우울증 점수')
            st.pyplot(plt)

        
        elif sc_choice == radio_menu[4] :

            # 사용시간과 총합계 점수를 평균으로 나눈 뒤 저장.
            mean_score = df.groupby('하루 평균 소셜미디어 사용 시간')['총합계 점수'].mean().sort_values(ascending=True)

            # 파이차트 색상 추출
            pie_colors = plt.cm.tab10(range(len(mean_score)))

            # 두 개의 데이터프레임을 이용하여 파이차트와 바차트 그리기
            fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

            # 첫 번째 서브플롯에 파이차트 그리기
            ax1.pie(mean_score, labels=mean_score.index, autopct='%1.1f%%', startangle=140, colors=pie_colors)
            ax1.set_title('소셜미디어 사용 시간에 따른 총합계 점수')

            # 두 번째 서브플롯에 바차트 그리기 (파이차트와 동일한 색상 적용)
            mean_score.plot(kind='bar', ax=ax2, color=pie_colors)
            plt.xlabel('사용시간')
            plt.ylabel('총합계 점수')
            ax2.set_title('평균 총합계 점수')
            st.pyplot(plt)


    elif choice_select == select_menu[4] :


        df1_corr = df1.corr()

        radio_menu = ['상관계수', '히스토그램', '히트맵']
        sc_choice = st.radio(
        "**클릭하시면 상관계수와 히스토그램 히트맵을 보여줍니다.**",
        (radio_menu))

        if sc_choice == radio_menu[0] :
        
            st.text('상관계수는 값이 1또는 -1에 가까울수록 연관성이 높습니다.')
            st.text('0에 가까울수록 연관성이 매우 낮으므로 참고하시면 감사하겠습니다.')

            st.dataframe(df1_corr)

        elif sc_choice == radio_menu[1] :

            sb.pairplot(df1, hue='결과', diag_kind = 'kde')
            st.pyplot(plt)

        elif sc_choice == radio_menu[2] :

            st.text('색이 진할수록 영향을 많이 받습니다')

            plt.figure(figsize=(20, 10))
            sb.heatmap(df1_corr, annot=True, cmap=sb.dark_palette("#69d", reverse=True, as_cmap=True), annot_kws={"size": 8})
            st.pyplot(plt)





