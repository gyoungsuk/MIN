import streamlit as st

st.markdown("👩‍⚕️ **의사** – 건강을 책임지는 전문가!")
st.markdown("👨‍🔬 **과학자** – 세상의 원리를 밝히는 탐구자!")
st.markdown("🧑‍💻 **프로그래머** – 미래를 코딩하는 창조자!")
st.markdown("🎨 **디자이너** – 세상을 아름답게 꾸미는 예술가!")
st.markdown("🎤 **MC/연예인** – 무대 위의 빛나는 스타!")
st.markdown("👨‍🏫 **선생님** – 배움의 길을 밝혀주는 길잡이!")
st.markdown("🧑‍🚀 **우주인** – 끝없는 하늘을 향해 나아가는 개척자!")
st.markdown("👮 **경찰관** – 우리 사회의 안전지킴이!")
st.markdown("👩‍🍳 **요리사** – 맛으로 행복을 만드는 예술가!")
st.markdown("🧑‍🌾 **농부** – 자연과 함께하는 생명의 수호자!")
import streamlit as st
import streamlit as st

st.title("🔍 진로 탐색: 직업 분류별 보기")

# 탭 이름 정의
tabs = st.tabs(["👩‍⚕️ 의료", "🧑‍💻 IT/공학", "🎨 예술/디자인", "🎓 교육", "🚓 공공서비스", "📺 미디어/연예", "🌾 자연/환경"])

# 각 탭 내용 정의
with tabs[0]:  # 의료
    st.subheader("👩‍⚕️ 의료 관련 직업")
    st.markdown("- 👨‍⚕️ 의사")
    st.markdown("- 🧑‍⚕️ 간호사")
    st.markdown("- 🦷 치과의사")
    st.markdown("- 👁️‍🗨️ 안과의사")
    st.markdown("- 🧬 임상병리사")

with tabs[1]:  # IT/공학
    st.subheader("🧑‍💻 IT · 공학 직업")
    st.markdown("- 👨‍💻 프로그래머")
    st.markdown("- 🧠 AI 개발자")
    st.markdown("- 🧑‍🔧 로봇공학자")
    st.markdown("- 🌐 웹 개발자")
    st.markdown("- 🧑‍🚀 항공우주공학자")

with tabs[2]:  # 예술/디자인
    st.subheader("🎨 예술 · 디자인 직업")
    st.markdown("- 👩‍🎨 그래픽 디자이너")
    st.markdown("- 🎬 영화감독")
    st.markdown("- 📸 사진작가")
    st.markdown("- 👗 패션 디자이너")
    st.markdown("- 🎨 일러스트레이터")

with tabs[3]:  # 교육
    st.subheader("🎓 교육 관련 직업")
    st.markdown("- 👨‍🏫 교사")
    st.markdown("- 📚 교육행정가")
    st.markdown("- 🧑‍💼 진로상담사")
    st.markdown("- 🧠 특수교육교사")

with tabs[4]:  # 공공서비스
    st.subheader("🚓 공공 서비스 직업")
    st.markdown("- 👮 경찰")
    st.markdown("- 👨‍🚒 소방관")
    st.markdown("- 🏛️ 공무원")
    st.markdown("- ⚖️ 판사 / 검사 / 변호사")

with tabs[5]:  # 미디어/연예
    st.subheader("📺 미디어 · 연예")
    st.markdown("- 🎤 가수")
    st.markdown("- 🎭 배우")
    st.markdown("- 📰 기자")
    st.markdown("- 🎧 음향엔지니어")
    st.markdown("- 🎮 게임 스트리머")

with tabs[6]:  # 자연/환경
    st.subheader("🌾 자연 · 환경 관련 직업")
    st.markdown("- 👨‍🌾 농부")
    st.markdown("- 🧑‍🔬 환경연구원")
    st.markdown("- 🐾 생물학자")
    st.markdown("- 🌋 지질학자")

