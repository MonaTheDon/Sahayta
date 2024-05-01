import streamlit as st
import base64
from inference_sdk import InferenceHTTPClient
from PIL import Image, ImageDraw, ImageOps

def detectVictim(api_key, image):
    size = (640,640)    
    image = ImageOps.fit(image, size)
    try:
        CLIENT = InferenceHTTPClient(
            api_url="https://detect.roboflow.com",
            api_key=api_key
        )
        result = CLIENT.infer(image, model_id="water-level-sindh/6")
        if 'predictions' in result:
            return result['predictions']
        else:
            st.error("Failed to get predictions from the model.")
            return None
    except Exception as e:
        if "403 Client Error: Forbidden" in str(e):
            st.error("Invalid API Key. Please check your API key and try again.")
        else:
            st.error(f"An error occurred: {e}")
        return None

def draw_bounding_box(image, predictions):
    draw = ImageDraw.Draw(image)
    for prediction in predictions:
        x = prediction['x']
        y = prediction['y']
        width = prediction['width']
        height = prediction['height']
        draw.rectangle([x, y, x+width, y+height], outline="red", width=3)
        draw.text((x, y), prediction['class'], fill="red")

def main():
  st.set_page_config(page_title="Sahayta", page_icon="🤝")

  st.title("Sahayta: Help the Helping Hands 🤝")
  st.subheader("Let's Test the Victim Detection Model")

  higherClass=['level 5','level 6', 'level 7', 'level 8', 'level 9', 'level 10', 'level 11', 'level 12']

  api_key = st.text_input("Enter API Key")
  uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])
  if uploaded_file is not None:
     if api_key is not None:
         image = Image.open(uploaded_file)
         predictions=detectVictim(api_key,image)
         if predictions:
          draw_bounding_box(image, predictions)
          st.image(image, caption='Processed Image', use_column_width=True)
          for entity in predictions:
            # st.write(entity['class'])
            if entity['class'] == 'flood':
               st.subheader("**Flood is detected**")
            elif entity['class'] in higherClass:
               st.subheader(f"High level of Flood Detected: :red[{entity['class']}]")
            else:
               st.subheader(f"Low Flood levels detected: :green[{entity['class']}]")
            
     else:
        st.error("Add Valid Roboflow API Key")

if __name__ == "__main__":
    main()

