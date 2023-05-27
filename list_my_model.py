import streamlit as st
import openai
from datetime import datetime

# 输入API密钥
api_key = st.text_input("Enter your OpenAI API KEY")

# 设置OpenAI API密钥
openai.api_key = api_key

# 创建函数以获取并显示所有模型
def list_models():
    # 获取模型列表
    models = openai.Model.list()

    # 筛选并提取需要的字段
    filtered_models = [
        {
            "created": datetime.fromtimestamp(model["created"]).strftime("%Y-%m-%d %H:%M:%S"),
            "id": model["id"],
            "parent": model["parent"]
        }
        for model in models['data']
        if model['owned_by'] not in ['openai-internal', 'openai', 'system', 'openai-dev']
    ]

    # 输出终端机消息到Streamlit
    col1, col2, col3 = st.beta_columns([1, 1, 1])
    with col1:
        st.write("Model Created")
        for model in filtered_models:
            st.write(model['created'])
    with col2:
        st.write("Model ID")
        for model in filtered_models:
            st.write(model['id'])
    with col3:
        st.write("Parent")
        for model in filtered_models:
            st.write(model['parent'])

    # 在每一行数据后方添加删除功能
    st.write("Actions")
    for model in filtered_models:
        col1, col2, col3 = st.beta_columns([1, 1, 1])
        with col1:
            st.empty()
        with col2:
            st.empty()
        with col3:
            delete_button = st.button(f"Delete {model['id']}")
            if delete_button:
                openai.Model.delete(model['id'])
                st.success(f"Model {model['id']} deleted successfully.")

# 设置标题
st.title("List of Models")

# 检查是否输入了API密钥
if api_key:
    # 调用函数以显示所有模型
    list_models()
