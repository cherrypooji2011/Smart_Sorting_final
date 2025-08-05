import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image

# Load the model
model = load_model("rotten_fruit_classifier.h5")

st.set_page_config(page_title="🍎 Smart Sorting - Fruit Classifier")
st.title("🍏 Smart Sorting: Fresh vs Rotten")
st.markdown("Upload a fruit or vegetable image to check if it's **Fresh** or **Rotten**.")

uploaded_file = st.file_uploader("📤 Upload an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display the image
    img = Image.open(uploaded_file)
    st.image(img, caption="Uploaded Image", use_column_width=True)

    # Preprocess
    img = img.resize((224, 224))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    # Predict
    prediction = model.predict(img_array)[0][0]
    st.write("🧠 Prediction Score:", round(prediction, 4))

    # Display result
    if prediction < 1.5:
        st.error("❌ It is **Rotten**")
    else:
        st.success("✅ It is **Fresh**")
