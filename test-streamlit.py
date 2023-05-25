import streamlit as st
import openai

# 输入 OpenAI API KEY
api_key = st.text_input("Enter your OpenAI API KEY")

# 设置 OpenAI API 密钥
openai.api_key = api_key

# 获取现有模型列表
response = openai.ChatCompletion.list_models()

# 解析响应数据
if response and "data" in response:
    models = response["data"]
else:
    st.error("Error fetching model list")

# 显示模型列表
st.title("Existing Models")
for model in models:
    st.write(f"- Model ID: {model['id']}")
    st.write(f"  Model Name: {model['name']}")
    st.write(f"  Model Description: {model['description']}")
    st.write(f"  Model Owner: {model['owner']}")
    st.write("---")
