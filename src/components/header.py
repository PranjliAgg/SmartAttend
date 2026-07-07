import streamlit as st

import base64

with open("src/img/logo_final.png", "rb") as f:
    logo = base64.b64encode(f.read()).decode()

def header_home():

    st.markdown(
        f"""
        <div style="display: flex; flex-direction: column; align-items:center; justify-content:center; margin-bottom:30px; margin-top:0px">
            <img src='data:image/png;base64,{logo}' style='height: 100px;'>
            <h1 style='text-align: center; color: #213448'>SmartAttend</h1>
        </div>
        """, unsafe_allow_html=True
    )

def header_dashboard():

    st.markdown(
        f"""
        <div style="display:flex; align-items:center; justify-content:center; gap:10px; margin-top:0px">
            <img src='data:image/png;base64,{logo}' style='height: 85px;'>
            <h2 style='color: #213448'>Smart<br>Attend</h1>
        </div>
        """, unsafe_allow_html=True
    )