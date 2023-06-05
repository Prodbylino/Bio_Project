import requests
from streamlit_lottie import st_lottie
import streamlit as st

st.set_page_config(page_title= "My Website", page_icon=":tada:",layout ="wide")
# if "my_input" not in st.session_state:
#     st.session_state["my_input"] =""

# my_input = st.text_input("Input a text here",st.session_state["my_input"])
# submit = st.button("Submit")
# if submit:
#     st.session_state["my_input"] = my_input
#     st.write("You entered",my_input)



#-----Sidebar----------------




#---Animation
def load_lotti(url):
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
lottie_coding = load_lotti("https://assets1.lottiefiles.com/packages/lf20_kq41y3pa.json")

# img_contact_form = Image.open("None")
# img_lottie_animation = Image.open("None")

#----Headers----
with st.container():

    st.subheader("Hi, I am Lino :wave:")
    st.title("A Data Anlyst from Melbourne")
    st.write("I have few years of experience in project mangement and I am transitioning my career into tech industry")

#---What I do ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """


            """
        )
    with right_column:
        st_lottie(lottie_coding,height=350,key="coding")

#---Project---

with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        None
    with text_column:
        st.subheader("project Name")
        st.subheader("###")
        st.write("ddd")
        st.markdown("dddd")


#--- Contacts ---


with st.container():
    st.write("---")
    st.header("Get In Touch With Me") 
    st.write("##")


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
