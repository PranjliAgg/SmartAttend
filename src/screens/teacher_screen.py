import streamlit as st

from src.ui.base_layout import style_bg_dashboard, style_base_layout
from src.components.header import header_dashboard
from src.components.footer import footer_dashboard
from src.database.db import check_teacher_exists, create_teacher, teacher_login

def teacher_screen():

    style_bg_dashboard()
    style_base_layout()


    if "teacher_data" in st.session_state:
        teacher_dashboard()
    elif "teacher_login_type" not in st.session_state or st.session_state.teacher_login_type=="login":
        teacher_screen_login()
    elif st.session_state.teacher_login_type=="register":
        teacher_screen_register()



    footer_dashboard()



def teacher_dashboard():
    teacher_data = st.session_state.teacher_data
    st.header(f"Welcome {teacher_data["name"]}")



def login_teacher(username, password):
    if not username or not password:
        return False

    teacher = teacher_login(username, password)

    if teacher:
        st.session_state.user_role = "teacher"
        st.session_state.teacher_data = teacher
        st.session_state.is_logged_in = True
        return True
    
    return False



def teacher_screen_login():

    col1, col2 = st.columns(2, vertical_alignment="center", gap="xxlarge")

    with col1:
        header_dashboard()

    with col2:
        if st.button("Go back to Home", key="loginbackbtn", type="primary", shortcut="control+backspace"):
            st.session_state["login_type"] = None
            st.rerun()

    st.header("Login using password", text_alignment="center")

    st.space()
    st.space()

    teacher_username = st.text_input("Enter username", placeholder="@johndoe")
    teacher_pass = st.text_input("Enter password", type="password", placeholder="example$123")

    st.divider()

    btncl1, btncl2 = st.columns(2)

    with btncl1:
        if st.button("Login", type="primary", icon=":material/passkey:", shortcut="control+enter", width="stretch"):
            if login_teacher(teacher_username, teacher_pass):
                st.toast("Welcome Back!", icon="👋")
                import time
                time.sleep(1)
                st.rerun()
            else:
                st.error("Invalid Username or Password")

    with btncl2:
        if st.button("Register New User", type="secondary", icon=":material/passkey:", width="stretch"):
            st.session_state["teacher_login_type"] = "register"
            st.rerun()



def register_teacher(teacher_username, teacher_name, teacher_pass, teacher_pass_confirm):
    if not teacher_username or not teacher_name or not teacher_pass:
        return False, "All field are mandatory!"
    if check_teacher_exists(teacher_username):
        return False, "Username already taken."
    if teacher_pass!=teacher_pass_confirm:
        return False, "Password doesn't match"
    
    try:
        create_teacher(teacher_username, teacher_name, teacher_pass)
        return True, "Successfully Created! Login Now"
    except Exception as e:
        st.write(e)
        return False, "Unexpected Error Occured!"



def teacher_screen_register():

    col1, col2 = st.columns(2, vertical_alignment="center", gap="xxlarge")

    with col1:
        header_dashboard()

    with col2:
        if st.button("Go back to Home", key="loginbackbtn", type="primary", shortcut="control+backspace"):
            st.session_state["login_type"] = None
            st.rerun()
            
    st.header("Register as a Teacher", text_alignment="center")

    st.space()
    st.space()

    teacher_username = st.text_input("Enter username", placeholder="@johndoe")
    teacher_name = st.text_input("Enter name", placeholder="John Doe")
    teacher_pass = st.text_input("Enter password", type="password", placeholder="example$123")
    teacher_pass_confirm = st.text_input("Confirm your password", type="password", placeholder="example$123")

    btncl1, btncl2 = st.columns(2)

    with btncl1:
        if st.button("Login", type="primary", icon=":material/passkey:", width="stretch"):
            st.session_state["teacher_login_type"] = "login"
            st.rerun()    

    with btncl2:
        if st.button("Register New User", type="secondary", icon=":material/passkey:", width="stretch", shortcut="control+enter"):
            success, message = register_teacher(teacher_username, teacher_name, teacher_pass, teacher_pass_confirm)
            if success:
                st.success(message)
                import time
                time.sleep(2)
                st.session_state.teacher_login_type = "login"
                st.rerun()
            else:
                st.error(message)

    st.divider()