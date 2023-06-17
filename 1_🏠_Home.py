import requests
from streamlit_lottie import st_lottie
import streamlit as st
from PIL import Image

st.set_page_config(page_title= "My Website", page_icon=":tada:",layout ="wide")



#---Animation
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
        

local_css("style/style.css")


# Image & animation loading 
lottie_coding = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_kq41y3pa.json")

# ---- LOAD images ----
img_pandas_ai = Image.open("images/pandasai_1.png")

#----Headers----
with st.container():

    st.subheader("Hi, I am Lino :wave:")
    st.title("A Data Anlyst from Melbourne")
    st.subheader("My passion is centered around data analysis, where I find joy in deciphering patterns and creating efficient solutions 💻")

#---What I do ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns((2,1))
    with left_column:
        st.header("From Concrete Blocks🧱 to Coding Blocks👨‍💻")
        # st.write("##")
        st.write(
            """
            🚧 **Construction Industry**: I Spent 3 years in the construction industry.I worked on variety of projects inclduing mining, builiding and infrastructure.I dedicated 30% of my time to handling building drawings, schedules, and contracts, and the other 70% to interacting with people.

            📊 **Found a Passion for Data**: In 2022, while working as a consultant, I realised I was using Excel for about 80% of my day. This got me thinking about ways to improve efficiency and accuracy in handling data.

            📚 **e-Learning**: Before I fully committed to data analysis, I learnt Python on freecodecamp, later enrolled in a data analysis bootcamp. I learned SQL, PowerBI, Tableau, Statistics and Machine Learning. I also used platforms like Datacamp, YouTube to continuously learn by myself.

            👨‍💻 **Learn by doing**: I am now Currently working on building data analysis tools and engaging in meaningful data analysis projects. I am trying to establish a solid portfolio as a data analyst. 

            This marks my exciting transition from the construction industry to the realm of data analysis, and I'm eager to continue this journey 📝 

            """
        )
    with right_column:
        st_lottie(lottie_coding,2, height=350,key="coding")


#--- Contacts ---


with st.container():
    st.write("---")
    st.header("Get In Touch With Me 📨") 
    st.write("##")



# #---- My Interest ----------
# lottie_coding = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_kq41y3pa.json")
# lottie_coding = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_kq41y3pa.json")
# basketball = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_wOCCGc.json")
# boxing = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_5Ag28fn9JG.json")

# with st.container():
#     st.write("---")
#     left_column, right_column = st.columns((2,1))
#     with left_column:
#         st.header("My Interests")
#         # st.write("##")

# st_lottie(basketball,'2', height=350,key="coding1")
# st_lottie(lottie_coding, height=350,key="coding2")
#         st_lottie(lottie_coding, height=350,key="coding3")
#         st_lottie(lottie_coding, height=350,key="coding4")








# add a contact form
contact_form = """
<form action="https://formsubmit.co/zzlunsw@outlook.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name", placeholder="Name" required>
     <input type="email" name="email", placeholder= "Email" required>
     <textarea name="message" placeholder="Message" required></textarea>
     <button type="submit">Send</button>
</form>

"""

left_column,right_column = st.columns(2)
with left_column:
    st.markdown(contact_form,unsafe_allow_html=True)
with right_column:
    st.empty()




