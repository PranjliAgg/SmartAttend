import streamlit as st

def footer_home():
    st.markdown(
        """
        <div style="display: flex; flex-direction: column; align-items:center; justify-content:center; margin-bottom:30px; margin-top:30px">
            <p style="font-weight: bold; color: #213448;">© 2026 • Built by Pranjli & Alden</p>
        </div>
        """, unsafe_allow_html=True
    )


def footer_dashboard():
    st.markdown(
        """
        <div style="display: flex; flex-direction: column; align-items:center; justify-content:center; margin-bottom:30px; margin-top:30px">
            <p style="font-weight: bold; color: #213448; opacity: 0.6;">© 2026 • Built by Pranjli & Alden</p>
        </div>
        """, unsafe_allow_html=True
    )