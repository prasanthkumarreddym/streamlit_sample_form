import streamlit as st
import os
import requests
#from streamlit_lottie import st_lottie


st.set_page_config(layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coder = load_lottieurl("https://lottie.host/03eed002-5781-468d-81f6-cb24126cc813/v7utSiUDEO.json")
lottie_about = load_lottieurl("https://lottie.host/655e891d-da17-478d-ac04-03110002e4d0/dP16rwEUwV.json")
lottie_skills = load_lottieurl("https://lottie.host/610a4a50-6ebc-4b4d-a4c0-fed64c9ab24c/3kYgbLOqna.json")
lottie_home = load_lottieurl("https://lottie.host/610a4a50-6ebc-4b4d-a4c0-fed64c9ab24c/3kYgbLOqna.json")
lottie_contact = load_lottieurl("https://lottie.host/183de52a-d872-4911-8604-88a78e072a02/bdNCmM0s2E.json")


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)
local_css(r"C:\Users\mosal\Desktop\streamlit\style\style.css")


col1, col2, col3= st.columns([1,1,1])
with col2:
    st.header("SAMPLE FORM")
st.write("##")

col1, col2, col3= st.columns([1,3,1])
with col1:
    st.lottie(lottie_contact)

with col2:    
    contact_form = """
    <form action = "https://formsubmit.co/prasanthkumar5608@gmail.com" method = "POST">
     <input type = "hidden" name = "_captcha" value = "false">
     <input type = "text" name = "name" placeholder = "Your Name" required>
     <input type = "email" name = "email" placeholder = "Your email" required>
     <textarea name = "message" placeholder = "Your Message" required></textarea>
     <button type = "submit">send</button>
    </form>

        """
    st.markdown(contact_form, unsafe_allow_html = True)

st.write("##")

st.subheader("~ It is created for practice purpose only. However it works and you can also send your thoughts/MESSAGES in this sample form. \n * TRY ONCE IF YOU ARE INTRESTED...")
st.write("---")
st.write("* It is my first streamlit app, I just wanted to know how it looks and works.")
st.write("* Apart from that, And i just created this contact form for the purpose of how to deploy this streamlit app in streamlit cloud.")

col1, col2, col3, col4, col5 = st.columns([1,1,1,1,1])
with col5:
    st.write('M.Prasanth Kumar Reddy')

st.balloons()





        
        


