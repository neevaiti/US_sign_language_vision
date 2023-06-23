import streamlit as st
from ultralytics import YOLO
from PIL import Image
from streamlit_webrtc import webrtc_streamer, RTCConfiguration, VideoTransformerBase
import av
import cv2


# streamlit run main.py
# docker build -t olaffsen/ussign .
# docker run -p 80:80 olaffsen/ussign


st.set_page_config(page_title="Computer vision", page_icon="🖥️")
st.title("US Sign Language Vision")

model = YOLO('src/model/best.pt')

# Création des onglets
tabs = st.sidebar.radio("Navigation", ("Image", "Webcam"))

# Onglet Image
if tabs == "Image":
    uploaded_file = st.file_uploader("Enter an image:", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        resized_image = image.resize((800, 800))
        results = model.predict(resized_image)
        st.image(results[0].plot())

# Onglet Webcam
if tabs == "Webcam":
    class VideoProcessor(VideVideooTransformerBase):
        def transform(self, frame):
            frm = frame.to_ndarray(format="bgr24")

            new_frm = model(frm)
            plot = new_frm[0].plot()
            frame_with_boxes = cv2.cvtColor(plot, cv2.COLOR_BGR2RGB)

            return frame_with_boxes

    webrtc_streamer(key="key", 
                    video_transformer_factory=VideoProcessor, 
                    rtc_configuration=RTCConfiguration({"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]}))
