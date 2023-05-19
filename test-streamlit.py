import streamlit as st

# 使用 st.beta_expander (Streamlit v0.87.0 或更高版本)
with st.beta_expander("點擊展開內容"):
    st.write("這是一大段內容...")

# 或者使用 st.expander (Streamlit v0.86.0 或更低版本)
with st.expander("點擊展開內容"):
    st.write("這是一大段內容...")
