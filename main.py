import streamlit as st
from ultralytics import YOLO
from PIL import Image

st.title("Détection des signes de l'alphabet en ASL (American Sign Language)")

uploaded_file = st.file_uploader("Choisir un fichier :", type=["jpg", "jpeg", "png"])

model = YOLO("./src/model/best.pt")

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    resized_image = image.resize((800, 800))
    results = model.predict(resized_image)
    st.image(results[0].plot())
