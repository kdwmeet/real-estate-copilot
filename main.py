import streamlit as st
from app.generator import generate_description

st.set_page_config(page_title="부동산 AI 카피라이터", layout="wide")

# --- 헤더 --- 
st.title("부동산 매물 AI 카피라이터")
st.divider()

# --- 화면 레이아웃 (좌:입력, 우:결과) --- 
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("매물 정보 입력")

    # 사진 업로드
    uploaded_file = st.file_uploader("대표 사진 (거실 추천)", type=["jpg", "png", "jpeg"])
    if uploaded_file:
        st.image(uploaded_file, caption="선택된 사진", width="stretch")

    # 기본 정보 입력
    property_type = st.selectbox("매물 유형", ["원룸/오피스텔", "아파트", "빌라/다세대", "상가/사무실"])

    # 추가 특징 (옵션)
    info_text = st.text_area(
        "추가 특징 (선택사항)",
        height=100,
        placeholder="예: 역세권 5분, 풀옵션, 남향, 즉시 입주 가능, 보증금 조절 가능"
    )
    
    generate_btn = st.button("✨ 홍보글 생성", type="primary", width="stretch")
with col2:
    st.subheader("생성 결과")
    
    if generate_btn:
        if not uploaded_file:
            st.warning("먼저 매물 사진을 업로드해주세요")
        else:
            with st.spinner("AI 중개사가 매물을 분석하고 글을 쓰는 중..."):
                result = generate_description(uploaded_file, property_type, info_text)

                if "error" in result:
                    st.error(result["error"])
                else:
                    # 결과 파싱
                    title = result.get("title", "")
                    keywords = result.get("keywords", [])
                    desc = result.get("description", "")
                    hashtags = result.get("hashtags", "")

                    # 제목 카드
                    st.success(f"**제목:** {title}")
                    
                    # 키워드 태그
                    st.write("**핵심 포인트**")
                    st.markdown(" ".join([f"`{k}`" for k in keywords]))

                    # 본문 내용 (복사하기 좋게 텍스트 에어리어로)
                    st.write(" **상세 설명 (블로그/플랫폼용**")
                    st.text_area("결과 복사", value=desc + "\n\n" + hashtags, height=250)

                    st.info(" 팁: 위 내용을 복사해서 블로그나 플랫폼에 바로 붙여넣으세요")

    elif not generate_btn and not uploaded_file:
        st.info("왼쪽에서 사진을 올리고 정보를 입력해주세요.")           