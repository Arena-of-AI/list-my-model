import streamlit as st

# 定义选项卡名称列表
tabs = ["Tab 1", "Tab 2", "Tab 3"]

# 在sidebar中创建选项卡
selected_tab = st.sidebar.selectbox("Select Tab", tabs)

# 根据选项卡显示相应的内容
if selected_tab == "Tab 1":
    st.header("Tab 1 Content")
    st.write("This is the content of Tab 1.")
elif selected_tab == "Tab 2":
    st.header("Tab 2 Content")
    st.write("This is the content of Tab 2.")
elif selected_tab == "Tab 3":
    st.header("Tab 3 Content")
    st.write("This is the content of Tab 3.")
