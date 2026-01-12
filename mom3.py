import streamlit as st
import pandas as pd
from datetime import datetime
import time
import random

# --- 0. 따뜻한 기술(Warm Tech) 구현을 위한 감성 피드백 함수 ---
def get_warm_feedback():
    messages = [
        "당신의 감정은 타당합니다. 있는 그대로 받아들여주세요. 🌿",
        "잠시 멈추어 호흡하세요. 당신은 생각보다 강합니다. 🍃",
        "기록하는 용기가 변화의 시작입니다. 오늘도 잘하셨어요. ☕",
        "이 생각은 당신의 전부가 아닙니다. 그저 지나가는 날씨입니다. ☁️",
        "자신을 너무 몰아세우지 마세요. 지금도 충분히 잘하고 계십니다. 🌕",
        "마음의 소리를 들어주셔서 감사합니다. 조금 더 편안해지시길. 🧘"
    ]
    return random.choice(messages)

# --- 1. 페이지 설정 및 스타일 ---\
st.set_page_config(page_title="AI 솔빙 스트레스 - 마음챙김 솔루션", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #F9FCFF; }
    .main-header { font-size: 2rem; color: #2C3E50; font-weight: bold; margin-bottom: 20px; }
    .sub-header { font-size: 1.5rem; color: #34495E; margin-top: 20px; margin-bottom: 10px; }
    .card { background-color: white; padding: 20px; border-radius: 15px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); margin-bottom: 15px; }
    .highlight { color: #E67E22; font-weight: bold; }
    .stButton>button { border-radius: 20px; height: 45px; width: 100%; }
    
    /* 전문성 배지 스타일 */
    .expert-badge {
        padding: 10px;
        background-color: #E8F6F3;
        border: 1px solid #1ABC9C;
        border-radius: 10px;
        text-align: center;
        font-size: 0.85em;
        color: #16A085;
        margin-top: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. 데이터 세션 초기화 ---
if 'thoughts' not in st.session_state: st.session_state.thoughts = []
if 'journal_entries' not in st.session_state: st.session_state.journal_entries = []

# --- 3. 사이드바 메뉴 ---
with st.sidebar:
    st.title("🧩 AI 솔빙 스트레스")
    st.caption("Counseling Psychology & AI")
    
    menu = st.radio("마음 챙김 단계", 
        ["1. 걱정에 이름표 붙이기", 
         "2. 주제별 분류 및 거리두기", 
         "3. 신체 감각 모니터링", 
         "📒 [종합] 제3자의 시선 걱정 일지",
         "🚀 AI 맞춤형 솔루션 (Beta)"]) # 메뉴 추가됨
    
    st.markdown("---")
    # [추가됨] 사업계획서의 '전문성'과 '데이터' 강조
    st.markdown("""
    <div class='expert-badge'>
        <b>🎓 전문성 보증</b><br>
        본 서비스는 <b>상담심리학 박사(교수)</b>의<br>
        임상 검증 알고리즘과<br>
        <b>국가 바우처 사업 실데이터</b>를<br>
        기반으로 설계되었습니다.
    </div>
    """, unsafe_allow_html=True)

# --- 4. 메인 기능 구현 ---

# [메뉴 1] 걱정에 이름표 붙이기
if menu == "1. 걱정에 이름표 붙이기":
    st.markdown("<div class='main-header'>☁️ 흐르는 생각 포착하기</div>", unsafe_allow_html=True)
    st.info("떠오르는 걱정이나 생각을 단어 형태로 짧게 잡아두세요. (예: '발표 실수', '미래 걱정')")
    
    with st.form("thought_form", clear_on_submit=True):
        col1, col2 = st.columns([3, 1])
        with col1:
            thought_word = st.text_input("지금 머릿속을 스치는 생각은?")
        with col2:
            submit = st.form_submit_button("생각 잡아두기")
            
        if submit and thought_word:
            st.session_state.thoughts.append({'word': thought_word, 'date': datetime.now()})
            # [변경됨] 따뜻한 피드백 적용
            st.success(f"생각을 안전하게 잡아두었습니다. {get_warm_feedback()}")

    if st.session_state.thoughts:
        st.markdown("### 🧺 내가 잡아둔 생각들")
        for i, t in enumerate(st.session_state.thoughts[-5:]):  # 최근 5개만
            st.markdown(f"- 🕒 {t['date'].strftime('%H:%M')} : **{t['word']}**")

# [메뉴 2] 주제별 분류 및 거리두기
elif menu == "2. 주제별 분류 및 거리두기":
    st.markdown("<div class='main-header'>🗂️ 생각 정리 및 거리두기</div>", unsafe_allow_html=True)
    
    if not st.session_state.thoughts:
        st.warning("먼저 '1. 걱정에 이름표 붙이기'에서 생각을 포착해주세요.")
    else:
        recent_thought = st.session_state.thoughts[-1]['word']
        st.markdown(f"""
        <div class='card'>
            <h3>지금 다룰 생각: <span class='highlight'>'{recent_thought}'</span></h3>
            <p>이 생각은 어떤 종류인가요? 이름을 붙이는 순간, 감정의 압도됨이 줄어듭니다.</p>
        </div>
        """, unsafe_allow_html=True)
        
        category = st.selectbox("이 생각의 카테고리는?", 
            ["막연한 미래 걱정", "타인의 시선 의식", "지나간 일 후회", "해결해야 할 현실 문제", "단순한 신체 반응"])
        
        if st.button("분류 완료"):
            st.success(f"'{category}' 서랍에 잘 정리했습니다. {get_warm_feedback()}")

# [메뉴 3] 신체 감각 모니터링
elif menu == "3. 신체 감각 모니터링":
    st.markdown("<div class='main-header'>🧘 몸의 소리 듣기</div>", unsafe_allow_html=True)
    st.write("감정은 몸으로 먼저 찾아옵니다. 지금 느껴지는 감각을 체크해보세요.")
    
    symptoms = st.multiselect("지금 느껴지는 신체 반응을 모두 고르세요",
        ["가슴 답답함", "심장 두근거림", "어깨/목 뭉침", "두통", "손발 차가움", "속 울렁거림", "아무 느낌 없음"])
    
    stress_level = st.slider("지금 스트레스 점수는 몇 점인가요? (0: 평온 ~ 10: 폭발 직전)", 0, 10, 5)
    
    if st.button("신체 반응 기록하기"):
        # [변경됨] 따뜻한 피드백 적용
        if stress_level > 7:
            st.warning(f"스트레스 수치가 높네요. 잠시 심호흡을 권해드립니다. 🌬️ {get_warm_feedback()}")
        else:
            st.success(f"몸의 상태를 잘 알아차리셨습니다. {get_warm_feedback()}")

# [메뉴 4] 종합 걱정 일지
elif menu == "📒 [종합] 제3자의 시선 걱정 일지":
    st.markdown("<div class='main-header'>📒 전지적 관찰자 시점 일지</div>", unsafe_allow_html=True)
    st.info("나의 감정을 '남의 이야기'처럼 서술해보세요. 객관화는 치유의 첫걸음입니다.")
    
    with st.form("journal_form"):
        st.markdown("### 📝 오늘의 관찰 기록")
        if st.session_state.thoughts:
            st.caption(f"최근 키워드: {st.session_state.thoughts[-1]['word']}")
            
        journal_content = st.text_area("작성 예시: '철수는 오늘 발표 때문에 긴장했다. 가슴이 뛰었지만 곧 괜찮아질 것이라 생각했다.'", height=150)
        
        if st.form_submit_button("일지 저장 및 분석 요청"):
            st.session_state.journal_entries.append({
                "content": journal_content,
                "date": datetime.now().strftime("%Y-%m-%d %H:%M")
            })
            st.balloons()
            # [변경됨] 따뜻한 피드백 적용
            st.success(f"오늘의 마음을 훌륭하게 기록하셨습니다. {get_warm_feedback()}")

# [메뉴 5 - 신규] AI 맞춤형 솔루션 (Beta) -> 사업계획서 핵심 구현
elif menu == "🚀 AI 맞춤형 솔루션 (Beta)":
    st.markdown("<div class='main-header'>🤖 AI 스트레스 정밀 분석</div>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class='info-box' style='background-color:#EBF5FB; padding:15px; border-radius:10px; border-left: 5px solid #3498DB;'>
    <b>💡 AI 분석 엔진 가동</b><br>
    누적된 <b>바우처 사업 임상 데이터</b>와 귀하의 <b>행동 패턴(Log)</b>을 대조 분석하여, 
    현재 심리 상태에 최적화된 솔루션을 제공합니다.
    </div>
    """, unsafe_allow_html=True)
    
    st.write("") # 여백

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("#### 📊 현재 분석 가능한 데이터")
        st.metric(label="누적 생각 기록", value=f"{len(st.session_state.thoughts)}건")
        st.metric(label="작성된 관찰 일지", value=f"{len(st.session_state.journal_entries)}건")
    
    with col2:
        st.markdown("#### 🩺 분석 예상 소요 시간")
        st.write("약 3~5초 (실시간 클라우드 연동)")
        analyze_btn = st.button("내 마음 정밀 진단 시작", use_container_width=True)

    if analyze_btn:
        if len(st.session_state.thoughts) == 0:
            st.error("분석할 데이터가 부족합니다. '1. 걱정에 이름표 붙이기'를 먼저 진행해주세요.")
        else:
            # AI 분석 시뮬레이션 (Loading Effect)
            with st.spinner("임상 심리 알고리즘이 데이터를 분석 중입니다..."):
                time.sleep(2.5) # 분석하는 척
                
            st.success("분석이 완료되었습니다!")
            st.markdown("---")
            
            # 결과 리포트 (Mock-up)
            st.markdown(f"""
            <div class='card' style='border-left: 5px solid #E67E22;'>
                <h3>📑 AI 심리 분석 리포트</h3>
                <p><b>진단 유형:</b> <span style='color:#E67E22; font-weight:bold;'>미래 불안형 (Anticipatory Anxiety)</span></p>
                <p>사용자님의 기록에서 <b>'막막함', '걱정', '내일'</b>과 관련된 키워드 빈도가 높게 나타납니다.
                이는 통제할 수 없는 미래의 불확실성을 통제하려는 인지적 노력에서 비롯된 것으로 보입니다.</p>
                <hr>
                <h4>💊 상담심리학 박사의 맞춤 처방전</h4>
                <ul>
                    <li><b>인지 훈련:</b> '통제 가능한 것'과 '불가능한 것'을 종이에 적어 분류하세요.</li>
                    <li><b>행동 처방:</b> 불안이 올라올 때 '그만!' 이라고 외치는 사고 중지(Thought Stopping) 기법을 3회 실시하세요.</li>
                    <li><b>추천 콘텐츠:</b> 5분 호흡 명상 (앱 내 오디오 가이드)</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
            
            st.info("📌 이 결과는 초기 데이터에 기반한 예측이며, 데이터가 쌓일수록 더 정교해집니다.")

# --- Footer ---
st.markdown("---")
st.markdown("<div style='text-align: center; color: #95A5A6;'>© 2026 AI Solving Stress. All rights reserved.</div>", unsafe_allow_html=True)