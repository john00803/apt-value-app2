# app.py

import streamlit as st
from auth.user_loader import is_valid_user
from gpt.gpt_cache import gpt_with_cache
from components.show_gpt_result import show_gpt_result

# 타이틀
st.title("아파트 가치 평가 프로그램")
st.markdown("이메일을 입력하세요")

# 이메일 입력 받기
email = st.text_input("이메일을 입력하세요")

# 이메일 검증
if email:
    if is_valid_user(email):
        st.success("등록된 사용자입니다!")
        st.markdown("아파트 가치 평가를 시작합니다.")
        
        # GPT 모델을 호출하는 버튼
        if st.button("평가 시작"):
            # GPT를 활용한 평가 프로세스
            prompt = "아파트 가치 평가에 대한 분석을 수행해 주세요."  # 예시 프롬프트
            result = gpt_with_cache(prompt)

            # 결과 출력
            show_gpt_result(result)
    else:
        st.error("등록되지 않은 사용자입니다.")
