import streamlit as st
import openai

# 输入API密钥
api_key = st.text_input("Enter your OpenAI API KEY")

# 设置OpenAI API密钥
openai.api_key = api_key

# 创建函数以获取并显示所有模型名称
def list_models():
    # 获取模型列表
    model_lst = openai.Model.list()

    # 提取模型名称并显示
    model_names = [model['id'] for model in model_lst['data']]
    st.write("Available Models:")
    for name in model_names:
        st.write(name)

# 设置标题
st.title("List of Models")

# 检查是否输入了API密钥
if api_key:
    # 调用函数以显示所有模型名称
    list_models()
