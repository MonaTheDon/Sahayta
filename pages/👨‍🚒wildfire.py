import streamlit as st

st.set_page_config(page_title='WildFire', page_icon='👨‍🚒', initial_sidebar_state='expanded')
st.title("Detect Early Wildfires 👨‍🚒")

st.markdown("The solution utilizes satellite imagery, particularly NOAA-20 satellites called VIIRS, for detection of Wildfires in early stages so that Disaster Relief teams can be sent the information before, expeding Disaster Relief.")
st.divider()
st.subheader("How ?")
st.markdown("Using Deep Learning models (CNN) we can detect Wildfires from satellite Images as the model learns the changes in vegetation density and area landscape")
st.divider()
st.subheader("Technologies")
st.markdown("**Model:** Pretrained RESNET101 _(Transfer Learning is applied)_ ")
st.markdown("**Accuracy:** 90.5%")
st.markdown("**Area Under Curve (AUC):** 94.23%")
st.markdown("**Confusion Matrix**")
st.image('./assets/wildfire/confusion_mat.png')
st.divider()
st.subheader("Results")
st.image('./assets/wildfire/results.png')
