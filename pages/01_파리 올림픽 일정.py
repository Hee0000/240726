import streamlit as st

st.title('파리 올림픽 일정표 확인하기')

name = st.text_input('대한민국 국가대표 선수들에게 응원의 한마디! : ')

sports = st.selectbox('확인하고 싶은 파리 올림픽 종목을 선택해주세요 : ', 
                      ['육상', '수영', '테니스', '배드민턴', '농구', '배구', '축구'])

if st.button('종목 정보 보기'):
    st.write(name + sports + '의 일정은 다음과 같습니다.')

    # 종목의 일정을 보여줍니다.
    schedule_url = 'https://olympics.com/ko/paris-2024/schedule'

    if sports == '육상':
        st.write(f'[육상 경기 일정 보기]({schedule_url})')
        st.write('육상 경기 일정: 2024년 8월 1일 - 2024년 8월 11일')
    elif sports == '수영':
        st.write(f'[수영 경기 일정 보기]({schedule_url})')
        st.write('수영 경기 일정: 2024년 7월 27일 - 2024년 8월 4일')
    elif sports == '체조':
        st.write(f'[체조 경기 일정 보기]({schedule_url})')
        st.write('체조 경기 일정: 2024년 7월 27일 - 2024년 8월 5일')
    elif sports == '유도':
        st.write(f'[유도 경기 일정 보기]({schedule_url})')
        st.write('유도 경기 일정: 2024년 7월 27일 - 2024년 8월 3일')
    elif sports == '테니스':
        st.write(f'[테니스 경기 일정 보기]({schedule_url})')
        st.write('테니스 경기 일정: 2024년 7월 27일 - 2024년 8월 4일')
    elif sports == '배드민턴':
        st.write(f'[배드민턴 경기 일정 보기]({schedule_url})')
        st.write('배드민턴 경기 일정: 2024년 7월 27일 - 2024년 8월 5일')
    elif sports == '농구':
        st.write(f'[농구 경기 일정 보기]({schedule_url})')
        st.write('농구 경기 일정: 2024년 7월 27일 - 2024년 8월 10일')
    elif sports == '배구':
        st.write(f'[배구 경기 일정 보기]({schedule_url})')
        st.write('배구 경기 일정: 2024년 7월 27일 - 2024년 8월 11일')
    elif sports == '축구':
        st.write(f'[축구 경기 일정 보기]({schedule_url})')
        st.write('축구 경기 일정: 2024년 7월 24일 - 2024년 8월 10일')
