import streamlit as st
st.title('희원의 웹 서비스 만들기')
name = st.text_input('이름을 입력해주세요 : ')
menu = st.selectbox('좋아하는 디저트를 선택해주세요 : ', ['과일', '아이스크림', '마카롱', '소금빵', '커피'])
if st.button('인생말 생성') :
 st.write(name + '님! 당신이 좋아하는 음식은 '+menu+'이군요? 아쉽게도 쿠폰 제공은 어렵습니다.ㅋㅋ')
