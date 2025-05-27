import cv2
import pytesseract

def recognize_text(image):
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Use pytesseract to extract text
    text = pytesseract.image_to_string(gray_image)

    return text
