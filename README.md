# ASL Alphabet Sign Detection

![ASL Alphabet Sign Detection](src/images/x_predict.jpg)

## Introduction

This project aims to detect and recognize American Sign Language (ASL) alphabet signs in images and real-time video using deep learning and computer vision techniques. It leverages the Ultralytics YOLOv8 object detection framework and Streamlit for building an interactive web application.

## Features

- Object detection and recognition of ASL alphabet signs
- Support for both image-based and real-time webcam-based detection
- User-friendly web interface for easy interaction
- Display of bounding boxes and class labels on detected signs

## Requirements

- Python 3.11
- Streamlit
- Ultralytics YOLO
- OpenCV
- PIL
- Docker (optional)

## Installation

1. Clone the repository:
```bash 
git@github.com:neevaiti/US_sign_language_vision.git
```


2. Install the required Python packages:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the Streamlit app:
```bash
streamlit run main.py
```

2. Access the application via the provided URL in the terminal.

3. Select the desired option ("Image" or "Camera") from the sidebar.

4. Follow the instructions for image-based or webcam-based detection.


## Docker

Alternatively, you can run the application using Docker for easier setup and deployment. Here's how:

1. Pull the Docker image from the Docker Hub:
```bash
docker pull neevaiti/asl-detect-app:v1.0
```

2. Run the Docker container:
```bash
docker run -p 80:80 neevaiti/asl-detect-app:v1.0
```


3. Access the application by opening your web browser and navigating to `http://localhost:8501`.

## Customization

- You can adjust the confidence threshold and IOU values in the code to change the detection accuracy and speed.
- To modify the appearance of bounding boxes and class labels, you can change the colors and text properties in the `transform` and `draw_preds` methods of the `VideoTransformer` class.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

- [Ultralytics YOLOv8](https://docs.ultralytics.com/models/yolov8/)
- [Streamlit](https://streamlit.io)
- [OpenCV](https://opencv.org)
- [PIL](https://python-pillow.org)
- [Docker](https://www.docker.com/)
- [Docker model image](https://hub.docker.com/layers/neevaiti/asl-detect-app/v1.0/images/sha256:af56ccc197ca07b38cb7fe7c6da8b7fd82a513718f887896d2800dec61f5c4cf)
- [Dataset](https://universe.roboflow.com/gerdus-kemp/american-sign-language-letters-rarfr)

## Authors

- [@Olaffson](https://github.com/Olaffson)
- [@neevaiti](https://github.com/neevaiti)