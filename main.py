import streamlit as st
from ultralytics import YOLO
from PIL import Image

st.title("US Sign Language Vision")

uploaded_file = st.file_uploader("Enter an image :", type=["jpg", "jpeg", "png"])

model = YOLO('best.pt')

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    resized_image = image.resize((800, 800))
    results = model.predict(resized_image)
    st.image(results[0].plot())

