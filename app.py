"""Invendo AI Academy - Project 1: AI Image Inspection.

Run from the VS Code terminal: python -m streamlit run app.py
"""

from io import BytesIO

import pandas as pd
import streamlit as st
from PIL import Image, ImageOps
from ultralytics import YOLO


st.set_page_config(page_title="AI Image Inspection", page_icon="🔎", layout="wide")


@st.cache_resource
def load_model():
    """Load the pretrained detection model once and reuse it."""
    return YOLO("yolo11n.pt")


st.title("🔎 AI Image Inspection Tool")
st.caption("Invendo AI Academy • Beginner Computer Vision Project")
st.write(
    "Upload a photograph. The AI model will find common objects, "
    "draw bounding boxes, and create a detection report."
)

threshold = st.slider(
    "Minimum confidence", min_value=0.10, max_value=0.90, value=0.30, step=0.05
)
uploaded_file = st.file_uploader("Upload a JPG or PNG image", type=["jpg", "jpeg", "png"])

if uploaded_file is None:
    st.info("Choose an image above to begin.")
else:
    try:
        original_image = ImageOps.exif_transpose(Image.open(uploaded_file)).convert("RGB")
    except Exception:
        st.error("The uploaded file could not be opened as an image.")
        st.stop()

    with st.spinner("AI is inspecting your image..."):
        try:
            model = load_model()
            result = model.predict(
                source=original_image, conf=threshold, verbose=False
            )[0]
        except Exception as error:
            st.error(f"Model could not run: {error}")
            st.info("Check your internet connection on the first run, and the installed packages.")
            st.stop()

    # Ultralytics draws on a BGR image; convert it into RGB for the browser.
    annotated_image = Image.fromarray(result.plot()[..., ::-1])

    left, right = st.columns(2)
    with left:
        st.subheader("Original photo")
        st.image(original_image)
    with right:
        st.subheader("AI detections")
        st.image(annotated_image)

    rows = []
    for box in result.boxes:
        coordinates = [round(float(v), 1) for v in box.xyxy[0].tolist()]
        rows.append(
            {
                "Object": result.names[int(box.cls.item())],
                "Confidence (%)": round(float(box.conf.item()) * 100, 1),
                "X1": coordinates[0],
                "Y1": coordinates[1],
                "X2": coordinates[2],
                "Y2": coordinates[3],
            }
        )

    report = pd.DataFrame(
        rows, columns=["Object", "Confidence (%)", "X1", "Y1", "X2", "Y2"]
    )
    st.metric("Objects detected", len(report))
    st.subheader("Detection report")

    if report.empty:
        st.warning("No objects detected at this confidence threshold. Try another image or a lower threshold.")
    else:
        st.dataframe(report, hide_index=True)

    image_buffer = BytesIO()
    annotated_image.save(image_buffer, format="PNG")
    image_bytes = image_buffer.getvalue()

    image_col, csv_col = st.columns(2)
    with image_col:
        st.download_button(
            "Download detected image",
            data=image_bytes,
            file_name="detected_image.png",
            mime="image/png",
        )
    with csv_col:
        st.download_button(
            "Download CSV report",
            data=report.to_csv(index=False).encode("utf-8"),
            file_name="detections.csv",
            mime="text/csv",
        )

st.divider()
st.caption(
    "Educational demo: this model detects common object categories. "
    "It does not identify people or reliably infer dangerous behaviour. "
    "Use photos you have permission to process."
)
