import streamlit as st
import requests
from PIL import Image
import io
import base64

st.set_page_config(page_title="Gun Detection", layout="centered")
st.title("🔫 Gun Detection System")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    if st.button("Detect Gun"):
        files = {"image": uploaded_file.getvalue()}
        try:
            res = requests.post("http://127.0.0.1:5000/detect", files={"image": uploaded_file})
            if res.status_code == 200:
                detected_img_b64 = res.json()["image"]
                detected_img = Image.open(io.BytesIO(base64.b64decode(detected_img_b64)))
                st.image(detected_img, caption="Detection Result", use_column_width=True)
            else:
                st.error("Detection failed.")
        except Exception as e:
            st.error(f"Error connecting to backend: {e}")
