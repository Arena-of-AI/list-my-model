import streamlit as st

def authenticate(password):
    # 在這裡執行密碼驗證邏輯，例如比對密碼是否正確
    return password == "your_password"

def main():
    # 檢查 Session State 中是否已進行過驗證
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False

    # 如果尚未進行驗證，請求使用者輸入密碼
    if not st.session_state.authenticated:
        password = st.text_input("請輸入密碼", type="password")
        if st.button("驗證"):
            if authenticate(password):
                st.session_state.authenticated = True
                st.success("驗證成功！")
            else:
                st.error("驗證失敗！請再試一次。")
    else:
        # 顯示多頁選擇的畫面
        page = st.sidebar.selectbox("選擇頁面", ("頁面 1", "頁面 2", "頁面 3"))

        # 根據選擇顯示相應的內容和按鈕
        if page == "頁面 1":
            st.title("頁面 1")
            st.button("按鈕 1")
        elif page == "頁面 2":
            st.title("頁面 2")
            st.button("按鈕 2")
        elif page == "頁面 3":
            st.title("頁面 3")
            st.button("按鈕 3")

if __name__ == "__main__":
    main()
