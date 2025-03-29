# gpt/make_prompt.py

def make_prompt(apt_name: str, apt_data: dict) -> str:
    lines = [
        f"당신은 아파트 분석 전문가입니다.",
        f"아파트명: {apt_name}",
        "다음은 이 아파트의 주요 정보입니다:\n",
    ]

    for key, value in apt_data.items():
        lines.append(f"- {key}: {value}")

    lines.append("\n위 정보를 바탕으로 아래 항목에 대해 요약 평가해주세요:\n")
    lines.append("1. 교통 접근성")
    lines.append("2. 학군 및 생활 인프라")
    lines.append("3. 실거주 만족도")
    lines.append("4. 브랜드 및 프리미엄 가치")
    lines.append("5. 투자 안전성과 향후 전망")
    lines.append("\n각 항목은 1~2문장으로 간결하게 작성해주세요.")

    return "\n".join(lines)
