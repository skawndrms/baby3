import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 페이지 기본 설정
st.set_page_config(page_title="지역별 데이터 시각화", layout="wide")

# 데이터 불러오기 (Streamlit Cloud에서는 같은 디렉토리에 있어야 함)
@st.cache_data
def load_data():
    df = pd.read_csv("sum_by_region.csv")
    return df

df = load_data()

# 제목
st.title("📊 지역별 데이터 시각화 대시보드")

# 데이터 미리보기
with st.expander("데이터 미리보기"):
    st.dataframe(df, use_container_width=True)

# 사이드바 필터
st.sidebar.header("필터 설정")
numeric_cols = df.select_dtypes(include="number").columns.tolist()
category_cols = df.select_dtypes(exclude="number").columns.tolist()

# 집계 기준 선택 (예: 지역, 시도 등)
if category_cols:
    group_col = st.sidebar.selectbox("집계 기준(범주형 열)", category_cols)
else:
    group_col = None

# 수치 열 선택
if numeric_cols:
    value_col = st.sidebar.selectbox("시각화할 수치 열", numeric_cols)
else:
    value_col = None

# 시각화
if group_col and value_col:
    st.subheader(f"📍 {group_col}별 {value_col} 시각화")

    grouped = df.groupby(group_col)[value_col].sum().sort_values(ascending=False)

    # 막대 그래프
    fig, ax = plt.subplots(figsize=(10, 6))
    grouped.plot(kind="bar", ax=ax)
    ax.set_ylabel(value_col)
    ax.set_xlabel(group_col)
    ax.set_title(f"{group_col}별 {value_col}")
    st.pyplot(fig)

    # 데이터 테이블
    st.dataframe(grouped.reset_index(), use_container_width=True)
else:
    st.warning("CSV에 범주형 열과 수치 열이 있어야 시각화 가능합니다.")
    st.dataframe(region_df)
