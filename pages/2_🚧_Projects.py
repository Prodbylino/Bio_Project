import streamlit as st
st.title("Projects")
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

code = '''(select * from table")'''
st.code(code, language='sql')