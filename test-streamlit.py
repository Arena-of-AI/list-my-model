import streamlit as st
import openai

# 输入 OpenAI API KEY
api_key = st.text_input("Enter your OpenAI API KEY")

# 设置OpenAI API密钥
openai.api_key = api_key

model_lst = openai.Model.list()

for i in model_lst['data']:
    print(i['id'])
# 设置标题
st.title("List of Models")
