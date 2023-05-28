import streamlit as st
import openai
from datetime import datetime

# 设置标题
st.title("List of Your Fine-Tuned Models")

# 输入API密钥
api_key = st.text_input("Enter your OpenAI API KEY")

# 设置OpenAI API密钥
openai.api_key = api_key

# 创建函数以获取并返回所有模型
def list_models():
    # 检查是否输入了API密钥
    if not api_key:
        st.warning("Please enter your OpenAI API KEY.")
        return []

    try:
        # 获取模型列表
        models = openai.Model.list()

        # 筛选并提取需要的字段
        filtered_models = [
            {
                "Created at": datetime.fromtimestamp(model["created"]).strftime("%Y-%m-%d %H:%M:%S"),
                "Model Name (ID)": model["id"],
                "Parent Model": model["parent"]
            }
            for model in models['data']
            if model['owned_by'] not in ['openai-internal', 'openai', 'system', 'openai-dev']
        ]

        # 检查模型列表是否为空
        if not filtered_models:
            st.warning("This API Key doesn't have any fine-tuned model.")

        return filtered_models
    except openai.error.AuthenticationError as e:
        st.error(str(e))
        return []


# 调用函数以获取所有模型
models = list_models()

# 检查模型列表是否为空
if models:
    # 显示模型列表的表格
    st.table(models)

    # 添加对话框和删除按钮
    st.title("Delete Your Fine-Tuned Models")
    model_name = st.text_input("To avoid accidental deletion, please type the model name (ID) you want to delete here")
    delete_button = st.button("Delete")

    # 当删除按钮被按下时执行删除操作
    if delete_button:
        if model_name:
            model_names = [model["Model Name (ID)"] for model in models]
            if model_name in model_names:
                # 显示确认对话框
                confirmation = st.checkbox("Are you sure you want to delete the model?")

                # 当确认对话框为True时执行删除操作
                if confirmation:
                    # 删除模型
                    try:
                        response = openai.Model.delete(model_name)

                        # 判断删除是否成功
                        if response.get("deleted"):
                            # 显示成功消息
                            st.success("Model deleted successfully.")
                        else:
                            # 显示失败消息
                            st.error("Failed to delete the model.")
                    except openai.error.APIError as e:
                        st.error(str(e))
            else:
                st.warning("Please enter a valid model name.")
        else:
            st.warning("Please enter a model name to delete.")
