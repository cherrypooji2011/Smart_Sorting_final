import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image

# Load trained model
model = load_model("rotten_fruit_classifier.h5")

# Streamlit UI setup
st.set_page_config(page_title="🍎 Smart Sorting - Fruit Classifier")
st.title("🍏 Smart Sorting: Fresh vs Rotten")
st.markdown("Upload a fruit or vegetable image to check if it's **Fresh** or **Rotten**.")

# File uploader
uploaded_file = st.file_uploader("📤 Upload an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Load and display image
    img = Image.open(uploaded_file)
    st.image(img, caption="🖼 Uploaded Image", use_column_width=True)

    # Preprocess the image
    img = img.resize((224, 224))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    # Predict using the model
    prediction = model.predict(img_array)[0][0]
    st.subheader(f"🧠 Prediction Score: `{prediction:.4f}`")

    # Decision threshold at 0.5
    if prediction < 0.5:
        st.success("✅ It is **Fresh**")

    else:
        st.error("❌ It is **Rotten**")




