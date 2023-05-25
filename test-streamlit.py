import streamlit as st
import openai

api_key = st.text_input("Enter your OpenAI API KEY")

# 设置OpenAI API密钥
openai.api_key = api_key

# 创建函数以获取并显示所有模型
for model in models:
    st.write(f"Model Name: {model.name}")
    st.write(f"Model ID: {model.id}")
    st.write(f"Owner: {model.owner}")
    st.write("---） 





# 设置标题
st.title("List of Models")

# 调用函数以显示所有模型
list_models()
