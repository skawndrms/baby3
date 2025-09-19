import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# CSV 파일 불러오기
@st.cache
def load_data():
    file_path = 'sum_by_region.csv'
    data = pd.read_csv(file_path, encoding='euc-kr')
    return data

# 데이터 로드
data = load_data()

# 페이지 헤더
st.title('Birth Registrations by Region')

# 사용자가 선택할 지역 데이터
regions = data['시도명'].unique()
selected_region = st.selectbox('Select a region (시도명):', regions)

# 선택한 지역 필터링
filtered_data = data[data['시도명'] == selected_region]

# 시각화
st.subheader(f'Birth Registrations in {selected_region}')
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(filtered_data['시군구명'], filtered_data['계'], color='skyblue')
ax.set_xlabel('Districts (시군구명)', fontsize=12)
ax.set_ylabel('Total Births', fontsize=12)
ax.set_title(f'Total Births by District in {selected_region}', fontsize=14)
plt.xticks(rotation=45, ha='right')
st.pyplot(fig)

