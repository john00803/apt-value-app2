# components/show_gpt_result.py

import streamlit as st

def show_gpt_result(result: str):
    st.subheader("🏢 GPT 아파트 가치 평가 결과")

    if not result:
        st.warning("GPT 응답이 없습니다.")
        return

    blocks = result.strip().split("\n")
    for block in blocks:
        if block.startswith("1.") or block.startswith("2.") or block.startswith("3."):
            st.markdown(f"✅ {block}")
        elif block.startswith("4.") or "한줄평" in block:
            st.success(block)
        elif "총점" in block:
            st.info(f"📊 {block}")
        elif block.startswith("📍"):
            st.markdown(f"### {block}")
        else:
            st.write(block)
