import streamlit as st
import joblib
import numpy as np 
import time

def run_ml() :
    st.subheader('정신건강 예측하기')

    #1. 예측하기 위해서 유저한테 입력받기.
    # 나이,성별, 결혼여부, 하루 사용시간, ADHD 관련질문, 불안장애 관련, 자존감 관련, 우울증 관련

    #1-1. 나이 입력받기

    st.text('나이를 입력하세요.')
    age = st.number_input( '나이 입력', min_value=18, max_value=100, value=24 )

    print('나이')
    print(age)

    #1-2. 성별 입력받기
    st.text('성별을 선택하세요.')
    gender = st.radio('성별 선택', ['남자', '여자'])

    if gender == '남자' :
        gender = 0
    elif gender == '여자' :
        gender = 1

    print('성별')
    print(gender)

    #1-3. 결혼여부 입력받기
    st.text('결혼여부를 선택하세요.')
    Married = st.radio('결혼여부 선택', ['결혼', '이혼', '미혼'])

    if Married == '결혼' :
        Married = 0

    elif Married == '이혼' :
        Married = 1

    elif Married == '미혼' :
        Married = 2

    print('결혼')
    print(Married)

    #1-4. 사용시간 입력받기
    st.text('하루 평균 사용시간을 선택하세요.')
    sc_time = st.radio('사용시간 선택', ['1시간 미만', 
                                  '1 ~ 2시간 사이',
                                  '2 ~ 3시간 사이', 
                                  '3 ~ 4시간 사이', 
                                  '4 ~ 5시간 사이', 
                                  '5시간 이상'])
    
    if sc_time == '1시간 미만' :
        sc_time = 0
        
    elif sc_time == '1 ~ 2시간 사이' :
        sc_time = 1

    elif sc_time == '2 ~ 3시간 사이' :
        sc_time = 2

    elif sc_time == '3 ~ 4시간 사이' :
        sc_time = 3

    elif sc_time == '4 ~ 5시간 사이' :
        sc_time = 4

    elif sc_time == '5시간 이상' :
        sc_time = 5

    print('사용시간')
    print(sc_time)

    #1-5. ADHD 관련 질문 입력받기.
    st.text('ADHD 관련 질문 문항')

    sc_use = st.radio('1.특정 목적 없이 소셜 미디어를 자주 사용한다.', ['전혀 그렇지 않다.', 
                                  '그렇지 않다.',
                                  '그렇다.', 
                                  '자주 그렇다.', 
                                  '매우 그렇다.' ])
    
    if sc_use == '전혀 그렇지 않다.' :
        sc_use = 1
        
    elif sc_use == '그렇지 않다.' :
        sc_use = 2

    elif sc_use == '그렇다.' :
        sc_use = 3

    elif sc_use == '자주 그렇다.' :
        sc_use = 4

    elif sc_use == '매우 그렇다.' :
        sc_use = 5

    print("목적")
    print(sc_use)

    sc_att = st.radio('2.뭔가를 하느라 바쁠 때 소셜 미디어로 인해 주의력이 떨어진다.', ['전혀 그렇지 않다.', 
                                  '그렇지 않다.',
                                  '그렇다.', 
                                  '자주 그렇다.', 
                                  '매우 그렇다.' ])
    
    if sc_att == '전혀 그렇지 않다.' :
        sc_att = 1
        
    elif sc_att == '그렇지 않다.' :
        sc_att = 2

    elif sc_att == '그렇다.' :
        sc_att = 3

    elif sc_att == '자주 그렇다.' :
        sc_att = 4

    elif sc_att == '매우 그렇다.' :
        sc_att = 5

    print("주의")
    print(sc_att)

    sc_dis = st.radio('3.쉽게 산만해지거나 정신이 없다.', ['전혀 그렇지 않다.', 
                                  '그렇지 않다.',
                                  '그렇다.', 
                                  '자주 그렇다.', 
                                  '매우 그렇다.' ])
    
    if sc_dis == '전혀 그렇지 않다.' :
        sc_dis = 1
        
    elif sc_dis == '그렇지 않다.' :
        sc_dis = 2

    elif sc_dis == '그렇다.' :
        sc_dis = 3

    elif sc_dis == '자주 그렇다.' :
        sc_dis = 4

    elif sc_dis == '매우 그렇다.' :
        sc_dis = 5

    print("산만")
    print(sc_dis)

    sc_dif = st.radio('4.어떤일이나 해야하는 일에 집중하기가 어렵다.', 
                                ['전혀 그렇지 않다.', 
                                  '그렇지 않다.',
                                  '그렇다.', 
                                  '자주 그렇다.', 
                                  '매우 그렇다.' ])
    
    if sc_dif == '전혀 그렇지 않다.' :
        sc_dif = 1
        
    elif sc_dif == '그렇지 않다.' :
        sc_dif = 2

    elif sc_dif == '그렇다.' :
        sc_dif = 3

    elif sc_dif == '자주 그렇다.' :
        sc_dif = 4

    elif sc_dif == '매우 그렇다.' :
        sc_dif = 5

    print("집중")
    print(sc_dif)

    #1-6. 불안장애 질문 입력받기
    st.text('불안장애 관련 질문 문항')

    sc_res = st.radio('1.한동안 소셜미디어를 사용하지 않으면 불안하다.', 
                                ['전혀 그렇지 않다.', 
                                  '그렇지 않다.',
                                  '그렇다.', 
                                  '자주 그렇다.', 
                                  '매우 그렇다.' ])
    
    if sc_res == '전혀 그렇지 않다.' :
        sc_res = 1
        
    elif sc_res == '그렇지 않다.' :
        sc_res = 2

    elif sc_res == '그렇다.' :
        sc_res = 3

    elif sc_res == '자주 그렇다.' :
        sc_res = 4

    elif sc_res == '매우 그렇다.' :
        sc_res = 5

    print("불안")
    print(sc_res)

    sc_sca = st.radio('2.걱정거리로 인해 괴로울때가 있다.', 
                                ['전혀 그렇지 않다.', 
                                  '그렇지 않다.',
                                  '그렇다.', 
                                  '자주 그렇다.', 
                                  '매우 그렇다.' ])
    
    if sc_sca == '전혀 그렇지 않다.' :
        sc_sca = 1
        
    elif sc_sca == '그렇지 않다.' :
        sc_sca = 2

    elif sc_sca == '그렇다.' :
        sc_sca = 3

    elif sc_sca == '자주 그렇다.' :
        sc_sca = 4

    elif sc_sca == '매우 그렇다.' :
        sc_sca = 5

    print("걱정")
    print(sc_sca)

    #1-7. 자존감(열등감) 질문 입력받기
    st.text('자존감(열등감) 관련 질문 문항')

    sc_sf = st.radio('1.소셜미디어를 사용하면서 성공한 사람과 나를 자주 비교한다.', 
                                ['전혀 그렇지 않다.', 
                                  '그렇지 않다.',
                                  '그렇다.', 
                                  '자주 그렇다.', 
                                  '매우 그렇다.' ])
    
    if sc_sf == '전혀 그렇지 않다.' :
        sc_sf = 1
        
    elif sc_sf == '그렇지 않다.' :
        sc_sf = 2

    elif sc_sf == '그렇다.' :
        sc_sf = 3

    elif sc_sf == '자주 그렇다.' :
        sc_sf = 4

    elif sc_sf == '매우 그렇다.' :
        sc_sf = 5

    print("비교")
    print(sc_sf)

    sc_th = st.radio('2.이전 질문에 대하여 그러한 비교에 어떻게 생각하시나요?', 
                                ['매우 부정적이다.', 
                                  '부정적이다.',
                                  '모르겠다.', 
                                  '약간 긍정적이다.', 
                                  '매우 긍정적이다.' ])
    
    if sc_th == '매우 부정적이다.' :
        sc_th = 1
        
    elif sc_th == '부정적이다.' :
        sc_th = 2

    elif sc_th == '모르겠다.' :
        sc_th = 3

    elif sc_th == '약간 긍정적이다.' :
        sc_th = 4

    elif sc_th == '매우 긍정적이다.' :
        sc_th = 5

    print("생각")
    print(sc_th)

    sc_val = st.radio('3.소셜미디어의 기능으로부터 검증(좋은결과)을 얻으려고한다.', 
                                ['전혀 그렇지 않다.', 
                                  '그렇지 않다.',
                                  '그렇다.', 
                                  '자주 그렇다.', 
                                  '매우 그렇다.' ])
    
    if sc_val == '전혀 그렇지 않다.' :
        sc_val = 1
        
    elif sc_val == '그렇지 않다.' :
        sc_val = 2

    elif sc_val == '그렇다.' :
        sc_val = 3

    elif sc_val == '자주 그렇다.' :
        sc_val = 4

    elif sc_val == '매우 그렇다.' :
        sc_val = 5

    print("검증")
    print(sc_val)


    #1-8. 우울증 질문 입력받기
    st.text('우울증 관련 질문 문항')

    sc_dep = st.radio('1.자주 우울하거나 무기력함을 느낀다.', 
                                ['전혀 그렇지 않다.', 
                                  '그렇지 않다.',
                                  '그렇다.', 
                                  '자주 그렇다.', 
                                  '매우 그렇다.' ])
    
    if sc_dep == '전혀 그렇지 않다.' :
        sc_dep = 1
        
    elif sc_dep == '그렇지 않다.' :
        sc_dep = 2

    elif sc_dep == '그렇다.' :
        sc_dep = 3

    elif sc_dep == '자주 그렇다.' :
        sc_dep = 4

    elif sc_dep == '매우 그렇다.' :
        sc_dep = 5

    print("무기력")
    print(sc_dep)

    sc_fre = st.radio('2.일상생활의 활동에서 관심사가 자주 변한다.', 
                                ['전혀 그렇지 않다.', 
                                  '그렇지 않다.',
                                  '그렇다.', 
                                  '자주 그렇다.', 
                                  '매우 그렇다.' ])
    
    if sc_fre == '전혀 그렇지 않다.' :
        sc_fre = 1
        
    elif sc_fre == '그렇지 않다.' :
        sc_fre = 2

    elif sc_fre == '그렇다.' :
        sc_fre = 3

    elif sc_fre == '자주 그렇다.' :
        sc_fre = 4

    elif sc_fre == '매우 그렇다.' :
        sc_fre = 5

    print("관심사")
    print(sc_fre)

    sc_slp = st.radio('3.밤에 잠을 자기가 어렵다.', 
                                ['전혀 그렇지 않다.', 
                                  '그렇지 않다.',
                                  '그렇다.', 
                                  '자주 그렇다.', 
                                  '매우 그렇다.' ])
    
    if sc_slp == '전혀 그렇지 않다.' :
        sc_slp = 1
        
    elif sc_slp == '그렇지 않다.' :
        sc_slp = 2

    elif sc_slp == '그렇다.' :
        sc_slp = 3

    elif sc_slp == '자주 그렇다.' :
        sc_slp = 4

    elif sc_slp == '매우 그렇다.' :
        sc_slp = 5

    print('잠')
    print(sc_slp)

    #2. 머신러닝으로 예측하기.
    st.subheader('버튼을 누르면 예측합니다.')

    #2-1. 버튼을 만들어 예측하기.
    if st.button('예측하기'):
    
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
    
        #2-2. 준비된 모델 불러오기
        NBm = joblib.load('./model/NBModel.pkl')


        #2-2. 각 질문에 점수를 합산하여 다시 저장한다.
        Adhd_score = [sc_use + sc_att + sc_dis + sc_dif]   
        print('ADHD점수')
        print(Adhd_score)

        Anx_score =  [sc_res + sc_sca]
        print('불안장애 점수')
        print(Anx_score)

        Comp_score = [sc_sf + sc_th + sc_val]
        print('열등 점수')
        print(Comp_score)

        Dep_score = [sc_dep + sc_fre + sc_slp]
        print('우울 점수')
        print(Dep_score)

        total_score = [sum(Adhd_score) + sum(Anx_score) + sum(Comp_score) + sum(Dep_score)]


        new_df = [age, gender, Married, sc_time, Adhd_score, Anx_score, Comp_score, Dep_score]
        print(new_df)

        # 리스트의 내부 요소들을 평탄화하여 모든 요소를 동일한 데이터 타입으로 만듭니다.
        nnew_df = [item if not isinstance(item, list) else item[0] for item in new_df]

        # 데이터를 numpy 배열로 변환합니다.
        np_array = np.array(nnew_df).reshape(1, -1)


        # 모델로 예측을 수행합니다.
        y_pred = NBm.predict(np_array)

        # 예측 결과를 출력하거나 필요에 따라 해당 결과를 사용합니다.
        print(y_pred)

        if y_pred == 0 :
            st.success('당신은 소셜미디어 중독이 아닙니다.')
            st.text(f"당신의 점수는 {total_score}점 입니다.")
            
        elif y_pred == 1 :
            st.info('당신은 소셜미디어 중독이 의심됩니다.')
            st.text(f"당신의 점수는 {total_score}점 입니다.") 

        elif y_pred == 2 :
            st.warning('당신은 심각한 소셜미디어 중독이 의심됩니다.')
            st.text(f"당신의 점수는 {total_score}점 입니다.") 













