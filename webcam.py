from streamlit_webrtc import webrtc_streamer, RTCConfiguration, VideoTransformerBase
import av
import cv2
from ultralytics import YOLO
from PIL import Image 
import requests 
import streamlit as st 




st.set_page_config(page_title="Computer vision", page_icon="🖥️")
st.title("US Sign Language Vision")

model = YOLO('src/model/best.pt')

class VideoProcessor(VideoTransformerBase):
    def transform(self, frame):
        frm = frame.to_ndarray(format="bgr24")

        new_frm = model(frm)
        plot = new_frm[0].plot()
        frame_with_boxes = cv2.cvtColor(plot, cv2.COLOR_BGR2RGB)

        return frame_with_boxes

webrtc_streamer(key="key", video_transformer_factory=VideoProcessor)




# st.set_page_config(page_title="Computer vision", page_icon="🖥️")  

# st.title("US Sign Language Vision")

# model = YOLO('src/model/best.pt')

# class VideoProcessor(VideoTransformerBase):
#     def transform(self, frame):
#         frm = frame.to_ndarray(format="bgr24")

#         new_frm = model(frm)
#         plot = new_frm[0].plot()
#         frame_with_boxes = cv2.cvtColor(plot, cv2.COLOR_BGR2RGB)
        
#         return av.VideoFrame.from_ndarray(frame_with_boxes, format="bgr24")

# webrtc_streamer(key="key", video_processor_factory=VideoProcessor, rtc_configuration=RTCConfiguration())




# st.set_page_config(page_title="Computer vision", page_icon="🖥️")
# st.title("US Sign Language Vision")

# model = YOLO('src/model/best.pt')

# class VideoProcessor(VideoTransformerBase):
#     def transform(self, frame):
#         frm = frame.to_ndarray(format="bgr24")

#         new_frm = model(frm)
#         plot = new_frm[0].plot()
#         frame_with_boxes = cv2.cvtColor(plot, cv2.COLOR_BGR2RGB)

#         return frame_with_boxes

# webrtc_streamer(key="key", video_transformer_factory=VideoProcessor)
