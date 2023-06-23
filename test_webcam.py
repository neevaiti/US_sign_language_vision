import cv2
import streamlit as st
from moviepy.editor import VideoFileClip
from moviepy.video.io.ffmpeg_writer import FFMPEG_VideoWriter


cap = cv2.VideoCapture(1)

st.title("Video")

frame_placeholder = st.empty()

stop_button_pressed = st.button("Stop")

while cap.isOpened() and not stop_button_pressed:

    ret, frame = cap.read()

    if not ret:
        st.write("The video capture is ended.")
        break

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    frame_placeholder.image(frame, channels="RGB")

    if cv2.waitKey(1) & 0xFF == ord("q") or stop_button_pressed:
        break

cap.release()
cv2.destroyAllWindows()








# Fonction pour capturer et afficher la vidéo de la webcam
def capture_video():
    # Créer l'objet de capture vidéo pour la webcam
    cap = cv2.VideoCapture(0)  # Utilisez 1 au lieu de 0 si vous avez plusieurs webcams

    # Récupérer les propriétés de la vidéo
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Définir le nom du fichier temporaire pour la vidéo
    output_file = "webcam_temp.mp4"

    # Créer un écrivain vidéo avec les propriétés de la vidéo de la webcam
    video_writer = FFMPEG_VideoWriter(output_file, (width, height), fps)

    # Boucle pour capturer les images de la webcam et les ajouter à la vidéo
    while True:
        # Lire l'image de la webcam
        ret, frame = cap.read()

        # Vérifier si la capture a réussi
        if not ret:
            break

        # Ajouter l'image à la vidéo
        video_writer.write_frame(frame)

        # Afficher l'image dans Streamlit
        st.image(frame, channels="BGR")

        # Vérifier si l'utilisateur a appuyé sur la touche 'Esc' pour arrêter la capture
        if cv2.waitKey(1) == 27:
            break

    # Fermer l'écrivain vidéo
    video_writer.close()

    # Libérer les ressources
    cap.release()


def read_video():
    video_file = open('webcam_temp.mp4', 'rb')
    video_bytes = video_file.read()

    # Afficher la vidéo dans Streamlit
    st.video(video_bytes, start_time=0)


# Appeler la fonction de capture vidéo dans Streamlit
# capture_video()

# Appeler la fonction de lecture vidéo dans Streamlit
read_video()