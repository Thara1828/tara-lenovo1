"""
predict.py
----------
Single-image inference for Diabetic Retinopathy detection.
Usage: python src/predict.py --image path/to/fundus.jpg
"""

import argparse
import numpy as np
import cv2
import tensorflow as tf
from pathlib import Path

CLASS_NAMES = ["No DR", "Mild DR", "Moderate DR", "Severe DR", "Proliferative DR"]
IMG_SIZE    = 224
MODEL_PATH  = Path("models/final_model.keras")

def preprocess(img_path: str) -> np.ndarray:
    img = cv2.imread(img_path)
    img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return np.expand_dims(img, axis=0)  # (1, 224, 224, 3)

def predict(img_path: str):
    model = tf.keras.models.load_model(str(MODEL_PATH))
    img   = preprocess(img_path)
    probs = model.predict(img, verbose=0)[0]
    pred  = np.argmax(probs)

    print(f"\n🔬 Image: {img_path}")
    print(f"   Prediction  : {CLASS_NAMES[pred]} (Grade {pred})")
    print(f"   Confidence  : {probs[pred] * 100:.1f}%")
    print(f"\n   Class Probabilities:")
    for i, (cls, prob) in enumerate(zip(CLASS_NAMES, probs)):
        bar = "█" * int(prob * 30)
        marker = " ◄" if i == pred else ""
        print(f"   {cls:20s} {prob*100:5.1f}%  {bar}{marker}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="DR Prediction Inference")
    parser.add_argument("--image", required=True, help="Path to retinal fundus image")
    args = parser.parse_args()
    predict(args.image)
