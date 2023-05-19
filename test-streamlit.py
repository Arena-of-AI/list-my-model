import streamlit as st

# 定義分頁內容
page1_content = """
    ## 第一個標題
    這是第一個分頁的內容。
"""

page2_content = """
    ## 第二個標題
    這是第二個分頁的內容。
"""

page3_content = """
    ## 第三個標題
    這是第三個分頁的內容。
"""

# 在選擇框中顯示分頁選項
page = st.selectbox("選擇分頁", ("分頁1", "分頁2", "分頁3"))

# 根據選擇的分頁顯示相應的內容
if page == "分頁1":
    st.markdown(page1_content)
elif page == "分頁2":
    st.markdown(page2_content)
elif page == "分頁3":
    st.markdown(page3_content)
