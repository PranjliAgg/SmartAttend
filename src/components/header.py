import streamlit as st

def header_home():
    logo_url = "https://github.com/shradha-khapra/ai-attendance-project-landing/blob/main/static/img/logo.png?raw=true"
    logo_path = "src/img/logo_transparent.png"

    col1, col2 = st.columns([2, 5])

    with col1:
        st.image(logo_path, width=100)


    with col2:
        st.markdown(
            """
            <h1 style="color:#213448;">SmartAttend</h1>
            """,
            unsafe_allow_html=True,
        )

    st.markdown(
        """
        <h3 style="color: #213448;">AI-Powered Attendance System</h3>
        <p style="color: #213448;">Automating attendance using face recognition and voice verification to eliminate proxy entries</p>
        """,
        unsafe_allow_html=True
    )