import streamlit as st
from PIL import Image
import requests
from streamlit_lottie import st_lottie

#---Animation
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# ---- LOAD images ----
img_pandas_ai = Image.open("images/pandasai_1.png")

st.title("My Projects")

#---Project---

with st.container():
    st.write("---")
    
    # st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_pandas_ai)
    with text_column:
        st.subheader("AI Powered Data Analysis Tool")
        # st.write("")
        st.markdown("I built a streamlined data analysis web app that incoperates AI power from OPENAI API. The application allows users to upload CSV or XLSX files, enter prompts, and AI will generate the insights or plot the graphs. This makes time efficient data analysis. With this application, users can performe basic analysis with their data. Try it out here: http://54.206.224.58:8501/")
        st.markdown("Github Repo: https://github.com/Prodbylino/PandasAI_Streamlit_Project.git")

with st.container():
    st.write("---")
    
    # st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        web_scrapping = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_4AVFntm5f7.json")
        st_lottie(web_scrapping,'2', width = 200, height=200,key="web_scrapping")
    with text_column:
        st.subheader("Stock Web Scrapping - ETL Project")
        st.write("This is an ETL project which scrapes several pages of the most recent data from the Yahoo Finance website regarding the CBA and ANZ stocks information. Data is loaded into MangoDB")
        
        st.markdown("Github Repo: https://github.com/Prodbylino/ETL-Project_Yahoo-Finance.git")
