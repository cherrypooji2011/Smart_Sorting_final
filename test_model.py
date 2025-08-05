from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np

model = load_model("rotten_fruit_classifier.h5")

img_path = "banana_rotten.png"  # change this
img = image.load_img(img_path, target_size=(224, 224))
img_array = image.img_to_array(img) / 255.0
img_array = np.expand_dims(img_array, axis=0)

prediction = model.predict(img_array)[0][0]
print("🧠 Raw prediction score:", prediction)

if prediction < 0.5:
    print("❌ Prediction: Rotten")
else:
    print("✅ Prediction: Fresh")
