"""
train.py
--------
Full training pipeline for Diabetic Retinopathy CNN.
Phase 1: Feature extraction (frozen base)
Phase 2: Fine-tuning (top layers unfrozen)
"""

import os
import numpy as np
import tensorflow as tf
from pathlib import Path
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.callbacks import (
    ModelCheckpoint, EarlyStopping, ReduceLROnPlateau, CSVLogger
)

from model import build_model, unfreeze_top_layers

# ── Config ────────────────────────────────────────────────────────────
IMG_SIZE     = 224
BATCH_SIZE   = 32
PHASE1_EPOCHS = 20
PHASE2_EPOCHS = 30
NUM_CLASSES  = 5

DATA_DIR    = Path("data/processed")
MODELS_DIR  = Path("models")
RESULTS_DIR = Path("results")
MODELS_DIR.mkdir(exist_ok=True)
RESULTS_DIR.mkdir(exist_ok=True)

# ── Data Generators ───────────────────────────────────────────────────
def get_generators():
    train_datagen = ImageDataGenerator(
        rotation_range=20,
        zoom_range=0.15,
        width_shift_range=0.1,
        height_shift_range=0.1,
        horizontal_flip=True,
        vertical_flip=True,
        brightness_range=[0.8, 1.2],
        fill_mode="nearest",
    )
    val_datagen = ImageDataGenerator()  # No augmentation for val/test

    train_gen = train_datagen.flow_from_directory(
        DATA_DIR / "train",
        target_size=(IMG_SIZE, IMG_SIZE),
        batch_size=BATCH_SIZE,
        class_mode="sparse",
        shuffle=True,
        seed=42,
    )
    val_gen = val_datagen.flow_from_directory(
        DATA_DIR / "val",
        target_size=(IMG_SIZE, IMG_SIZE),
        batch_size=BATCH_SIZE,
        class_mode="sparse",
        shuffle=False,
    )
    return train_gen, val_gen

# ── Class Weights (handle imbalance) ─────────────────────────────────
def compute_class_weights(train_gen) -> dict:
    from sklearn.utils.class_weight import compute_class_weight
    labels = train_gen.classes
    weights = compute_class_weight("balanced", classes=np.unique(labels), y=labels)
    return dict(enumerate(weights))

# ── Callbacks ─────────────────────────────────────────────────────────
def get_callbacks(phase: int):
    return [
        ModelCheckpoint(
            str(MODELS_DIR / f"best_model_phase{phase}.keras"),
            monitor="val_accuracy",
            save_best_only=True,
            verbose=1,
        ),
        EarlyStopping(monitor="val_loss", patience=7, restore_best_weights=True, verbose=1),
        ReduceLROnPlateau(monitor="val_loss", factor=0.5, patience=3, min_lr=1e-7, verbose=1),
        CSVLogger(str(RESULTS_DIR / f"training_log_phase{phase}.csv")),
    ]

# ── Training ──────────────────────────────────────────────────────────
def main():
    print("🔧 Building model...")
    model = build_model(num_classes=NUM_CLASSES, freeze_base=True)
    model.summary()

    print("\n📦 Loading datasets...")
    train_gen, val_gen = get_generators()
    class_weights = compute_class_weights(train_gen)
    print(f"   Class weights: {class_weights}")

    # ── Phase 1: Feature Extraction ──────────────────────────────────
    print("\n🚀 Phase 1: Training classifier head (frozen backbone)...")
    history1 = model.fit(
        train_gen,
        epochs=PHASE1_EPOCHS,
        validation_data=val_gen,
        class_weight=class_weights,
        callbacks=get_callbacks(1),
    )

    # ── Phase 2: Fine-Tuning ──────────────────────────────────────────
    print("\n🔓 Phase 2: Fine-tuning top layers...")
    model = unfreeze_top_layers(model, num_layers=30)
    history2 = model.fit(
        train_gen,
        epochs=PHASE2_EPOCHS,
        validation_data=val_gen,
        class_weight=class_weights,
        callbacks=get_callbacks(2),
    )

    model.save(str(MODELS_DIR / "final_model.keras"))
    print("\n✅ Training complete. Model saved to models/final_model.keras")

if __name__ == "__main__":
    main()
