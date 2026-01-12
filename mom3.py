import streamlit as st
import pandas as pd
from datetime import datetime
import time

# --- 1. 페이지 설정 및 디자인 ---
st.set_page_config(page_title="LAMP: 심리 치유 완결판", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #F5FFFA; }
    .stMultiSelect div div div div div { background-color: #3EB489 !important; color: white !important; }
    div.stButton > button:first-child { background-color: #3EB489; color: white; border-radius: 20px; font-weight: bold; }
    .info-box { padding: 15px; border-radius: 10px; background-color: #E0FFF0; border-left: 5px solid #3EB489; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

if 'journal' not in st.session_state: st.session_state.journal = []

# --- 사이드바 ---
st.sidebar.title("🌿 LAMP 완결 가이드")
choice = st.sidebar.radio("단계별 이동", [
    "홈: 걱정의 원리",
    "L: 걱정 모니터링 & 유형분류",
    "A: 통제욕구 버리기 (이완)",
    "M: 수직 화살표 & 사실검증",
    "P: 5-4-3-2-1 접지 & 행동",
    "Special: 3단계 대화법",
    "📂 나의 치유 데이터"
])

# --- [홈: 걱정의 진행과정 보완] ---
if choice == "홈: 걱정의 원리":
    st.title("🌱 당신의 걱정은 어떻게 진행되나요?")
    st.markdown('<div class="info-box">문서 1부: 걱정은 <b>사건 → 침투적 생각 → 메타걱정 → 감정/신체 반응</b>의 사슬로 이어집니다.</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        # 사진 크기 작게 조정
        st.image("https://images.unsplash.com/photo-1494438639946-1ebd1d20bf85?auto=format&fit=crop&w=400&q=80", caption="고요함으로 가는 길")
    
    st.subheader("💡 잊지 마세요")
    st.write("- 미래는 통제할 수 없습니다.")
    st.write("- 걱정은 문제를 해결해주지 않습니다.")
    st.write("- 생각은 실제 사건이 아닌 뇌의 활동일 뿐입니다.")

# --- [L: 유형 분류 보완] ---
elif choice == "L: 걱정 모니터링 & 유형분류":
    st.header("🏷️ Step 1. 세밀한 이름표 붙이기")
    
    # 문서 1부의 걱정 유형 구체화
    WORRY_TYPES = ["대인관계(거절, 비난)", "완벽주의(실수, 실패)", "건강/안전", "경제적 문제", "미래의 불확실성", "사소한 일상(지각 등)"]
    
    col1, col2 = st.columns(2)
    with col1:
        thought = st.text_input("지금 포착된 생각", placeholder="예: 내가 한 말이 무례하게 들렸을까?")
        w_type = st.selectbox("어떤 유형의 걱정인가요?", WORRY_TYPES)
        intensity = st.select_slider("감정 농도", options=range(0, 101, 10), value=50)
        
        # 메타걱정 기능 추가 (문서의 핵심)
        st.write("---")
        meta_worry = st.checkbox("이 걱정 때문에 '내가 미칠 것 같다'거나 '큰일 날 것 같다'는 걱정이 또 드나요? (메타걱정)")
        
    with col2:
        emotions = st.multiselect("감정 버튼 (복수 선택)", ["불안", "후회", "자괴감", "막막함", "분노", "창피함", "초조"])
        sensations = st.multiselect("신체 버튼 (복수 선택)", ["가슴 답답", "심장 두근", "어깨 통증", "두통", "목 이물감", "입마름"])
        observer = st.text_area("관찰자 시점", placeholder="그녀는 과거의 대화를 반추하며 '사회적 유능감'에 대해 걱정하고 있다.")

    if st.button("Step 1 저장"):
        st.session_state.temp_data = {
            "thought": thought, "type": w_type, "intensity": intensity, 
            "emotions": emotions, "sensations": sensations, 
            "meta": meta_worry, "observer": observer
        }
        st.success("걱정의 실체를 성공적으로 분류했습니다.")

# --- [A: 이완 보완] ---
elif choice == "A: 통제 내려놓기 (이완)":
    st.header("🍃 Step 2. 몸과 마음의 긴장 풀기")
    st.info("문서 2부: 통제하려는 시도가 불안을 키웁니다. 그냥 두세요.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("🧘 4-7-8 호흡")
        if st.button("호흡 타이머 시작"):
            progress = st.progress(0)
            for i in range(1, 11): # 연습용 10초
                time.sleep(1)
                progress.progress(i * 10)
            st.success("호흡 주기를 마쳤습니다.")
    with col2:
        st.subheader("💪 근육 이완")
        st.write("힘을 5초간 꽉 줬다가 툭! 빼세요.")
        parts = ["눈/미간", "어깨/목", "주먹/팔", "허벅지/발"]
        for p in parts: st.checkbox(p)

# --- [M: 수직 화살표 보완] ---
elif choice == "M: 수직 화살표 & 사실검증":
    st.header("🤝 Step 3. 생각 받아들이기")
    st.markdown('<div class="info-box">수직 화살표 기법: 걱정의 끝까지 내려가서 그 정체가 무엇인지 확인하세요.</div>', unsafe_allow_html=True)
    
    q1 = st.text_input("그 걱정이 사실이라면, 당신에게 어떤 의미인가요?")
    q2 = st.text_input("그래서 일어날 수 있는 '최악의 결과'는 무엇인가요?")
    
    st.divider()
    st.subheader("🔍 사실인가, 생각인가?")
    c1, c2 = st.columns(2)
    with c1: st.text_area("걱정을 뒷받침하는 현실적 증거")
    with c2: st.text_area("걱정이 틀렸음을 보여주는 반대 증거")

# --- [P: 행동 계획 보완] ---
elif choice == "P: 5-4-3-2-1 접지 & 행동":
    st.header("📍 Step 4. 현재로 돌아오는 닻 내리기")
    st.write("오감을 사용하여 뇌를 '지금 여기'로 소환합니다.")
    
    c1, c2 = st.columns(2)
    with c1:
        st.text_input("👀 보이는 것 3가지")
        st.text_input("👂 들리는 소리 2가지")
        st.text_input("🖐️ 닿아있는 촉감 1가지")
    with c2:
        action = st.text_input("걱정 대신 지금 할 수 있는 '작은 행동'", placeholder="예: 3분간 산책하기")
        if st.button("치유 여정 마침"):
            if 'temp_data' in st.session_state:
                final = st.session_state.temp_data
                final.update({"action": action, "date": datetime.now().strftime("%Y-%m-%d %H:%M")})
                st.session_state.journal.append(final)
                st.balloons()
                st.success("전체 과정이 기록되었습니다.")

# --- [Special: 대화법] ---
elif choice == "Special: 3단계 대화법":
    st.header("🗣️ 공격적이지 않은 대화 훈련")
    st.info("문서 마지막: 사실 - 감정 - 요청의 흐름을 지키세요.")
    
    with st.expander("연습하기 (예시: 상대방이 무례한 말을 했을 때)"):
        st.write("1. **사실**: 네가 그런 말을 했을 때")
        st.write("2. **감정**: 나는 당황스럽고 상처를 받았어")
        st.write("3. **요청**: 다음부턴 조금 더 조심해서 말해줄 수 있니?")
    
    st.text_area("당신의 상황에 대입해 보세요")
    if st.button("대화법 저장"): st.success("연습 기록이 저장되었습니다.")

# --- [📂 히스토리 보완] ---
elif choice == "📂 나의 치유 데이터":
    st.header("📊 마음 모니터링 분석")
    if not st.session_state.journal:
        st.info("기록이 없습니다.")
    else:
        df = pd.DataFrame(st.session_state.journal)
        st.line_chart(df['intensity']) # 감정 농도 변화 그래프
        
        for log in reversed(st.session_state.journal):
            with st.expander(f"📌 {log['date']} | {log['thought'][:15]}... ({log['type']})"):
                st.write(f"**🎭 감정:** {', '.join(log['emotions'])} / **농도:** {log['intensity']}%")
                st.write(f"**⚡ 신체:** {', '.join(log['sensations'])}")
                if log['meta']: st.warning("⚠️ 메타걱정(걱정에 대한 걱정)이 동반되었습니다.")
                st.info(f"**🕵️ 관찰 기록:** {log['observer']}")
                st.success(f"**✅ 실천:** {log['action']}")