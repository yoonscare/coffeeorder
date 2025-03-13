import streamlit as st
import pandas as pd
from datetime import datetime
import time

# 페이지 설정
st.set_page_config(
    page_title="우리 동네 커피숍",
    page_icon="☕",
    layout="wide",
    initial_sidebar_state="expanded",
)

# CSS 스타일 적용 - 가독성 개선
st.markdown("""
<style>
    /* 전체 배경 색상 */
    .main {
        background-color: #f5efe0;
    }
    
    /* 컨테이너 간격 */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    
    /* 메인 제목 스타일 */
    .main-title {
        color: #4e342e;
        font-size: 3.5rem;
        font-weight: 900;
        text-align: center;
        margin-bottom: 1rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
    }
    
    /* 부제목 스타일 */
    .subtitle {
        color: #5d4037;
        font-size: 1.8rem;
        font-weight: 700;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    /* 제목 스타일 */
    h1 {
        color: #4e342e;
        font-size: 3rem !important;
        font-weight: 800 !important;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
    }
    
    h2 {
        color: #4e342e;
        font-size: 2.3rem !important;
        font-weight: 700 !important;
    }
    
    h3 {
        color: #4e342e;
        font-size: 1.8rem !important;
        font-weight: 600 !important;
    }
    
    /* 버튼 스타일 */
    .stButton>button {
        background-color: #5d4037;
        color: #ffebcd;
        font-weight: bold;
        font-size: 1.1rem;
        border-radius: 8px;
        border: none;
        padding: 0.6rem 1.2rem;
        box-shadow: 0 3px 6px rgba(0,0,0,0.2);
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        background-color: #8d6e63;
        transform: translateY(-3px);
        box-shadow: 0 5px 10px rgba(0,0,0,0.25);
    }
    
    /* 메뉴 카테고리 스타일 */
    .menu-category {
        background: linear-gradient(135deg, #5d4037, #8d6e63);
        padding: 1rem 1.5rem;
        border-radius: 10px;
        margin-bottom: 1.5rem;
        font-weight: bold;
        font-size: 1.5rem;
        color: #ffebcd;
        text-align: center;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
    
    /* 메뉴 아이템 스타일 */
    .menu-item {
        background-color: #5d4037;
        color: #ffebcd;
        padding: 1.2rem;
        border-radius: 10px;
        margin-bottom: 1rem;
        box-shadow: 0 3px 6px rgba(0,0,0,0.16);
        font-size: 1.1rem;
    }
    
    .menu-item:hover {
        box-shadow: 0 5px 10px rgba(0,0,0,0.25);
        transform: translateY(-2px);
        transition: all 0.3s ease;
    }
    
    /* 하이라이트 스타일 */
    .highlight {
        background-color: #ffab40;
        color: #4e342e;
        padding: 0.3rem 0.6rem;
        border-radius: 5px;
        font-weight: 600;
    }
    
    /* 주문 요약 스타일 */
    .order-summary {
        background-color: #8d6e63;
        color: #ffebcd;
        padding: 1.5rem;
        border-radius: 10px;
        margin-top: 1.5rem;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        font-size: 1.1rem;
    }
    
    /* 장바구니 헤더 스타일 */
    .cart-header {
        background-color: #4e342e;
        color: #ffebcd;
        padding: 1.5rem;
        border-radius: 10px 10px 0 0;
        font-size: 2.2rem;
        font-weight: bold;
        text-align: center;
        margin-bottom: 1rem;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
    
    /* 푸터 스타일 */
    .footer {
        text-align: center;
        margin-top: 3rem;
        padding: 1.5rem;
        background-color: #4e342e;
        color: #ffebcd;
        font-size: 1.1rem;
        border-radius: 10px;
        box-shadow: 0 -2px 10px rgba(0,0,0,0.1);
    }
    
    /* 셀렉트박스 스타일 */
    div.stSelectbox > div > div {
        background-color: #fff3e0;
        color: #4e342e !important;
        font-weight: 600;
        border: 2px solid #8d6e63;
        font-size: 1.1rem;
    }
    
    div.stMultiselect > div > div {
        background-color: #fff3e0;
        color: #4e342e !important;
        font-weight: 600;
        border: 2px solid #8d6e63;
        font-size: 1.1rem;
    }
    
    /* 인풋 필드 스타일 */
    .stNumberInput input, .stTextInput input, .stTextArea textarea {
        background-color: #fff3e0;
        color: #4e342e;
        font-weight: 600;
        border: 2px solid #8d6e63 !important;
        border-radius: 8px;
        padding: 0.8rem;
        font-size: 1.1rem;
    }
    
    /* 진행 바 스타일 */
    .stProgress > div > div > div {
        background-color: #5d4037;
    }
    
    /* 카테고리 탭 스타일 */
    .coffee-tab {
        background-color: #5d4037;
        color: #ffebcd;
        padding: 1.2rem;
        border-radius: 10px 10px 0 0;
        font-size: 1.5rem;
        font-weight: bold;
        text-align: center;
        margin-bottom: -1px;
        box-shadow: 0 -2px 10px rgba(0,0,0,0.1);
    }
    
    .options-tab {
        background-color: #7d5d4f;
        color: #ffebcd;
        padding: 1.2rem;
        border-radius: 10px 10px 0 0;
        font-size: 1.5rem;
        font-weight: bold;
        text-align: center;
        margin-bottom: -1px;
        box-shadow: 0 -2px 10px rgba(0,0,0,0.1);
    }
    
    /* 장바구니 아이콘 스타일 */
    .cart-icon {
        color: #ffebcd;
        font-size: 2rem;
        margin-right: 0.5rem;
    }
    
    /* 드롭다운 옵션 스타일 */
    .coffee-option {
        background-color: #5d4037;
        color: #ffebcd;
        padding: 1rem;
        border-radius: 0;
        border-bottom: 1px solid rgba(255,235,205,0.3);
        font-weight: 500;
    }
    
    .coffee-option:hover {
        background-color: #7d5d4f;
    }
    
    /* 사이드바 스타일 */
    .sidebar .sidebar-content {
        background-color: #3e2723;
        color: #ffebcd;
    }
    
    /* 사이드바 내비게이션 스타일 */
    .sidebar-nav {
        background-color: #4e342e;
        color: #ffebcd;
        padding: 1.2rem;
        border-radius: 10px;
        margin-bottom: 1rem;
        font-weight: bold;
        text-align: center;
        box-shadow: 0 2px 5px rgba(0,0,0,0.2);
    }
    
    /* 디버그 정보 스타일 */
    .debug-info {
        background-color: #fff3e0;
        border: 2px solid #8d6e63;
        border-radius: 10px;
        padding: 1rem;
        margin-top: 2rem;
    }
    
    /* 장바구니 배지 스타일 */
    .cart-badge {
        display: inline-block;
        background-color: #ff6f00;
        color: white;
        font-weight: bold;
        padding: 0.3rem 0.6rem;
        border-radius: 50%;
        margin-left: 0.5rem;
        box-shadow: 0 2px 4px rgba(0,0,0,0.2);
    }
    
    /* 빈 장바구니 스타일 */
    .empty-cart {
        background-color: #fff3e0;
        color: #5d4037;
        padding: 2rem;
        border-radius: 10px;
        text-align: center;
        margin: 2rem 0;
        border: 2px dashed #8d6e63;
    }
    
    /* 정보 메시지 스타일 */
    .stInfo {
        background-color: #bbdefb;
        color: #0d47a1;
        padding: 1rem;
        border-radius: 8px;
        font-weight: 500;
    }
    
    /* 성공 메시지 스타일 */
    .stSuccess {
        background-color: #c8e6c9;
        color: #1b5e20;
        padding: 1rem;
        border-radius: 8px;
        font-weight: 500;
    }
    
    /* 에러 메시지 스타일 */
    .stError {
        background-color: #ffcdd2;
        color: #b71c1c;
        padding: 1rem;
        border-radius: 8px;
        font-weight: 500;
    }
    
    /* 주문 항목 스타일 */
    .order-item {
        border-left: 5px solid #ff8f00;
        padding-left: 1rem;
        margin-bottom: 0.5rem;
    }
    
    /* 옵션 라벨 스타일 */
    .option-label {
        background-color: #d7ccc8;
        color: #4e342e;
        padding: 0.2rem 0.5rem;
        border-radius: 4px;
        margin-right: 0.5rem;
        font-size: 0.9rem;
        font-weight: 500;
    }
    
    /* 강조 버튼 스타일 */
    .primary-button {
        background-color: #ff8f00 !important;
        color: white !important;
    }
</style>
""", unsafe_allow_html=True)

