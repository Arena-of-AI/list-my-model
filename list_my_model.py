import datetime
import openai
import streamlit as st

# 获取终端输出并显示表格
def list_fine_tuned_tasks(api_key):
    openai.api_key = api_key
    terminal_output = openai.FineTune.list()
    return terminal_output["data"]

# 解析终端输出为表格行列表
def parse_terminal_output(terminal_output):
    rows = []
    for task in terminal_output:
        hyperparams = task["hyperparams"]
        training_file = task["training_files"][0]["filename"]

        created_at = datetime.datetime.fromtimestamp(task["created_at"]).strftime("%Y-%m-%d %H:%M:%S")

        row = {
            "Time": created_at,
            "Model Name": task["fine_tuned_model"],
            "Job ID": task["id"],
            "Parent Model": task["model"],
            "Status": task["status"],
            "Batch Size": hyperparams["batch_size"],
            "Learning Rate Multiplier": hyperparams["learning_rate_multiplier"],
            "Epochs": hyperparams["n_epochs"],
            "Prompt Loss Weight": hyperparams["prompt_loss_weight"],
            "Training File": training_file
        }
        rows.append(row)

    return rows

# 删除指定的模型
def delete_model(model_name):
    openai.Model.delete(model_name)
    st.success(f"Model '{model_name}' deleted successfully.")

# 读取 API 密钥
api_key = st.text_input("Enter your OpenAI API key", type="password")

# 当用户提供 API 密钥时，获取终端输出并解析为表格行列表
if api_key:
    tasks = list_fine_tuned_tasks(api_key)
    rows = parse_terminal_output(tasks)

    for row in rows:
        # 获取模型名称和索引
        model_name = row["Model Name"]
        index = rows.index(row)

        # 在行的末尾添加删除按钮
        delete_button = st.button(f"Delete {model_name}", key=f"delete_{index}")
        if delete_button:
            delete_model(model_name)

    st.table(rows)
else:
    st.warning("Please enter your OpenAI API key.")
