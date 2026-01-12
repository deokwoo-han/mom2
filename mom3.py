import streamlit as st
import pandas as pd
from datetime import datetime
import time

# --- 앱 설정 ---
st.set_page_config(page_title="LAMP: 마음 치유 풀코스", layout="wide")

# CSS: 연한 주황색 버튼 및 칩 스타일
st.markdown("""
    <style>
    .stMultiSelect div div div div div { background-color: #FFB347 !important; color: white !important; border-radius: 12px !important; }
    .stApp { background-color: #FFF9F0; }
    div.stButton > button:first-child { background-color: #FFB347; color: white; border-radius: 20px; border: none; width: 100%; }
    .step-box { padding: 20px; border-radius: 15px; background-color: #FFEBC1; border-left: 5px solid #FFB347; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

# 데이터 저장소
if 'worry_db' not in st.session_state: st.session_state.worry_db = []

# --- 사이드바 메뉴 (문서 파트별 구성) ---
st.sidebar.title("🍊 LAMP 치유 센터")
menu = st.sidebar.radio("단계별 훈련", [
    "홈: 오늘의 가이드",
    "Step 1: Labeling (이름표 붙이기)",
    "Step 2: Abandoning (통제욕구 버리기)",
    "Step 3: Mindful Acceptance (받아들이기)",
    "Step 4: Present (현재에 충실하기)",
    "Special: 마음을 전하는 대화법",
    "📂 전체 기록 확인"
])

# --- 홈 화면 ---
if menu == "홈: 오늘의 가이드":
    st.title("🕯️ 당신의 걱정을 밝히는 LAMP")
    st.markdown(f"""
    <div class="step-box">
    <h3>오늘 당신의 마음은 어떤가요?</h3>
    문서의 핵심인 4단계 치유법을 따라가며 걱정에서 벗어나 보세요. <br><br>
    <b>L</b>abeling: 걱정에 이름표를 붙여 거리 두기 <br>
    <b>A</b>bandoning: 통제할 수 없는 것을 내려놓는 이완 <br>
    <b>M</b>indful Acceptance: 두려움의 정체를 직면하고 수용 <br>
    <b>P</b>resent: 현재 순간의 감각에 집중하기
    </div>
    """, unsafe_allow_html=True)
    st.image("https://images.unsplash.com/photo-1506126613408-eca07ce68773?ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&q=80", caption="고요한 마음을 위한 여정")

# --- Step 1: Labeling (기존 기능 강화) ---
elif menu == "Step 1: Labeling (이름표 붙이기)":
    st.header("🏷️ Step 1. 걱정에 이름표 붙이기")
    col1, col2 = st.columns(2)
    
    with col1:
        thought = st.text_input("지금 떠오른 생각", placeholder="예: 프로젝트가 망하면 어떡하지?")
        intensity = st.select_slider("감정 농도", options=range(0, 101, 10), value=50)
        emotions = st.multiselect("느껴지는 감정 (버튼식)", ["초조함", "막막함", "자책", "두려움", "압박감", "억울함", "허무함"])
        
    with col2:
        sensations = st.multiselect("신체 반응 (버튼식)", ["가슴 답답", "심장 뜀", "어깨 뭉침", "두통", "목 이물감", "손 떨림"])
        label = st.selectbox("생각의 정체", ["소모적 걱정", "과거 반추", "실행 가능한 계획", "단순 사실"])
        observer = st.text_area("제3자의 시선 (관찰 일기)", placeholder="그녀는 미래를 걱정하며 몸이 긴장된 상태다.")

    if st.button("Step 1 완료 및 저장"):
        st.session_state.temp_data = {"thought": thought, "intensity": intensity, "emotions": emotions, "sensations": sensations, "label": label, "observer": observer}
        st.success("생각을 성공적으로 포착했습니다! 이제 Step 2로 이동하여 긴장을 풀어보세요.")

# --- Step 2: Abandoning (신규: 이완 훈련) ---
elif menu == "Step 2: Abandoning (통제욕구 버리기)":
    st.header("🍃 Step 2. 통제욕구 버리기 & 이완")
    st.info("문서 2부: 몸의 긴장을 풀고 마음을 흘러가게 두는 연습입니다.")
    
    tab1, tab2 = st.tabs(["복식 호흡 훈련", "근육 이완 체크리스트"])
    
    with tab1:
        st.subheader("🧘 4-7-8 호흡 가이드")
        st.write("1. 4초간 코로 숨을 들이마십니다. (배가 부풀어 오르게)")
        st.write("2. 7초간 숨을 참습니다.")
        st.write("3. 8초간 입으로 천천히 내뱉습니다.")
        if st.button("호흡 시작 (1분 타이머)"):
            progress_bar = st.progress(0)
            for i in range(100):
                time.sleep(0.6)
                progress_bar.progress(i + 1)
            st.balloons()
            st.success("몸이 한결 가벼워졌기를 바랍니다.")

    with tab2:
        st.subheader("💪 점진적 근육 이완 (PMR)")
        st.caption("문서에 나온 대로 부위별 긴장을 5초간 줬다가 한 번에 툭! 풀어보세요.")
        st.checkbox("주먹을 꽉 쥐었다가 풀기")
        st.checkbox("어깨를 귀까지 끌어올렸다가 풀기")
        st.checkbox("눈과 입을 꽉 다물었다가 풀기")
        st.checkbox("발가락을 오므렸다가 풀기")

# --- Step 3: Mindful Acceptance (신규: 직면 훈련) ---
elif menu == "Step 3: Mindful Acceptance (받아들이기)":
    st.header("🤝 Step 3. 생각과 감정 받아들이기")
    st.info("문서 3부: 두려움의 실체를 파악하고 수용하는 단계입니다.")
    
    st.subheader("🎯 수직 화살표 기법 (Vertical Arrow)")
    q1 = st.text_input("1. 그 걱정이 사실이라면, 당신에게 어떤 의미인가요?", placeholder="예: 나는 실패자라는 뜻이에요.")
    q2 = st.text_input("2. 그것이 사실이라면, 최악의 상황은 무엇인가요?", placeholder="예: 모두가 나를 비웃을 거예요.")
    
    st.subheader("🔍 사실 검증 (Fact Check)")
    col1, col2 = st.columns(2)
    with col1:
        st.text_area("걱정을 뒷받침하는 증거", placeholder="예: 지난번에도 실수를 했다.")
    with col2:
        st.text_area("반대되는 증거", placeholder="예: 하지만 동료들은 나를 도와주었다.")
    
    accept = st.button("두려움을 있는 그대로 수용하기")
    if accept:
        st.warning("이것은 단지 '생각'일 뿐이며, 내 안전을 위협하는 실제 사건이 아님을 인정합니다.")

# --- Step 4: Present (신규: 감각 접지) ---
elif menu == "Step 4: Present (현재에 충실하기)":
    st.header("📍 Step 4. 현재 순간에 충실하기")
    st.info("문서 4부: 지금 이 순간, 내 주변의 감각에 집중하여 닻을 내립니다.")
    
    st.subheader("🖐️ 5-4-3-2-1 접지법 (Grounding)")
    st.text_input("👁️ 눈에 보이는 것 3가지", placeholder="책상, 컵, 창밖의 나무...")
    st.text_input("👂 들리는 소리 2가지", placeholder="시계 소리, 멀리서 들리는 차 소리...")
    st.text_input("🖐️ 몸에 닿는 느낌 1가지", placeholder="의자의 딱딱함, 옷감의 촉감...")
    
    st.subheader("🏃 작은 행동 계획")
    st.write("걱정 대신 지금 바로 할 수 있는 '아주 작은 일' 하나를 정해보세요.")
    action = st.text_input("예: 물 한 잔 마시기, 책상 1분 정리하기")
    
    if st.button("현재로 돌아오기 완료"):
        if 'temp_data' in st.session_state:
            final_entry = st.session_state.temp_data
            final_entry.update({"action": action, "date": datetime.now().strftime("%Y-%m-%d %H:%M")})
            st.session_state.worry_db.append(final_entry)
            st.success("모든 치유 과정을 마치고 기록되었습니다!")

# --- Special: Communication (신규: 대화법) ---
elif menu == "Special: 마음을 전하는 대화법":
    st.header("🗣️ 마음을 전하는 3단계 대화법")
    st.info("문서 마지막 파트: 공격적이지 않게 내 필요를 전달하는 훈련입니다.")
    
    st.markdown("""
    <div class="step-box">
    <b>1단계: 상황을 객관적으로 말하기</b> (비난 없이)<br>
    <b>2단계: 내 감정 전달하기</b> ('나' 화법 사용)<br>
    <b>3단계: 구체적으로 요청하기</b> (부탁의 형식)
    </div>
    """, unsafe_allow_html=True)
    
    situation = st.text_area("바꾸고 싶은 상황", placeholder="예: 친구가 약속에 늦었을 때")
    practice = st.text_area("연습해보기", placeholder="네가 늦게 올 때(사실), 난 기다리며 조금 지쳤어(감정). 다음엔 미리 연락 줄래?(요청)")
    
    if st.button("대화법 연습 저장"):
        st.success("일상에서 이대로 한 번 말해보세요!")

# --- 📂 전체 기록 확인 ---
elif menu == "📂 전체 기록 확인":
    st.header("📖 나의 치유 여정 리스트")
    if not st.session_state.worry_db:
        st.info("기록된 일지가 없습니다.")
    else:
        for log in reversed(st.session_state.worry_db):
            with st.expander(f"📌 {log['date']} | {log['thought']} ({log.get('label', '미분류')})"):
                st.write(f"**🎭 감정:** {', '.join(log.get('emotions', []))} ({log.get('intensity', '0%')})")
                st.write(f"**⚡ 신체 감각:** {', '.join(log.get('sensations', []))}")
                st.write(f"**🕵️ 관찰자:** {log.get('observer', '기록 없음')}")
                st.info(f"**✅ 실천 계획:** {log.get('action', '없음')}")