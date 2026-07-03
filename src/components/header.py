import streamlit as st

def header_home():
    logo_url = "https://github.com/shradha-khapra/ai-attendance-project-landing/blob/main/static/img/logo.png?raw=true"

    st.markdown(
        f"""
        <div style="display: flex; flex-direction: column; align-items:center; justify-content:center; margin-bottom:30px; margin-top:0px">
            <img src='{logo_url}' style='height: 100px;'>
            <h1 style='text-align: center; color: #213448'>SNAP<br>CLASS</h1>
        </div>
        """, unsafe_allow_html=True
    )

def header_dashboard():
    logo_url = "https://github.com/shradha-khapra/ai-attendance-project-landing/blob/main/static/img/logo.png?raw=true"

    st.markdown(
        f"""
        <div style="display:flex; align-items:center; justify-content:center; gap:10px; margin-top:0px">
            <img src='{logo_url}' style='height: 85px;'>
            <h2 style='color: #213448'>SNAP<br>CLASS</h1>
        </div>
        """, unsafe_allow_html=True
    )