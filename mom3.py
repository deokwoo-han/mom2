import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. 페이지 설정 및 스타일 ---
st.set_page_config(page_title="스트레스와 불안 다루기", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #F9FCFF; }
    .main-header { font-size: 2rem; color: #2C3E50; font-weight: bold; margin-bottom: 20px; }
    .sub-header { font-size: 1.5rem; color: #34495E; margin-top: 20px; margin-bottom: 10px; }
    .card { background-color: white; padding: 20px; border-radius: 15px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); margin-bottom: 15px; }
    .highlight { color: #E67E22; font-weight: bold; }
    .stButton>button { border-radius: 20px; height: 45px; width: 100%; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. 데이터 세션 초기화 ---
if 'thoughts' not in st.session_state: st.session_state.thoughts = []
if 'ruminations' not in st.session_state: st.session_state.ruminations = []
if 'monitoring_logs' not in st.session_state: st.session_state.monitoring_logs = []
if 'journal_entries' not in st.session_state: st.session_state.journal_entries = []

# --- 3. 사이드바 메뉴 (워드 파일의 치유법 카테고리화) ---
st.sidebar.image("https://images.unsplash.com/photo-1515847049296-a281d6401047?w=300", caption="마음의 평온")
st.sidebar.title("🌿 치유 훈련 카테고리")
menu = st.sidebar.radio("단계 선택", [
    "홈: 걱정의 원리",
    "1. 걱정에 이름표 붙이기 (생각 잡기)",
    "2. 과거 반추 기록 (시간 돌리기)",
    "3. 인식 훈련 (계획 vs 소모)",
    "4. 걱정 주제 및 신체 감각",
    "5. 걱정 모니터링 연습",
    "📒 [종합] 제3자의 시선 걱정 일지"
])

# --- 메인 기능 구현 ---

if menu == "홈: 걱정의 원리":
    st.markdown("<div class='main-header'>🌱 당신의 걱정은 어떻게 작동하나요?</div>", unsafe_allow_html=True)
    st.markdown("""
    <div class='card'>
        <h3>걱정의 사슬 끊기</h3>
        <p>워드 문서에 따르면 걱정은 <b>사건 → 침투적 생각 → 메타걱정 → 신체 반응</b>으로 이어집니다.</p>
        <ul>
            <li><b>미래는 통제할 수 없습니다:</b> 불확실함을 받아들이고 현재에 집중하세요.</li>
            <li><b>인지적 탈융합:</b> 생각은 실제 사건이 아닙니다. 뇌가 만들어낸 신호일 뿐입니다.</li>
            <li><b>램프(LAMP) 치유법:</b> 1~5단계를 통해 걱정을 수용하고 가치 있는 행동으로 나아갑니다.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# --------------------------------------------------------------------------
# 1. 걱정에 이름표 붙이기 (생각 잡기 & 감정 농도)
# --------------------------------------------------------------------------
elif menu == "1. 걱정에 이름표 붙이기 (생각 잡기)":
    st.markdown("<div class='main-header'>🏷️ 1단계: 생각에 이름표 붙이기</div>", unsafe_allow_html=True)
    st.info("머릿속을 지나가는 단어를 '탁' 잡아서 이름표를 붙여보세요. 그 생각에는 어떤 감정이 묻어있나요?")

    col1, col2 = st.columns([1, 1])
    
    with col1:
        with st.form("thought_form"):
            st.markdown("### 🪤 생각 잡기")
            thought_word = st.text_input("지금 머릿속을 스치는 단어/생각은?", placeholder="예: 실수하면 어떡하지, 사람들이 날 싫어해...")
            
            st.markdown("### 🌡️ 감정 농도 (0~100)")
            intensity = st.slider("이 생각에 묻어있는 감정의 진하기", 0, 100, 50)
            
            emotions = st.multiselect("함께 느껴지는 감정들", 
                ["불안", "두려움", "수치심", "초조", "막막함", "분노", "우울", "죄책감"])
            
            submit = st.form_submit_button("이름표 붙여 저장하기")
            
            if submit and thought_word:
                st.session_state.thoughts.append({
                    "word": thought_word,
                    "intensity": intensity,
                    "emotions": emotions,
                    "date": datetime.now().strftime("%Y-%m-%d %H:%M")
                })
                st.success("생각을 잡아두었습니다.")

    with col2:
        st.markdown("### 👁️ 머물러 서서 관찰하기")
        if not st.session_state.thoughts:
            st.write("아직 잡힌 생각이 없습니다.")
        else:
            st.write("아래 리스트를 클릭하여 거리를 두고 관찰해보세요.")
            for idx, item in enumerate(reversed(st.session_state.thoughts)):
                with st.expander(f"💭 {item['word']} (농도: {item['intensity']}%)"):
                    st.write(f"**부착된 감정:** {', '.join(item['emotions'])}")
                    st.write(f"**포착 시간:** {item['date']}")
                    st.info("이것은 당신의 뇌가 만들어낸 '지나가는 생각'일 뿐입니다. 사실이 아닙니다.")

# --------------------------------------------------------------------------
# 2. 과거 반추 기록
# --------------------------------------------------------------------------
elif menu == "2. 과거 반추 기록 (시간 돌리기)":
    st.markdown("<div class='main-header'>⏪ 2단계: 과거 반추 다루기</div>", unsafe_allow_html=True)
    st.warning("과거의 일에 대해 '왜?'라고 묻는 것은 답이 없는 질문입니다. (문서 '지나간 일 되새기기' 중)")

    with st.container():
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        past_situation = st.text_area("자주 떠오르는 과거의 특정 상황은 무엇인가요?", height=100)
        past_emotion = st.text_input("그 당시, 혹은 지금 느껴지는 주요 감정은?")
        
        if st.button("반추 기록하기"):
            if past_situation:
                st.session_state.ruminations.append({
                    "situation": past_situation,
                    "emotion": past_emotion,
                    "date": datetime.now().strftime("%Y-%m-%d")
                })
                st.success("기록되었습니다. 과거는 통제할 수 없음을 인정하고 흘려보냅니다.")
        st.markdown("</div>", unsafe_allow_html=True)

    if st.session_state.ruminations:
        st.subheader("📜 반추 기록 보관함")
        for item in st.session_state.ruminations:
            st.write(f"- **상황:** {item['situation']} | **감정:** {item['emotion']}")

# --------------------------------------------------------------------------
# 3. 인식 훈련 (계획 vs 소모적 걱정)
# --------------------------------------------------------------------------
elif menu == "3. 인식 훈련 (계획 vs 소모)":
    st.markdown("<div class='main-header'>⚖️ 3단계: 걱정 성격 구분하기 (인식 훈련 4)</div>", unsafe_allow_html=True)
    st.markdown("지금 하고 있는 걱정이 **문제 해결을 위한 계획**인지, 에너지만 갉아먹는 **소모적 걱정**인지 구분합니다.")

    worry_content = st.text_input("지금 당신을 괴롭히는 걱정은 무엇인가요?")
    
    check_type = st.radio("이 걱정의 결과는 어디에 가깝나요?", 
        ["A. 구체적인 행동과 예방 조치를 세우고 있다. (계획)", 
         "B. 불안이 계속 커지고, 일을 미루거나 회피하게 된다. (소모적 걱정)"])

    if st.button("판단 결과 확인"):
        if "A" in check_type:
            st.success("✅ 이것은 **'계획 세우기'**입니다. 준비된 계획을 실행에 옮기세요.")
        else:
            st.error("🛑 이것은 **'소모적인 걱정'**입니다. (문서 참조)")
            st.markdown("""
            **솔루션:**
            - 이 걱정은 문제 해결에 도움이 되지 않습니다.
            - '어쩔 수 없지'라고 인정하고 현재의 감각(호흡 등)으로 돌아오세요.
            """)

# --------------------------------------------------------------------------
# 4. 걱정 주제 및 신체 감각
# --------------------------------------------------------------------------
elif menu == "4. 걱정 주제 및 신체 감각":
    st.markdown("<div class='main-header'>🗂️ 4단계: 주제 분류 및 신체 감각</div>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 📂 걱정 주제 분류")
        topic = st.selectbox("이 걱정은 어떤 카테고리에 속하나요?", 
            ["관계 (가족/친구/연인)", "직장/커리어", "건강/질병", "재정/돈", "미래의 불확실성", "기타"])
        st.info(f"선택한 주제: **{topic}**")

    with col2:
        st.markdown("### ⚡ 동반되는 신체 감각")
        st.write("걱정할 때 몸에서 어떤 반응이 일어나나요? (문서 '신체감각 알아보기')")
        body_symptoms = st.multiselect("신체 반응 체크", 
            ["심장이 쿵쾅거림", "가슴이 답답함", "소화불량/속쓰림", "근육 긴장/어깨 뭉침", 
             "손발에 땀이 남", "머리가 지끈거림", "호흡이 가빠짐"])
        
    if st.button("상태 저장"):
        st.success(f"주제 [{topic}]와 신체 반응 {body_symptoms}을 인식했습니다. 몸의 반응을 있는 그대로 허용하세요.")

# --------------------------------------------------------------------------
# 5. 걱정 모니터링 연습
# --------------------------------------------------------------------------
elif menu == "5. 걱정 모니터링 연습":
    st.markdown("<div class='main-header'>🔍 5단계: 걱정 모니터링 연습</div>", unsafe_allow_html=True)
    st.markdown("걱정의 발생부터 행동까지의 과정을 추적합니다.")
    
    with st.form("monitoring_form"):
        trigger = st.text_input("1. 촉발 사건 (무슨 일이 있었나요?)")
        thought_process = st.text_area("2. 생각/감정/신체반응 (어떤 생각과 느낌이 들었나요?)")
        action = st.text_input("3. 행동 반응 (그래서 무엇을 했나요? 예: 회피, 확인, 검색)")
        
        if st.form_submit_button("모니터링 기록 저장"):
            st.session_state.monitoring_logs.append({
                "trigger": trigger,
                "process": thought_process,
                "action": action,
                "date": datetime.now().strftime("%Y-%m-%d %H:%M")
            })
            st.success("객관적 모니터링이 완료되었습니다.")

# --------------------------------------------------------------------------
# [종합] 제3자의 시선 걱정 일지
# --------------------------------------------------------------------------
elif menu == "📒 [종합] 제3자의 시선 걱정 일지":
    st.markdown("<div class='main-header'>📒 종합 걱정 일지</div>", unsafe_allow_html=True)
    st.markdown("""
    <div class='info-box' style='background-color:#FFF3CD; padding:15px; border-radius:10px;'>
    <b>지침:</b> 앞서 훈련한 이름표 붙이기, 주제 분류, 신체 감각 등을 종합하여 기록합니다.<br>
    중요한 것은 <b>'나'의 입장이 아닌, 전지전능한 '제3자(관찰자)'의 시선</b>으로 서술하는 것입니다.
    </div>
    """, unsafe_allow_html=True)
    
    with st.form("journal_form"):
        st.markdown("### 📝 오늘의 관찰 일지")
        
        # 이전 단계들의 데이터를 참고용으로 보여줄 수 있음
        if st.session_state.thoughts:
            last_thought = st.session_state.thoughts[-1]['word']
            st.caption(f"최근 잡힌 생각: '{last_thought}'")
            
        journal_content = st.text_area("예시: '철수는 오늘 상사의 표정을 보고 불안해했다. 가슴이 뛰는 것을 느꼈지만, 그것을 단지 신체 반응으로 여기고 업무에 집중했다.'", height=150)
        
        if st.form_submit_button("일지 완성 및 저장"):
            st.session_state.journal_entries.append({
                "content": journal_content,
                "date": datetime.now().strftime("%Y-%m-%d %H:%M")
            })
            st.balloons()
            st.success("훌륭합니다! 당신은 걱정과 당신을 분리하는 데 성공했습니다.")

    # 저장된 일지 보기
    if st.session_state.journal_entries:
        st.divider()
        st.subheader("📂 지난 기록들")
        for entry in reversed(st.session_state.journal_entries):
            st.markdown(f"""
            <div class='card'>
                <small style='color:gray'>{entry['date']}</small><br>
                {entry['content']}
            </div>
            """, unsafe_allow_html=True)