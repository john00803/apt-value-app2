# components/show_gpt_result.py

import streamlit as st


def show_gpt_result(result_text: str):
    st.markdown("### ✅ GPT 분석 결과")
    st.markdown("---")
    st.markdown(result_text)
    st.markdown("---")
