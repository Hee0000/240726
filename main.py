import streamlit as st
st.title('희원의 웹 서비스 만들기")
name = st.text_input('이름을 입력해주세요 : ')
menu = st.selectbox('좋아하는 음식을 선택해주세요 : ', [샌드위치, 아이스크림])
if st.button('인생말 생성') :
 st.write(name + '님! 당신이 좋아하는 음식은 '+menu+'이군요? 저도 좋아요')
