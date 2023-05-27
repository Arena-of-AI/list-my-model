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
            "Created at": datetime.fromtimestamp(model["created"]).strftime("%Y-%m-%d %H:%M:%S"),
            "Model Name (ID)": model["id"],
            "Parent Model": model["parent"]
        }
        for model in models['data']
        if model['owned_by'] not in ['openai-internal', 'openai', 'system', 'openai-dev']
    ]

    return filtered_models

# 设置标题
st.title("List of Models")

# 检查是否输入了API密钥
if api_key:
    # 调用函数以显示所有模型
    models = list_models()

    # 检查模型列表是否为空
    if models:
        # 显示模型列表的表格
        st.table(models)

        # 添加对话框和删除按钮
        model_name = st.text_input("To avoid accidental deletion, please type the model name you want to delete")
        delete_button = st.button("Delete")

        # 当删除按钮被按下时执行删除操作
        if delete_button:
            # 确认删除的对话框
            confirmation = st.confirm("Are you sure you want to delete the model?")

            if confirmation:
                # 检查要删除的模型名称是否存在
                model_names = [model["Model Name (ID)"] for model in models]
                if model_name in model_names:
                    # 执行删除操作
                    response = openai.Model.delete(model_name)

                    # 等待删除操作完成并输出结果
                    st.write(response)
                    if response.get("deleted"):
                        st.success("Model deleted successfully.")
                    else:
                        st.error("Failed to delete the model.")
                else:
                    st.warning("Please enter a valid model name.")
    else:
        st.info("This API key doesn't have any fine-tuned model.")
