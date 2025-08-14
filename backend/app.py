from flask import Flask, request, jsonify
from utils.detector import detect_gun
import base64

app = Flask(__name__)

@app.route('/detect', methods=['POST'])
def detect():
    if 'image' not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    file = request.files['image']
    image_bytes = file.read()

    detected_img = detect_gun(image_bytes)
    return jsonify({"image": detected_img})

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
