import streamlit as st

# 定义选项卡名称列表
tabs = ["Tab 1", "Tab 2", "Tab 3"]

# 在sidebar中创建选项卡
selected_tab = st.sidebar.radio("Select Tab", tabs)

# 根据选项卡显示相应的内容
for tab in tabs:
    if tab == selected_tab:
        st.sidebar.markdown(f"**{tab}**")
    else:
        st.sidebar.markdown(tab)
