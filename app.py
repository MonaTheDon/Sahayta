import streamlit as st
import base64
import supervision as sv
from inference_sdk import InferenceHTTPClient
from PIL import Image, ImageDraw, ImageOps


st.set_page_config(page_title="Sahayta", page_icon="🤝",initial_sidebar_state='expanded')
@st.cache_data
def showGif():
    st.markdown(
            f'<img src="data:image/gif;base64,{data_url}" alt="Sahayta">',
            unsafe_allow_html=True,)

st.title("Sahayta: Help the Helping Hands🤝")
st.divider()
st.subheader("AIM 🚀")
st.markdown("Enhance disaster relief and response efforts by leveraging satellite imagery during disasters like floods and wildfires, integrating existing geospatial information, and utilizing environmental data for affected regions")
file_ = open("./assets/Sahayta.gif", "rb")
contents = file_.read()
data_url = base64.b64encode(contents).decode("utf-8")
file_.close()
showGif()
st.divider()

st.subheader("Problems in Post-Disaster Relief 👨‍🚒")
st.markdown("**👉Inaccurate Resource Allocation**")
st.markdown("**👉Information about disasters are usually shared after 15 min.**")
st.markdown("**👉Limited Situational Awareness**")
st.divider()
st.subheader("Solution 🔮")
st.image('./assets/app_asset.png')

