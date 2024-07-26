import streamlit as st

st.title('파리 올림픽 일정표 확인하기')

name = st.text_input('이름을 입력해주세요 : ')

sports = st.selectbox('확인하고 싶은 파리 올림픽 종목을 선택해주세요 : ', 
                      ['육상', '수영', '테니스', '배드민턴', '농구', '배구', '핸드볼']

if st.button('종목 정보 보기'):
    st.write(name + '님! ' + sports + '의 일정은 다음과 같습니다.')

    # 종목의 픽토그램과 일정을 보여줍니다.
    pictogram_url = 'https://olympics.com/ko/paris-2024/the-games/the-brand/pictograms'
    schedule_url = 'https://olympics.com/ko/paris-2024/schedule'

    if sports == '육상':
        st.image(pictogram_url)
        st.write(f'[육상 경기 일정 보기]({schedule_url})')
    elif sports == '수영':
        st.image(pictogram_url)
        st.write(f'[수영 경기 일정 보기]({schedule_url})')
    elif sports == '체조':
        st.image(pictogram_url)
        st.write(f'[체조 경기 일정 보기]({schedule_url})')
    elif sports == '유도':
        st.image(pictogram_url)
        st.write(f'[유도 경기 일정 보기]({schedule_url})')
    elif sports == '테니스':
        st.image(pictogram_url)
        st.write(f'[테니스 경기 일정 보기]({schedule_url})')
    # 다른 종목들에 대한 정보도 추가하세요
    # 예:
    # elif sports == '배드민턴':
    #     st.image(pictogram_url)
    #     st.write(f'[배드민턴 경기 일정 보기]({schedule_url})')

# 실제 이미지 URL을 사용해야 합니다. 위의 예시는 예제 URL입니다.
