
# 🍎 Smart Sorting: Transfer Learning for Rotten Fruits/Vegetables Detection

## 🔍 Objective
Classify images of fruits/vegetables as **Fresh** or **Rotten** using MobileNetV2 and Transfer Learning.

## 📁 Folder Structure
```
smart_sorting/
├── dataset/
│   ├── train/
│   │   ├── fresh/
│   │   └── rotten/
│   └── test/
│       ├── fresh/
│       └── rotten/
├── smart_sorting.py
├── requirements.txt
└── README.md
```

## 📦 Dataset Setup (Manual Step Required)

1. Go to [Kaggle Dataset Page](https://www.kaggle.com/datasets/mdatikurrahman3111/fresh-and-rotten-classification-dataset-3)
2. Click “Download”
3. Unzip the dataset into the `dataset/` folder of this project with the structure shown above.
4. Ensure folders like `train/fresh`, `train/rotten`, `test/fresh`, `test/rotten` contain actual images.

## 🛠️ How to Run

1. Open Command Prompt and navigate to the project folder:
   ```
   cd path\to\smart_sorting_package
   ```

2. Install packages:
   ```
   pip install -r requirements.txt
   ```

3. Run the training:
   ```
   python smart_sorting.py
   ```

## 🧠 Output
- Trained model saved as `rotten_fruit_classifier.h5`