# 세션 상태 초기화 - 주의: if 'key' not in st.session_state 구문 사용
if 'cart' not in st.session_state:
    st.session_state.cart = []
if 'order_history' not in st.session_state:
    st.session_state.order_history = []
if 'order_number' not in st.session_state:
    st.session_state.order_number = 1000
if 'active_tab' not in st.session_state:
    st.session_state.active_tab = "메뉴"
if 'debug_mode' not in st.session_state:
    st.session_state.debug_mode = False

# 앱 헤더
st.markdown('<div class="main-title">☕ 우리 동네 커피숍 🍵</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">맛있는 커피와 함께 특별한 시간을 보내세요!</div>', unsafe_allow_html=True)

# 메뉴 데이터
coffee_drinks = ["에스프레소", "아메리카노", "콜드 브루"]
milk_coffee_drinks = ["라떼", "카푸치노", "코르타도", "마키아토", "모카", "플랫 화이트"]
tea_drinks = ["차이 라떼", "말차 라떼", "런던 포그"]
other_drinks = ["스티머", "핫 초콜릿"]

# 수정자 옵션
milk_options = ["기본 (홀)", "2%", "오트", "아몬드", "락토스 프리 2%"]
shot_options = ["기본 (더블)", "싱글", "트리플", "쿼드러플"]
caffeine_options = ["기본 (레귤러)", "디카페인"]
temp_options = ["기본 (핫)", "아이스"]
sweetener_options = ["바닐라 시럽", "헤이즐넛 시럽", "카라멜 소스", "초콜릿 소스", "무설탕 바닐라 시럽"]
special_requests = ["엑스트라 핫", "한 펌프", "하프 카프", "엑스트라 폼", "더티 (에스프레소 샷 추가)"]

