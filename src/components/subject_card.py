import streamlit as st

def subject_card(name, code, section, stats=None, footer_callback=None):
    html = f"""
    <div style="background-color: #faf3e8; border: 1px solid black; padding: 25px; border-radius: 20px; margin-bottom: 16px;">
        <h4 style="margin-bottom: 10px; font-size: 1.5rem">{name}</h4>
        <p style="color: black; margin: 10px 0;">Code: <span style="background: #d3e6ed;color: black;padding: 2px 8px;border-radius: 5px;">{code}</span> | Section: <span>{section}</span></p>
    """

    if stats:
        html += '<div style="display: flex; gap: 8px; flex-wrap: wrap;">'
        for label, value in stats:
            html += f'<div style="background-color: white; padding: 6px 10px; border-radius: 6px; font-size: 0.9rem; box-shadow: 0 1px 3px rgba(0,0,0,0.1);"><b>{value}</b> {label}</div>'
        html += "</div>"

    html += "</div>"


    st.markdown(html, unsafe_allow_html=True)

    if footer_callback:
        footer_callback()