import streamlit as st
import openai

# 输入API密钥
api_key = st.text_input("Enter your OpenAI API KEY")

# 设置OpenAI API密钥
openai.api_key = api_key

# 创建函数以获取并显示所有Fine-Tuned模型
def list_fine_tuned_models():
    # 获取Fine-Tuned模型列表
    models = openai.FineTune.list()
    
    # 输出终端机消息到Streamlit
    st.code(models)

# 设置标题
st.title("List of Fine-Tuned Models")

# 检查是否输入了API密钥
if api_key:
    # 调用函数以显示所有Fine-Tuned模型
    list_fine_tuned_models()
