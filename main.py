import streamlit as st
from ultralytics import YOLO
from PIL import Image

# pour une image

st.title("US Sign Language Vision")

uploaded_file = st.file_uploader("Enter an image :", type=["jpg", "jpeg", "png"])

model = YOLO('src/model/best.pt')

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    resized_image = image.resize((800, 800))
    results = model.predict(resized_image)
    st.image(results[0].plot())


# pour une video

# import cv2
# from moviepy.editor import VideoFileClip

# st.title("Traitement et lecture de vidéos")

# uploaded_file = st.file_uploader("Choisir une vidéo au format MP4", type=["mp4"])

# if uploaded_file is not None:
#     # Lecture de la vidéo avec OpenCV
#     video_bytes = uploaded_file.read()
#     video_path = "uploaded_video.mp4"
    
#     with open(video_path, "wb") as video_file:
#         video_file.write(video_bytes)
    
#     # Traitement de la vidéo
#     processed_video_path = "processed_video.mp4"
    
#     # Ouverture de la vidéo avec OpenCV
#     video_capture = cv2.VideoCapture(video_path)
    
#     # Obtention des propriétés de la vidéo
#     fps = video_capture.get(cv2.CAP_PROP_FPS)
#     frame_size = (
#         int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH)),
#         int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
#     )
    
#     # Création de l'objet VideoWriter pour enregistrer la vidéo traitée
#     codec = cv2.VideoWriter_fourcc(*"mp4v")
#     video_out = cv2.VideoWriter(processed_video_path, codec, fps, (800, 800))
    
#     # Traitement frame par frame
#     while video_capture.isOpened():
#         ret, frame = video_capture.read()
        
#         if not ret:
#             break
        
#         # Redimensionner la frame à 800x800 pixels
#         resized_frame = cv2.resize(frame, (800, 800))
        
#         resized_frame = model.predict(resized_frame)

#         # Écrire la frame traitée dans la vidéo de sortie
#         video_out.write(resized_frame)
    
#     # Fermeture des objets de capture et de sortie vidéo
#     video_capture.release()
#     video_out.release()
    
#     st.success("Traitement vidéo terminé.")
    
#     # Lecture et affichage de la vidéo traitée
#     st.subheader("Lecture de la vidéo traitée")
    
#     st.video(processed_video_path)

    # video_clip = VideoFileClip(processed_video_path)
    
    # for frame in video_clip.iter_frames():
    #     st.image(frame)
    
    # video_clip.close()



