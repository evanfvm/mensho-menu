import streamlit as st
from streamlit_pdf_viewer import pdf_viewer

st.markdown(hide_streamlit_style, unsafe_allow_html=True)

with st.container(border=True):
    pdf_viewer("menu.pdf", width=1000, pages_vertical_spacing=10)
