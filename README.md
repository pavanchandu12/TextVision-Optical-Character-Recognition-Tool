VisionAssist: Real-Time Object & Text Detection with Audio Feedback

A Python-based assistive tool that helps visually impaired users by detecting objects and reading out visible text from their surroundings using real-time camera input.

✨ Features

Real-Time Object Detection

Uses computer vision to identify common objects in the camera feed and announces them using text-to-speech.

OCR Text Recognition

When no objects are detected, the system switches to recognize and read out any visible text in the scene.

Text-to-Speech (TTS) Feedback

Converts detected objects or recognized text into spoken feedback for the user.

Simple User Control

Press q to quit the camera feed.

📦 Requirements

Python 3.x

OpenCV (cv2)

Pre-trained object detection module (object_detection.py)

OCR module (ocr_text_recognition.py)

Text-to-speech module (text_to_speech.py)

Install dependencies:


pip install opencv-python

pip install pytesseract

pip install pyttsx3

🚀 How to Run

1️⃣ Clone the repo:



git clone "url"

cd vision-assist

2️⃣ Run the main script:


python main.py

3️⃣ The system will open your camera, process frames, and provide audio feedback.

📁 Project Structure


vision-assist/
├── main.py                     # Main application script

├── object_detection.py         # Object detection logic

├── ocr_text_recognition.py     # OCR (text recognition) logic

├── text_to_speech.py           # Text-to-speech functionality

└── README.md                   # Project readme
