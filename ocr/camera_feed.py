import cv2

def get_camera_frame():
    # Open the camera and capture the frame
    cap = cv2.VideoCapture(0)  # 0 is default camera, change if you have multiple cameras
    ret, frame = cap.read()
    if not ret:
        return None  # Handle camera error
    return frame
