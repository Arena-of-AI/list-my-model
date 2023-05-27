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
    st.table(filtered_models)

# 设置标题
st.title("List of Models")

# 检查是否输入了API密钥
if api_key:
    # 调用函数以显示所有模型
    list_models()

    # 添加对话框和删除按钮
    model_name = st.text_input("Enter the model name to delete")
    delete_button = st.button("Delete")

    # 当删除按钮被按下时执行删除操作
    if delete_button:
        if model_name:
            model_names = [model["id"] for model in filtered_models]
            if model_name in model_names:
                openai.Model.delete(model_name)
                st.success(f"Model {model_name} has been deleted.")
            else:
                st.warning("Please enter a valid model name.")
        else:
            st.warning("Please enter a model name to delete.")
