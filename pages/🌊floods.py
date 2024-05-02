import streamlit as st

st.set_page_config(page_title='Flood', page_icon='🌊', initial_sidebar_state='expanded')
st.title("Floods Masking and Segmentation Model 🌊")

st.markdown("AI techniques are applied for data analysis and decision support, including semantic segmentation of satellite imagery,and optimization of resource allocation. These algorithms provide actionable insights to emergency responders and relief agencies, aiding in strategic planning and response coordination.")
st.divider()
st.subheader("How ?")
st.markdown("Segmentation of Floods in Satellite Images can be done using U-NET architecture")
st.divider()
st.subheader("Technologies")
st.markdown("**Model:** U-NET Model")
st.markdown("**Model Architecture:** ")
st.image('./assets/floods/model_plot.png')
st.markdown("**Accuracy:** 91.76%")
st.divider()
st.subheader("Results")
st.image('./assets/floods/output_flood_segmentation.png')