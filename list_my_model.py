import streamlit as st
import openai
from datetime import datetime

# 输入API密钥
api_key = st.text_input("Enter your OpenAI API KEY")

# 设置OpenAI API密钥
openai.api_key = api_key

# 创建函数以获取并返回所有模型
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

    return filtered_models

# 设置标题
st.title("List of Models")

# 检查是否输入了API密钥
if api_key:
    # 调用函数以获取所有模型
    models = list_models()

    # 显示模型列表的表格
    st.table(models)

    # 添加对话框和删除按钮
    model_name = st.text_input("To avoid accidental deletion, please type the model name you want to delete")
    delete_button = st.button("Delete")

    # 当删除按钮被按下时执行删除操作
    if delete_button:
        if model_name:
            model_names = [model["id"] for model in models]
            if model_name in model_names:
                # 显示确认对话框
                confirmation = st.checkbox("Are you sure you want to delete the model?")

                # 当确认对话框为True时执行删除操作
                if confirmation:
                    # 删除模型
                    response = openai.Model.delete(model_name)

                    # 判断删除是否成功
                    if response.get("deleted"):
                        # 等待终端响应，显示成功消息
                        st.text("Deleting the model...")
                        st.success("Model deleted successfully.")
                    else:
                        # 等待终端响应，显示失败消息
                        st.text("Deleting the model...")
                        st.error("Failed to delete the model.")
            else:
                st.warning("Please enter a valid model name.")
        else:
            st.warning("Please enter a model name to delete.")
