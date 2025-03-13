import streamlit as st
import pandas as pd
from datetime import datetime
import random
import time

# 페이지 설정
st.set_page_config(
    page_title="우리 동네 커피숍",
    page_icon="☕",
    layout="wide",
    initial_sidebar_state="expanded",
)

# CSS 스타일 적용
st.markdown("""
<style>
    .main {
        background-color: #fff8e7;
    }
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    h1, h2, h3 {
        color: #5a3825;
    }
    .stButton>button {
        background-color: #c1e1c1;
        color: #5a3825;
        font-weight: bold;
        border-radius: 8px;
        border: none;
        padding: 0.5rem 1rem;
    }
    .stButton>button:hover {
        background-color: #93c47d;
        color: white;
    }
    .menu-category {
        background: linear-gradient(135deg, #c4e0f9, #e0c4fd);
        padding: 0.5rem 1rem;
        border-radius: 8px;
        margin-bottom: 1rem;
        font-weight: bold;
        color: #5a3825;
    }
    .menu-item {
        background-color: white;
        padding: 0.8rem;
        border-radius: 8px;
        margin-bottom: 0.5rem;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }
    .menu-item:hover {
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
    .highlight {
        background-color: #ffd1dc;
        padding: 0.2rem 0.5rem;
        border-radius: 5px;
        font-weight: 500;
    }
    .order-summary {
        background-color: #fdfdbd;
        padding: 1rem;
        border-radius: 8px;
        margin-top: 1rem;
    }
    .footer {
        text-align: center;
        margin-top: 2rem;
        color: #5a3825;
        font-size: 0.9rem;
    }
    div.stSelectbox > div > div {
        background-color: white;
    }
    div.stMultiselect > div > div {
        background-color: white;
    }
</style>
""", unsafe_allow_html=True)

# 세션 스테이트 초기화
if 'cart' not in st.session_state:
    st.session_state.cart = []
if 'order_history' not in st.session_state:
    st.session_state.order_history = []
if 'order_number' not in st.session_state:
    st.session_state.order_number = 1000
if 'active_tab' not in st.session_state:
    st.session_state.active_tab = "메뉴"

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

# 사이드바 - 영업 정보
with st.sidebar:
    st.image("https://via.placeholder.com/150x150.png?text=☕", width=150)
    st.title("우리 동네 커피숍")
    st.markdown("### 영업 시간")
    st.info("화, 수, 목 오전 10시 - 오후 2시")
    st.markdown("### 가격")
    st.success("모든 음료는 무료!")
    
    # 네비게이션
    st.markdown("## 메뉴")
    if st.button("메뉴 보기", key="menu_button"):
        st.session_state.active_tab = "메뉴"
    if st.button("장바구니", key="cart_button"):
        st.session_state.active_tab = "장바구니"
    if st.button("주문 내역", key="history_button"):
        st.session_state.active_tab = "주문 내역"
    
    st.markdown("---")
    st.markdown("### 고객 맞춤형 음료")
    st.markdown("다양한 우유, 시럽, 온도 등의 옵션으로 나만의 음료를 만들어보세요!")
    
    # 푸터
    st.markdown("---")
    st.markdown("#### ☕ 즐거운 시간 되세요! ☕")
    st.markdown("특별한 날을 위한 특별한 음료를 준비했습니다.")

# 장바구니에 추가하는 함수
def add_to_cart(drink, milk, shots, caffeine, temp, sweeteners, special, quantity):
    item = {
        "drink": drink,
        "milk": milk,
        "shots": shots,
        "caffeine": caffeine,
        "temp": temp,
        "sweeteners": sweeteners,
        "special": special,
        "quantity": quantity
    }
    st.session_state.cart.append(item)
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
    
    order = {
        "order_number": st.session_state.order_number,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "items": st.session_state.cart.copy(),
        "total_items": sum(item["quantity"] for item in st.session_state.cart)
    }
    
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

