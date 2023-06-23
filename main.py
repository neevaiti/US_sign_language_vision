from ultralytics import YOLO
from streamlit_webrtc import VideoTransformerBase, webrtc_streamer
import streamlit as st
import cv2
import numpy as np
from PIL import Image, ImageDraw

def load_model():
    """
    Load the YOLO model.

    Returns:
        YOLO: The loaded YOLO model.
    """
    
    model = YOLO("./src/model/best.pt")
    return model

# Créer une classe pour transformer le flux vidéo
class VideoTransformer(VideoTransformerBase):
    def __init__(self):
        self.model = load_model()

    def transform(self, frame):
        """
        Apply object detection on a video frame.

        Args:
            frame (numpy.ndarray): The input video frame.

        Returns:
            numpy.ndarray: The video frame with bounding boxes and class labels drawn on it.
        """
        
        img = frame.to_ndarray(format="bgr24")

        # Run the model
        try:
            preds = self.model(source=img, conf=0.4, iou=0.4, save=False)
        except:
            preds = []

        # Draw the predictions
        for i, result in enumerate(preds):
            for j, box in enumerate(result.boxes.data):
        
                color = (30, 215, 96) # Define the color of the rectangle

                cv2.rectangle(img,
                              (int(box[0]), int(box[1])),
                              (int(box[0] + box[2]), int(box[1] + box[3])),
                              color,
                              2)
                cv2.putText(img, 
                            f"{result.names[int(box[5])]} {box[4]:.2f}", 
                            (int(box[0]), int(box[1]-10)), 
                            cv2.FONT_HERSHEY_SIMPLEX, 
                            0.9, 
                            color, 
                            2)

        return img

# Add the prediction to the image
def draw_preds(image, preds):
    """
    Draw predictions on an image.

    Args:
        image (PIL.Image.Image): The input image.
        preds (List[ultralytics.YOLOResult]): List of YOLO detection results.

    Returns:
        PIL.Image.Image: The image with bounding boxes and class labels drawn on it.
    """
    
    draw = ImageDraw.Draw(image)

    for i, result in enumerate(preds):
        for j, box in enumerate(result.boxes.data):
            
            color = (30, 215, 96) # Define the color of the rectangle

            
            x1, y1 = int(box[0]), int(box[1])
            x2, y2 = int(box[0] + box[2]), int(box[1] + box[3])

            draw.rectangle([x1, y1, x2, y2], outline=color, width=2)

            text = f"{result.names[int(box[5])]} {box[4]:.2f}"
            draw.text((x1, y1-10), text, fill=color)

    return image

# Streamlit app
def app():
    """
    Streamlit application for sign language alphabet detection.

    Displays options to detect signs either from an image or through webcam.
    """
    
    model = load_model()
    st.header("Détection des signes de l'alphabet de l'ASL.")
    st.sidebar.title("Options :")
    option = st.sidebar.radio("Sélectionnez une option", ("Image", "Camera"))
    
    if option == "Image":
        st.header("Détection des lettres par image.")
        uploaded_file = st.file_uploader("Upload une image", type=['png', 'jpg', 'jpeg'])
        if uploaded_file is not None:
            try:
                image = Image.open(uploaded_file)
                resized_image = image.resize((800, 800))
                results = model.predict(resized_image)
                st.image(results[0].plot())
            except:
                st.error("Une erreur s'est produite lors de l'analyse de l'image.")
    
    elif option == "Camera":
        st.header("Détection des lettres (ASL) avec la webcam.")
        webrtc_streamer(key="example", video_transformer_factory=VideoTransformer)

# Exécuter l'application
app()