# 장바구니에 추가하는 함수
def add_to_cart(drink, milk, shots, caffeine, temp, sweeteners, special, quantity):
    # 중요: 깊은 복사나 새 객체 생성으로 참조 문제 해결
    item = {
        "drink": drink,
        "milk": milk,
        "shots": shots,
        "caffeine": caffeine,
        "temp": temp,
        "sweeteners": sweeteners.copy() if sweeteners else [],  # 리스트는 복사
        "special": special.copy() if special else [],  # 리스트는 복사
        "quantity": quantity
    }
    
    # 장바구니에 항목 추가
    st.session_state.cart.append(item)
    
    # 성공 메시지
    st.success(f"{drink} {quantity}잔이 장바구니에 추가되었습니다!")

# 장바구니 비우기
def clear_cart():
    st.session_state.cart = []
    st.success("장바구니가 비워졌습니다.")

# 주문 완료
def complete_order():
    if not st.session_state.cart:
        st.error("장바구니가 비어있습니다.")
        return
    
    # 깊은 복사를 통해 참조 문제 해결
    items_copy = []
    for item in st.session_state.cart:
        items_copy.append({
            "drink": item["drink"],
            "milk": item["milk"],
            "shots": item["shots"],
            "caffeine": item["caffeine"],
            "temp": item["temp"],
            "sweeteners": item["sweeteners"].copy() if item["sweeteners"] else [],
            "special": item["special"].copy() if item["special"] else [],
            "quantity": item["quantity"]
        })
    
    # 주문 정보 생성
    order = {
        "order_number": st.session_state.order_number,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "items": items_copy,
        "total_items": sum(item["quantity"] for item in st.session_state.cart)
    }
    
    # 주문 내역에 추가
    st.session_state.order_history.append(order)
    st.session_state.order_number += 1
    
    # 주문 처리 시뮬레이션
    progress_text = "주문 처리 중..."
    my_bar = st.progress(0, text=progress_text)
    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1, text=progress_text)
    
    st.balloons()
    st.success(f"주문 #{order['order_number']}이(가) 성공적으로 완료되었습니다!")
    st.info("바리스타가 주문을 준비 중입니다. 잠시만 기다려주세요.")
    
    # 장바구니 비우기
    st.session_state.cart = []
    
    # 주문 내역 페이지로 이동
    st.session_state.active_tab = "주문 내역"