# 메뉴 탭
def show_menu():
    st.title("음료 메뉴")
    st.markdown("원하는 음료를 선택하고 맞춤 옵션을 선택하세요.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="menu-category">커피 선택</div>', unsafe_allow_html=True)
        
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
        st.markdown('<div class="menu-category">맞춤 옵션</div>', unsafe_allow_html=True)
        
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
    
    # 장바구니에 추가 버튼
    if st.button("장바구니에 추가"):
        add_to_cart(drink, milk, shots, caffeine, temp, sweeteners, special, quantity)

# 장바구니 탭
def show_cart():
    st.title("장바구니")
    
    if not st.session_state.cart:
        st.info("장바구니가 비어있습니다.")
        if st.button("메뉴로 돌아가기"):
            st.session_state.active_tab = "메뉴"
        return
    
    for i, item in enumerate(st.session_state.cart):
        with st.container():
            col1, col2, col3 = st.columns([3, 1, 1])
            
            with col1:
                st.markdown(f"<div class='menu-item'>", unsafe_allow_html=True)
                st.markdown(f"#### {item['drink']} x{item['quantity']}")
                
                options = []
                if item['milk'] != "기본 (홀)":
                    options.append(item['milk'])
                if item['shots'] != "기본 (더블)":
                    options.append(item['shots'])
                if item['caffeine'] != "기본 (레귤러)":
                    options.append(item['caffeine'])
                if item['temp'] != "기본 (핫)":
                    options.append(item['temp'])
                if item['sweeteners']:
                    options.extend(item['sweeteners'])
                if item['special']:
                    options.extend(item['special'])
                
                if options:
                    st.markdown("**옵션:** " + ", ".join(options))
                st.markdown("</div>", unsafe_allow_html=True)
            
            with col2:
                if st.button("삭제", key=f"remove_{i}"):
                    st.session_state.cart.pop(i)
                    st.experimental_rerun()
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("장바구니 비우기"):
            clear_cart()
            st.experimental_rerun()
    
    with col2:
        if st.button("주문 완료", type="primary"):
            complete_order()

# 주문 내역 탭
def show_order_history():
    st.title("주문 내역")
    
    if not st.session_state.order_history:
        st.info("주문 내역이 없습니다.")
        if st.button("메뉴로 돌아가기", key="menu_from_history"):
            st.session_state.active_tab = "메뉴"
        return
    
    # 최신 주문부터 표시
    for order in reversed(st.session_state.order_history):
        with st.expander(f"주문 #{order['order_number']} - {order['date']}"):
            for item in order['items']:
                with st.container():
                    st.markdown(f"<div class='menu-item'>", unsafe_allow_html=True)
                    st.markdown(f"#### {item['drink']} x{item['quantity']}")
                    
                    options = []
                    if item['milk'] != "기본 (홀)":
                        options.append(item['milk'])
                    if item['shots'] != "기본 (더블)":
                        options.append(item['shots'])
                    if item['caffeine'] != "기본 (레귤러)":
                        options.append(item['caffeine'])
                    if item['temp'] != "기본 (핫)":
                        options.append(item['temp'])
                    if item['sweeteners']:
                        options.extend(item['sweeteners'])
                    if item['special']:
                        options.extend(item['special'])
                    
                    if options:
                        st.markdown("**옵션:** " + ", ".join(options))
                    st.markdown("</div>", unsafe_allow_html=True)
            
            st.success(f"총 {order['total_items']}잔 주문 완료")
    
    if st.button("새 주문하기"):
        st.session_state.active_tab = "메뉴"

# 메인 컨텐츠 - 탭에 따라 다른 내용 표시
if st.session_state.active_tab == "메뉴":
    show_menu()
elif st.session_state.active_tab == "장바구니":
    show_cart()
elif st.session_state.active_tab == "주문 내역":
    show_order_history()

# 푸터
st.markdown("""
<div class="footer">
    <p>© 2025 우리 동네 커피숍. 모든 권리 보유.</p>
</div>
""", unsafe_allow_html=True)
