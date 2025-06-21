
import streamlit as st
import random

# 질문 유형과 질문 데이터
question_bank = {
    "감정 탐색": [
        "요즘 자주 느끼는 감정은 뭐야?",
        "그 감정은 언제 가장 강하게 느껴져?",
        "감정을 말로 표현하는 게 어려울 때도 있니?"
    ],
    "자기이해": [
        "나는 어떤 사람이라고 생각해?",
        "나를 가장 잘 표현하는 말은 무엇일까?",
        "내가 가장 편안하다고 느낄 때는 언제야?"
    ],
    "관계/사회성": [
        "친구들과 있을 때 가장 편할 때는 언제야?",
        "가족 중에 누구와 가장 친하다고 느껴?",
        "다른 사람과 다툰 적 있을까? 그때 기분은 어땠어?"
    ],
    "스트레스/불안": [
        "최근에 스트레스 받았던 일이 있었어?",
        "스트레스를 받을 때 너만의 해소 방법이 있어?",
        "불안할 때 주로 어떤 생각이 들어?"
    ],
    "진로/미래": [
        "어떤 일을 할 때 시간이 빨리 가는 것 같아?",
        "미래에 꼭 해보고 싶은 게 있어?",
        "지금 꿈꾸는 직업이 있니?"
    ],
    "자존감": [
        "스스로 칭찬하고 싶은 점이 있어?",
        "“나는 괜찮은 사람이야”라는 말을 믿을 수 있어?",
        "내가 나를 믿지 못하는 순간은 언제였어?"
    ],
    "문제해결/갈등": [
        "친구랑 다툴 때 보통 어떻게 해결해?",
        "문제가 생기면 누구에게 먼저 말해?",
        "갈등을 피하고 싶을 때 너는 어떻게 해?"
    ]
}

# Streamlit 앱 설정
st.set_page_config(page_title="마음열기 질문툴", layout="wide")
st.title("💬 마음열기 질문툴")
st.caption("청소년의 마음을 여는 따뜻한 질문 도우미 🌱")

# 질문 유형 선택
st.markdown("### 🧠 질문 유형을 선택하세요")
question_type = st.selectbox("유형 선택", list(question_bank.keys()))

# 질문 표시 및 심각도 평가
if question_type:
    st.markdown(f"### 📘 '{question_type}' 질문 목록 및 감정 심각도 평가")
    responses = []

    for i, question in enumerate(question_bank[question_type], 1):
        st.markdown(f"**{i}. {question}**")
        severity = st.slider(
            f"→ 이 질문에 대한 감정의 심각도는? (0: 전혀 없음 ~ 10: 매우 심각)",
            0, 10, 0, key=f"slider_{i}"
        )
        responses.append({"질문": question, "심각도": severity})

    # 감정 요약 결과 보기
    if st.button("📊 감정 심각도 요약 보기"):
        st.markdown("### 📝 감정 심각도 결과")
        for item in responses:
            st.write(f"- **{item['질문']}** → 심각도: {item['심각도']}점")

        # 심각도 높은 질문 강조
        st.markdown("### 🚨 심각도가 높은 질문")
        high_risk = [r for r in responses if r['심각도'] >= 7]
        if high_risk:
            for r in high_risk:
                st.warning(f"⚠️ **{r['질문']}** → {r['심각도']}점")
        else:
            st.success("심각도가 높은 질문은 없습니다.")

    # 무작위 질문 추천
    if st.button("🎲 무작위 질문 추천"):
        st.info(f"랜덤 질문: **{random.choice(question_bank[question_type])}**")
      emotion_icons = {
    "😊 기쁨": "😊", 
    "😐 무기력": "😐", 
    "😢 슬픔": "😢"
}

selected_emotion = st.radio("지금 감정에 가장 가까운 이모지는?", list(emotion_icons.values()))

