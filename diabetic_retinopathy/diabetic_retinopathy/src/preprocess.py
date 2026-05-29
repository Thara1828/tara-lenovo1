"""
preprocess.py
-------------
Preprocesses IDRiD retinal fundus images:
- Resizes to 224x224
- Applies CLAHE (contrast enhancement)
- Saves to processed/ folder with train/val/test split
"""

import os
import cv2
import numpy as np
import pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split
from tqdm import tqdm

# ── Paths ──────────────────────────────────────────────────────────────
RAW_DIR       = Path("data/raw")
PROCESSED_DIR = Path("data/processed")
LABEL_CSV     = RAW_DIR / "labels.csv"   # columns: image_name, grade
IMG_SIZE      = 224

SPLITS = ["train", "val", "test"]
CLASSES = [0, 1, 2, 3, 4]

# ── CLAHE Enhancement ─────────────────────────────────────────────────
def apply_clahe(img: np.ndarray) -> np.ndarray:
    """Apply CLAHE to the green channel (best contrast for retinal vessels)."""
    lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    l = clahe.apply(l)
    lab = cv2.merge([l, a, b])
    return cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)

def crop_and_resize(img: np.ndarray, size: int = IMG_SIZE) -> np.ndarray:
    """Remove black borders and resize."""
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 10, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if contours:
        x, y, w, h = cv2.boundingRect(max(contours, key=cv2.contourArea))
        img = img[y:y+h, x:x+w]
    return cv2.resize(img, (size, size))

def preprocess_image(img_path: Path) -> np.ndarray:
    img = cv2.imread(str(img_path))
    if img is None:
        raise FileNotFoundError(f"Cannot read: {img_path}")
    img = crop_and_resize(img)
    img = apply_clahe(img)
    return img

# ── Dataset Split ─────────────────────────────────────────────────────
def build_splits(df: pd.DataFrame):
    train_df, temp_df = train_test_split(df, test_size=0.3, stratify=df["grade"], random_state=42)
    val_df, test_df  = train_test_split(temp_df, test_size=0.5, stratify=temp_df["grade"], random_state=42)
    return {"train": train_df, "val": val_df, "test": test_df}

# ── Main ──────────────────────────────────────────────────────────────
def main():
    df = pd.read_csv(LABEL_CSV)
    splits = build_splits(df)

    for split, split_df in splits.items():
        for grade in CLASSES:
            (PROCESSED_DIR / split / str(grade)).mkdir(parents=True, exist_ok=True)

        print(f"\n🔄 Processing {split} set ({len(split_df)} images)...")
        for _, row in tqdm(split_df.iterrows(), total=len(split_df)):
            img_path = RAW_DIR / f"{row['image_name']}.jpg"
            out_path = PROCESSED_DIR / split / str(row["grade"]) / f"{row['image_name']}.jpg"
            try:
                img = preprocess_image(img_path)
                cv2.imwrite(str(out_path), img)
            except Exception as e:
                print(f"  ⚠️  Skipping {img_path.name}: {e}")

    print("\n✅ Preprocessing complete.")
    for split, split_df in splits.items():
        print(f"   {split:5s}: {len(split_df)} images")

if __name__ == "__main__":
    main()
