import streamlit as st

def style_bg_home():

    st.markdown("""
        <style>
                
                .stApp {
                    background: #EAE0CF;
                }

                .stApp div[data-testid="stColumn"]{
                    background-color: #faf3e8 !important;
                    padding: 2.5rem !important;
                    border-radius: 3rem !important;
                    box-shadow: 0 6px 20px rgba(0,0,0,0.08) !important;
                }

        </style>
    """, unsafe_allow_html=True)

def style_bg_dashboard():

    st.markdown("""
        <style>
                
                .stApp {
                    background: #EAE0CF;
                }

        </style>
    """, unsafe_allow_html=True)




def style_base_layout():

    st.markdown("""
        <style>
                @import url('https://fonts.googleapis.com/css2?family=Urbanist:ital,wght@0,100..900;1,100..900&display=swap');
                @import url('https://fonts.googleapis.com/css2?family=Stack+Sans+Headline:wght@200..700&display=swap');
                @import url('https://fonts.googleapis.com/css2?family=BBH+Hegarty&display=swap');

                /* Hide Toolbar */
                #MainMenu, footer, header{
                    visibility: hidden;
                }

                .block-container{
                    padding-top: 1.5rem !important;
                }

                h1{
                    font-family: "BBH Hegarty", sans-serif !important;
                    font-size: 3rem !important;
                    line-height: 1.1 !important;
                    margin-bottom: 0rem !important;
                    color: #213448 !important;
                }

                h2{
                    font-family: "BBH Hegarty", sans-serif !important;
                    font-size: 1.5rem !important;
                    line-height: 1.1 !important;
                    margin-bottom: 0rem !important;
                    color: #213448 !important;
                }
                
                h3, h4, p{
                    font-family: "Urbanist", sans-serif !important;
                }

                button{
                    border-radius: 1.5rem !important;
                    background: #213448 !important;
                    color: white !important;
                    padding: 10px 20px !important;
                    border: none !important;
                    transition: transform 0.25s ease-in-out !important;
                }

                button[kind="secondary"]{
                    border-radius: 1.5rem !important;
                    background: #547792 !important;
                    color: white !important;
                    padding: 10px 20px !important;
                    border: none !important;
                    transition: transform 0.25s ease-in-out !important;
                }


                button[kind="tertiary"]{
                    border-radius: 1.5rem !important;
                    background: black !important;
                    color: white !important;
                    padding: 10px 20px !important;
                    border: none !important;
                    transition: transform 0.25s ease-in-out !important;
                }

                button:hover{
                    transform: scale(1.05);
                }


        </style>
    """, unsafe_allow_html=True)