import streamlit as st
import openai

# 输入 OpenAI API KEY
api_key = st.text_input("Enter your OpenAI API KEY")

# 设置 OpenAI API 密钥
openai.api_key = api_key

# 创建 ChatCompletion 实例
chat_instance = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What models do I have?"},
    ]
)

# 获取现有模型列表
models = chat_instance["choices"][0]["message"]["content"]

# 显示模型列表
st.title("Existing Models")
for model in models:
    st.write(f"- Model: {model}")
