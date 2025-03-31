import streamlit as st
import numpy as np
from utils import *
import tempfile
import os
import cv2

def sidebar_navigation():
    st.sidebar.title("🌾 Agriculture Assistant")
    page = st.sidebar.selectbox("Navigate to:", ["🌿 Crop Disease Analyzer"])
    return page

def crop_disease_analyzer():

    format_project()
    st.title("🌿 Crop Disease Analyzer")
    st.markdown("#### Upload a crop image to detect diseases and get a detailed analysis.")

    uploaded_file = st.file_uploader("📤 Upload a crop image (JPEG/PNG)...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        st.subheader("📊 Visual and Analytical Report")
        col1, col2 = st.columns([1, 1])

        button = st.button("🔍 Analyze crop")

        with col1:
            with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp_file:
                tmp_file.write(uploaded_file.getvalue())
                tmp_file_path = tmp_file.name
            display_uploaded_image(uploaded_file)

        if button:
            with col2:
                with st.spinner("Analyzing image..."):
                    model_path = "models/model.pt"
                    annotated_image = inference(model_path, tmp_file_path)
                    annotated_image_rgb = cv2.cvtColor(annotated_image, cv2.COLOR_BGR2RGB)
                    st.image(annotated_image_rgb, caption="Inference Output with Bounding Boxes", use_container_width=True)

            with st.spinner("Generating detailed analysis..."):
                prompt = build_prompt()
                response = generate_gemini_response(prompt, tmp_file_path)
                with st.expander("📋 **Click here to see the Detailed Analysis Report**", expanded=True):
                    st.markdown(response)

        os.unlink(tmp_file_path)
    else:
        st.info("Upload an image to start the analysis.")

    st.markdown("""
        ---
        **Disclaimer:** The information provided is based on expert plant pathology analysis. 
        Please consult with agricultural experts before implementing any treatments or strategies.
    """)

def main():
    st.set_page_config(page_title="AgriSure - Your Agriculture Assistant", page_icon="🌾", layout="wide")
    format_project()
    page = sidebar_navigation()

    if page == "🌿 Crop Disease Analyzer":
        crop_disease_analyzer()

    outro()

if __name__ == '__main__':
    main()
