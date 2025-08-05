import os
import shutil

# Step 1: Set path to your dataset folder
BASE_DIR = r'C:\Users\pooji\Downloads\smart_sorting_complete_package\dataset'

# Step 2: Map all original folders to 'fresh' or 'rotten'
LABEL_MAP = {
    'freshapple': 'fresh',
    'freshbanana': 'fresh',
    'freshorange': 'fresh',
    'rottenapple': 'rotten',
    'rottenbanana': 'rotten',
    'rottenorange': 'rotten'
}

# Step 3: Move images into correct folders
for split in ['train', 'test']:
    source_path = os.path.join(BASE_DIR, split)
    target_path = os.path.join(BASE_DIR, split + '_fixed')
    os.makedirs(target_path, exist_ok=True)

    for label in ['fresh', 'rotten']:
        os.makedirs(os.path.join(target_path, label), exist_ok=True)

    for folder in os.listdir(source_path):
        full_folder_path = os.path.join(source_path, folder)
        if not os.path.isdir(full_folder_path):
            continue
        folder_lower = folder.lower()
        if folder_lower in LABEL_MAP:
            label = LABEL_MAP[folder_lower]
            for image in os.listdir(full_folder_path):
                src_img = os.path.join(full_folder_path, image)
                dst_img = os.path.join(target_path, label, image)
                shutil.move(src_img, dst_img)
        else:
            print(f"Skipping unknown folder: {folder}")

print("✅ Dataset reorganized. Use 'train_fixed' and 'test_fixed' folders.")
