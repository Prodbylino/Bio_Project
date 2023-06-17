import streamlit as st
from pathlib import Path
from PIL import Image

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Lino Zhang"
PAGE_ICON = ":wave:"
NAME = "Lino Zhang"

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON,initial_sidebar_state="collapsed")

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir/'style_sub'/'resume.css'
profile_pic = '/Users/ziliangzhang/Desktop/Real_Project/Bio_Project/images/lino.png'

# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

# profile_pic = Image.open(profile_pic)


DESCRIPTION = """
    As a data analyst with experience in project management, I bring a unique perspective to projects. With expertise in
data extraction, analysis, and visualisation, I can interpret data comprehensively for all stakeholders to help
organisations make informed decisions. I am committed to continuous learning, always exploring new ideas and
technologies to help drive business success.

"""
email = "zzlusnw@outlook.com"
mobile = "0478 556 182"
LinkedIn = "www.linkedin.com/in/linozhanglink"
GitHub = "https://github.com"

# PROJECTS = {
#     "🏆 Sales Dashboard - Comparing sales across three stores": "https://youtu.be/Sb0A9i6d320",
#     "🏆 Income and Expense Tracker - Web app with NoSQL database": "https://youtu.be/3egaMfE9388",
#     "🏆 Desktop Application - Excel2CSV converter with user settings & menubar": "https://youtu.be/LzCfNanQ_9c",
#     "🏆 MyToolBelt - Custom MS Excel add-in to combine Python & Excel": "https://pythonandvba.com/mytoolbelt/",
# }


# --- HERO SECTION ---

st.title(NAME)

col1, col2 = st.columns(2, gap = 'small')
with col1:
    st.write(email)
    
# with col2:
    # st.write("📲:", mobile)

with col2:
    st.write(LinkedIn)
    
    # st.write("github", GitHub)
st.subheader("Professional Summary")
# st.write("---")
st.write(DESCRIPTION)


# --- EXPERIENCE & QUALIFICATIONS ---
# st.write('\n')
st.subheader("Experience & Qulifications")
# st.write("---")
st.write(
    """
- ✔️ 3 Years expereince in project management
- ✔️ Strong hands on experience and knowledge in Python, SQL and Excel
- ✔️ Good understanding of data warehousing
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)


# --- SKILLS ---
# st.write('\n')
# col1, col2 = st.columns((2,1))
# with col1:

st.subheader("Technical Skills")
# st.write("---")
st.write(
        """
    - 👨‍💻 Programming: Python (Scikit-learn, Pandas,Numpy), SQL, 
    - 📊 Data Visulization: PowerBI, Tableau, Matplotlib, Plotly, Streamlit, Excel
    - ⚙️ Modeling: Logistic regression, linear regression,
    - 🗄️ Databases: Postgres, MongoDB, MySQL,AWS S3
    """
    )
# with col2:
#     st.subheader("Soft Skills")
#     st.write(
#         """
#     - 👩‍💻 Critical Thinking | Stakeholder Communication | Project Management | Collaboration | Problem-Solving
#     """
#     )

# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Consultant | TBH**")
st.write("10/2021 - 04/2022")
st.write(
    """
- ► Strategically developed and deployed PowerBI dashboards, focusing on project delivery status and financial metrics,
which facilitated data-driven decision-making processes. Effectively communicated insights to senior project managers,
supporting them in successfully identifying opportunities for strategic project improvement and cost control.
- ► Developed comprehensive construction project schedules using Microsoft Project (Project Scheduling Tool). Communicated potential risks to
clients promptly, fostering transparency and client trust
- ► Established a risk model that analysed the risk impact on light-rail project milestone dates using Excel (Pivot Table),
identified the key risk factors, and brought the delivery milestone 2 months earlier
- ► Assisted senior PMO specialist in developing PMO uplift recommendation reports for a mining organisation including
interviewing over 20 client-side Projects Managers. Developed quick-wins solution report for the client
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Junior Project Manager | Handymel Construction**")
st.write("03/2020 - 04/2021")
st.write(
    """
- ► Oversaw the entire construction phases, successfully delivered over 20 projects
- ► Conducted Cost Estimation on foundation system and steel framing system, accurately quoted over 40 projects


"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", "**Contract Administrator | Sydbuilt Projects**")
st.write("03/2018 - 11/2019")
st.write(
    """
- ► Liaised with builders and contractors to ensure the quality of the work achieved per contract
- ► Managed tender submissions (Increased project tender capability and efficiency by at least 30%)
"""
)



st.subheader("Side Projects")
st.write("---")

# --- Project 1

st.write("💡", "**PandasAI - Excel Anlysis Tool ( http://54.206.224.58:8501/ )**")
st.write(
    """
- ► Developed and deployed a Streamlit web app that allow user to upload CSV / xlsx fils, that allows OPENAI LLM analyse the file with user's prompt. Deployed project on AWS EC2.
"""
)

# --- Project 2

st.write("💡", "**Accenture Bootcamp - DevOps Data Anlysis**")
st.write(
    """
- ► Collaborated with a cross-functional team to develop a DevOps analytical tool during a 4-day on-site bootcamp, optimizing
the workflow of DevOps practices and showcasing a solid understanding of AWS serverless solutions
- ► Led the creation of compelling presentation materials, successfully pitching the project to diverse teams and senior
management, demonstrating strong communication and leadership skills
"""
)

# --- Project 3

st.write("💡", "**Business Insights 360- Data Analyst Project at Codebasics.io**")
st.write(
    """
- ► Designed and implemented a comprehensive dashboard from scratch in Power BI for various departments including
finance, sales, marketing, supply chain, and executives, contributing to substantial gross margin improvement
"""
)

st.write('\n')
st.subheader("Education")
# st.write("---")

st.write("📚", "**Monash University Bootcamp |        2021 - 2022**")
st.markdown("Data Analytics [(Link to Certificate)](https://www.credly.com/badges/2de05180-dafd-49d5-bd83-88653e4b6237/linked_in)")
st.write('\n')
st.write("📚", "**University of New South Wales (UNSW) |        2017-2020**")
st.write("Bachelor of Construction Management")