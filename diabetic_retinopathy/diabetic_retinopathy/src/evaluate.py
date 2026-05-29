"""
evaluate.py
-----------
Evaluates trained DR model on test set.
Outputs: accuracy, classification report, confusion matrix, ROC curves.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import tensorflow as tf
from pathlib import Path
from sklearn.metrics import (
    classification_report, confusion_matrix,
    roc_curve, auc
)
from sklearn.preprocessing import label_binarize
from tensorflow.keras.preprocessing.image import ImageDataGenerator

IMG_SIZE    = 224
BATCH_SIZE  = 32
NUM_CLASSES = 5
CLASS_NAMES = ["No DR", "Mild", "Moderate", "Severe", "Proliferative DR"]

DATA_DIR    = Path("data/processed")
MODELS_DIR  = Path("models")
RESULTS_DIR = Path("results")
RESULTS_DIR.mkdir(exist_ok=True)

def load_model_and_data():
    model = tf.keras.models.load_model(str(MODELS_DIR / "final_model.keras"))

    test_datagen = ImageDataGenerator()
    test_gen = test_datagen.flow_from_directory(
        DATA_DIR / "test",
        target_size=(IMG_SIZE, IMG_SIZE),
        batch_size=BATCH_SIZE,
        class_mode="sparse",
        shuffle=False,
    )
    return model, test_gen

def plot_confusion_matrix(y_true, y_pred):
    cm = confusion_matrix(y_true, y_pred)
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues",
                xticklabels=CLASS_NAMES, yticklabels=CLASS_NAMES)
    plt.title("Confusion Matrix — DR Detection", fontsize=14)
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.tight_layout()
    plt.savefig(RESULTS_DIR / "confusion_matrix.png", dpi=150)
    print("📊 Saved: results/confusion_matrix.png")

def plot_roc_curves(y_true, y_prob):
    y_bin = label_binarize(y_true, classes=list(range(NUM_CLASSES)))
    plt.figure(figsize=(9, 6))
    for i, cls_name in enumerate(CLASS_NAMES):
        fpr, tpr, _ = roc_curve(y_bin[:, i], y_prob[:, i])
        roc_auc = auc(fpr, tpr)
        plt.plot(fpr, tpr, label=f"{cls_name} (AUC = {roc_auc:.2f})")
    plt.plot([0, 1], [0, 1], "k--")
    plt.title("ROC Curves per DR Grade")
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.legend(loc="lower right")
    plt.tight_layout()
    plt.savefig(RESULTS_DIR / "roc_curves.png", dpi=150)
    print("📊 Saved: results/roc_curves.png")

def main():
    print("🔍 Loading model and test data...")
    model, test_gen = load_model_and_data()

    print("⚙️  Running predictions...")
    y_prob = model.predict(test_gen, verbose=1)
    y_pred = np.argmax(y_prob, axis=1)
    y_true = test_gen.classes

    # ── Metrics ───────────────────────────────────────────────────────
    report = classification_report(y_true, y_pred, target_names=CLASS_NAMES)
    print("\n📋 Classification Report:\n")
    print(report)

    report_df = pd.DataFrame(
        classification_report(y_true, y_pred, target_names=CLASS_NAMES, output_dict=True)
    ).T
    report_df.to_csv(RESULTS_DIR / "classification_report.csv")

    plot_confusion_matrix(y_true, y_pred)
    plot_roc_curves(y_true, y_prob)

    acc = np.mean(y_true == y_pred)
    print(f"\n✅ Test Accuracy: {acc * 100:.2f}%")

if __name__ == "__main__":
    main()
