import cv2
import numpy as np

def load_classes(filename):
    with open(filename, "r") as f:
        classes = [line.strip() for line in f.readlines()]
    return classes

def detect_objects(frame):
    # Load the YOLO model
    net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
    
    # Prepare the frame for object detection
    height, width = frame.shape[:2]
    blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
    net.setInput(blob)

    # Get the output layer names
    layer_names = net.getLayerNames()
    output_layers_indices = net.getUnconnectedOutLayers()
    
    # Check if the output layer indices is a scalar or an array
    if isinstance(output_layers_indices, np.ndarray):
        output_layers = [layer_names[i - 1] for i in output_layers_indices.flatten()]
    else:
        output_layers = [layer_names[output_layers_indices - 1]]  # Handle scalar case

    # Perform forward pass to get output
    outputs = net.forward(output_layers)

    # Process the outputs to extract detected objects
    classes = load_classes("coco.names")  # Load class names
    detected_objects = []
    for output in outputs:
        for detection in output:
            scores = detection[5:]  # Get class scores
            class_id = np.argmax(scores)  # Get the index of the class with max score
            confidence = scores[class_id]  # Get the confidence score
            if confidence > 0.5:  # Filter out weak detections
                detected_objects.append(classes[class_id])  # Append class name

    return detected_objects  # Return the list of detected objects
