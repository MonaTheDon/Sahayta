import streamlit as st
from streamlit_card import card
import base64

st.set_page_config(page_title="Sahayta", page_icon="")

st.title("Sahayta: Provide a Helping Hand")
st.subheader("Let's Test the utilities")

with open('./assets/wildfires.jpg', "rb") as f:
    data = f.read()
    encoded = base64.b64encode(data)
data = "data:image/png;base64," + encoded.decode("utf-8")

hasClicked = card(
  title="Test Wildfires",
  text="Some description",
  image=data,
  on_click=lambda: print("Clicked!")
)