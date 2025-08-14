from ultralytics import YOLO
import cv2
import numpy as np
import base64
import os

# Load model once
MODEL_PATH = os.path.join(os.path.dirname(__file__), "..", "model", "best.pt")
model = YOLO(MODEL_PATH)

def detect_gun(image_bytes):
    # Convert bytes to OpenCV image
    nparr = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # Run detection
    results = model(img)
    annotated = results[0].plot()

    # Encode to base64
    _, buffer = cv2.imencode('.jpg', annotated)
    return base64.b64encode(buffer).decode('utf-8')
