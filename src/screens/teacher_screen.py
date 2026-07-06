import streamlit as st

from src.ui.base_layout import style_bg_dashboard, style_base_layout
from src.components.header import header_dashboard
from src.components.footer import footer_dashboard
from src.components.subject_card import subject_card
from src.database.db import check_teacher_exists, create_teacher, teacher_login, get_teacher_subjects
from src.components.dialog_create_subject import create_subject_dialog
from src.components.dialog_share_subject import share_subject_dialog
from src.components.dialog_add_photo import add_photos_dialog

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

    col1, col2 = st.columns(2, vertical_alignment="center", gap="xxlarge")

    with col1:
        header_dashboard()

    with col2:
        if st.button("Logout", key="loginbackbtn", type="primary", shortcut="control+backspace"):
            st.session_state["is_logged_in"] = False
            del st.session_state.teacher_data
            st.rerun()

    st.space()

    st.subheader(f"Welcome {teacher_data["name"]}")

    st.space()

    if "current_teacher_tab" not in st.session_state:
        st.session_state.current_teacher_tab = "take_attendance"

    tab1, tab2, tab3 = st.columns(3)

    with tab1:
        type1 = "primary" if st.session_state.current_teacher_tab == "take_attendance" else "secondary"
        if st.button("Take Attendance", type=type1, width="stretch", icon=":material/ar_on_you:"):
            st.session_state.current_teacher_tab = "take_attendance"
            st.rerun()

    with tab2:
        type2 = "primary" if st.session_state.current_teacher_tab == "manage_subjects" else "secondary"
        if st.button("Manage Subjects", type=type2, width="stretch", icon=":material/book_ribbon:"):
            st.session_state.current_teacher_tab = "manage_subjects"
            st.rerun()

    with tab3:
        type3 = "primary" if st.session_state.current_teacher_tab == "attendance_records" else "secondary"
        if st.button("Attendance Records", type=type3, width="stretch", icon=":material/cards_stack:"):
            st.session_state.current_teacher_tab = "attendance_records"
            st.rerun()

    st.divider()

    if st.session_state.current_teacher_tab == "take_attendance":
        teacher_tab_take_attendance()
    if st.session_state.current_teacher_tab == "manage_subjects":
        teacher_tab_manage_subjects()
    if st.session_state.current_teacher_tab == "attendance_records":
        teacher_tab_attendance_records()



def teacher_tab_take_attendance():
    teacher_id = st.session_state.teacher_data["teacher_id"]
    st.header("Take Attendance")

    if "attendance_images" not in st.session_state:
        st.session_state.attendance_images = []

    subjects = get_teacher_subjects(teacher_id)

    if not subjects:
        st.warning("You haven't created any subjects yet. Please create one to begin!")
        return
    
    subject_options = {f"{s["name"]} - {s["subject_code"]}": s["subject_id"] for s in subjects}

    col1, col2 = st.columns([3, 1])

    with col1:
        selected_subject_label = st.selectbox("Select Subject", options=list(subject_options.keys()))
    
    with col2:
        if st.button("Add Photos", type="primary", icon=":material/photo_prints:", width="stretch"):
            add_photos_dialog()

    selected_subject_id = subject_options[selected_subject_label]

    st.divider()            



def teacher_tab_manage_subjects():
    teacher_id = st.session_state.teacher_data["teacher_id"]
    col1, col2 = st.columns(2)
    
    with col1:
        st.header("Manage Subjects")
    
    with col2:
        if st.button("Create New Subject", type="primary", width="stretch"):
            create_subject_dialog(teacher_id)

    subjects = get_teacher_subjects(teacher_id)
    if subjects:
        for sub in subjects:
            stats = [
                ("Students", sub["total_students"]),
                ("Classes", sub["total_classes"])
            ]
        
            def share_btn():
                if st.button(f"Share Code: {sub['name']}", key=f"share_{sub['subject_code']}", icon=':material/share:'):
                    share_subject_dialog(sub["name"], sub["subject_code"])
                st.space()
            
            subject_card(
                name = sub["name"],
                code = sub["subject_code"],
                section = sub["section"],
                stats = stats,
                footer_callback = share_btn
            )
    else:
        st.info("No Subjects Found. Create your first Subject!")



def teacher_tab_attendance_records():
    st.header("Attendance Records")



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