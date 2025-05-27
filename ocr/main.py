import cv2 # type: ignore
from object_detection import detect_objects
from ocr_text_recognition import recognize_text
from text_to_speech import speak_text

def process_frame(frame):
    # Try object detection
    objects = detect_objects(frame)
    if objects:
        speak_text(f"Detected objects: {', '.join(objects)}")
    else:
        # Try text recognition if no objects are detected
        text = recognize_text(frame)
        if text:
            speak_text(f"Recognized text: {text}")
        else:
            speak_text("No objects or text detected")

def main():
    cap = cv2.VideoCapture(0)  # Start video capture from camera

    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        process_frame(frame)

        cv2.imshow('Camera Feed', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