# 사이드바 - 영업 정보
with st.sidebar:
    st.image("https://via.placeholder.com/150x150.png?text=☕", width=150)
    st.title("☕ 우리 동네 커피숍")
    
    st.markdown('<div class="sidebar-nav">영업 시간</div>', unsafe_allow_html=True)
    st.info("화, 수, 목 오전 10시 - 오후 2시")
    
    st.markdown('<div class="sidebar-nav">가격</div>', unsafe_allow_html=True)
    st.success("모든 음료는 무료! 🎁")
    
    # 네비게이션
    st.markdown('<div class="sidebar-nav">메뉴</div>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("메뉴 보기 🍹", key="menu_button", use_container_width=True):
            st.session_state.active_tab = "메뉴"
            st.experimental_rerun()
    
    with col2:
        # 장바구니 아이템 수 배지 표시
        cart_count = len(st.session_state.cart)
        cart_label = f"장바구니 🛒 {cart_count}" if cart_count > 0 else "장바구니 🛒"
        
        if st.button(cart_label, key="cart_button", use_container_width=True):
            st.session_state.active_tab = "장바구니"
            st.experimental_rerun()
    
    if st.button("주문 내역 📋", key="history_button", use_container_width=True):
        st.session_state.active_tab = "주문 내역"
        st.experimental_rerun()
    
    st.markdown("---")
    st.markdown('<div class="sidebar-nav">고객 맞춤형 음료 ✨</div>', unsafe_allow_html=True)
    st.markdown("다양한 우유, 시럽, 온도 등의 옵션으로 나만의 음료를 만들어보세요!")
    
    # 디버그 모드 토글
    if st.checkbox("디버그 모드", value=st.session_state.debug_mode):
        st.session_state.debug_mode = True
    else:
        st.session_state.debug_mode = False
    
    # 푸터
    st.markdown("---")
    st.markdown("#### ☕ 즐거운 시간 되세요! ☕")
    st.markdown("특별한 날을 위한 특별한 음료를 준비했습니다.")

# 메뉴 탭
def show_menu():
    st.markdown('<div class="menu-category">🍹 음료 메뉴</div>', unsafe_allow_html=True)
    st.markdown("원하는 음료를 선택하고 맞춤 옵션을 선택하세요.")
    
    # 커피 선택 탭과 맞춤 옵션 탭
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="coffee-tab">☕ 커피 선택</div>', unsafe_allow_html=True)
        
        # 음료 카테고리 선택
        category = st.selectbox("카테고리", 
                               ["커피 음료", "우유가 들어간 커피 음료", "우유가 들어간 차 음료", "기타 음료"])
        
        # 선택된 카테고리에 따른 음료 목록
        if category == "커피 음료":
            drink_list = coffee_drinks
        elif category == "우유가 들어간 커피 음료":
            drink_list = milk_coffee_drinks
        elif category == "우유가 들어간 차 음료":
            drink_list = tea_drinks
        else:
            drink_list = other_drinks
        
        # 음료 선택
        drink = st.selectbox("음료 선택", drink_list)
        
        # 음료 수량
        quantity = st.number_input("수량", min_value=1, max_value=10, value=1)
        
    with col2:
        st.markdown('<div class="options-tab">🥛 맞춤 옵션</div>', unsafe_allow_html=True)
        
        # 우유 옵션
        milk = st.selectbox("우유 옵션", milk_options)
        
        # 에스프레소 샷
        shots = st.selectbox("에스프레소 샷", shot_options)
        
        # 카페인
        caffeine = st.selectbox("카페인", caffeine_options)
        
        # 온도
        temp = st.selectbox("온도", temp_options)
        
        # 시럽
        sweeteners = st.multiselect("시럽 (여러 개 선택 가능)", sweetener_options)
        
        # 특별 요청
        special = st.multiselect("특별 요청", special_requests)
    
    # 주문 요약 (미리보기)
    st.markdown('<div class="order-summary">', unsafe_allow_html=True)
    st.markdown(f"### 📝 주문 미리보기")
    
    order_details = [drink]
    if milk != "기본 (홀)":
        order_details.append(milk)
    if shots != "기본 (더블)":
        order_details.append(shots)
    if caffeine != "기본 (레귤러)":
        order_details.append(caffeine)
    if temp != "기본 (핫)":
        order_details.append(temp)
    if sweeteners:
        order_details.extend(sweeteners)
    if special:
        order_details.extend(special)
    
    st.markdown(f"**{drink}** x {quantity}잔")
    if len(order_details) > 1:
        st.markdown(f"**옵션:** {', '.join(order_details[1:])}")
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # 장바구니에 추가 버튼
    if st.button("장바구니에 추가 🛒", use_container_width=True):
        add_to_cart(drink, milk, shots, caffeine, temp, sweeteners, special, quantity)
        
        # 장바구니에 추가 후 장바구니 화면으로 자동 이동
        st.session_state.active_tab = "장바구니"
        st.experimental_rerun()

# 장바구니 탭
def show_cart():
    st.markdown('<div class="cart-header">🛒 장바구니</div>', unsafe_allow_html=True)
    
    if not st.session_state.cart:
        st.markdown('<div class="empty-cart">', unsafe_allow_html=True)
        st.markdown("### 장바구니가 비어있습니다.")
        st.markdown("메뉴에서 음료를 선택하여 장바구니에 추가해 주세요.")
        st.markdown('</div>', unsafe_allow_html=True)
        
        if st.button("메뉴로 돌아가기 🍹", use_container_width=True):
            st.session_state.active_tab = "메뉴"
            st.experimental_rerun()
        return
    
    # 장바구니 내용 표시
    for i, item in enumerate(st.session_state.cart):
        with st.container():
            col1, col2 = st.columns([4, 1])
            
            with col1:
                st.markdown(f"<div class='menu-item'>", unsafe_allow_html=True)
                st.markdown(f"### {item['drink']} <span style='font-size:1.5rem;'>x{item['quantity']}</span>")
                
                options = []
                if item['milk'] != "기본 (홀)":
                    options.append(f"<span class='option-label'>{item['milk']}</span>")
                if item['shots'] != "기본 (더블)":
                    options.append(f"<span class='option-label'>{item['shots']}</span>")
                if item['caffeine'] != "기본 (레귤러)":
                    options.append(f"<span class='option-label'>{item['caffeine']}</span>")
                if item['temp'] != "기본 (핫)":
                    options.append(f"<span class='option-label'>{item['temp']}</span>")
                if item['sweeteners']:
                    for sweetener in item['sweeteners']:
                        options.append(f"<span class='option-label'>{sweetener}</span>")
                if item['special']:
                    for sp in item['special']:
                        options.append(f"<span class='option-label'>{sp}</span>")
                
                if options:
                    st.markdown(f"<div class='order-item'>옵션: {''.join(options)}</div>", unsafe_allow_html=True)
                st.markdown("</div>", unsafe_allow_html=True)
            
            with col2:
                if st.button("삭제 🗑️", key=f"remove_{i}", use_container_width=True):
                    # 삭제 후 세션 상태 갱신을 위해 새 리스트 생성
                    new_cart = st.session_state.cart.copy()
                    new_cart.pop(i)
                    st.session_state.cart = new_cart
                    st.experimental_rerun()
    
    # 주문 합계
    st.markdown('<div class="order-summary">', unsafe_allow_html=True)
    st.markdown(f"### 📝 주문 합계")
    st.markdown(f"총 주문 수량: **{sum(item['quantity'] for item in st.session_state.cart)}잔**")
    st.markdown('</div>', unsafe_allow_html=True)
    
    # 장바구니 작업 버튼
    col1, col2 = st.columns(2)
    with col1:
        if st.button("장바구니 비우기 🗑️", use_container_width=True):
            st.session_state.cart = []
            st.experimental_rerun()
    
    with col2:
        # 주문 완료 버튼에 primary 클래스 추가
        if st.button("주문 완료 ✅", key="complete_order", type="primary", use_container_width=True):
            complete_order()
            st.experimental_rerun()

# 주문 내역 탭
def show_order_history():
    st.markdown('<div class="cart-header">📋 주문 내역</div>', unsafe_allow_html=True)
    
    if not st.session_state.order_history:
        st.markdown('<div class="empty-cart">', unsafe_allow_html=True)
        st.markdown("### 주문 내역이 없습니다.")
        st.markdown("아직 완료된 주문이 없습니다. 메뉴에서 음료를 선택하여 주문해 보세요.")
        st.markdown('</div>', unsafe_allow_html=True)
        
        if st.button("메뉴로 돌아가기 🍹", key="menu_from_history", use_container_width=True):
            st
