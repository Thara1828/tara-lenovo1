"""
model.py
--------
EfficientNetB3-based CNN for 5-class DR grading.
Includes transfer learning setup + custom classifier head.
"""

import tensorflow as tf
from tensorflow.keras import layers, Model
from tensorflow.keras.applications import EfficientNetB3

IMG_SIZE   = 224
NUM_CLASSES = 5

def build_model(num_classes: int = NUM_CLASSES, freeze_base: bool = True) -> Model:
    """
    Build EfficientNetB3 model with custom classification head.
    
    Args:
        num_classes:  Number of DR severity classes (5 for IDRiD).
        freeze_base:  Freeze backbone weights initially for feature extraction.
    
    Returns:
        Compiled Keras model.
    """
    inputs = layers.Input(shape=(IMG_SIZE, IMG_SIZE, 3))

    # Normalize to [0,1] inside the model
    x = layers.Rescaling(1.0 / 255)(inputs)

    # EfficientNetB3 backbone
    base = EfficientNetB3(
        include_top=False,
        weights="imagenet",
        input_tensor=x,
    )
    base.trainable = not freeze_base

    # Custom head
    x = base.output
    x = layers.GlobalAveragePooling2D()(x)
    x = layers.BatchNormalization()(x)
    x = layers.Dense(256, activation="relu")(x)
    x = layers.Dropout(0.4)(x)
    x = layers.Dense(128, activation="relu")(x)
    x = layers.Dropout(0.3)(x)
    outputs = layers.Dense(num_classes, activation="softmax")(x)

    model = Model(inputs=base.input, outputs=outputs)

    model.compile(
        optimizer=tf.keras.optimizers.Adam(learning_rate=1e-4),
        loss="sparse_categorical_crossentropy",
        metrics=[
            "accuracy",
            tf.keras.metrics.SparseTopKCategoricalAccuracy(k=2, name="top2_acc"),
        ],
    )
    return model


def unfreeze_top_layers(model: Model, num_layers: int = 30) -> Model:
    """
    Unfreeze the top N layers of the backbone for fine-tuning.
    Call after initial training with frozen base.
    """
    base = model.layers[2]  # EfficientNetB3 is the 3rd layer
    base.trainable = True
    for layer in base.layers[:-num_layers]:
        layer.trainable = False

    model.compile(
        optimizer=tf.keras.optimizers.Adam(learning_rate=1e-5),
        loss="sparse_categorical_crossentropy",
        metrics=[
            "accuracy",
            tf.keras.metrics.SparseTopKCategoricalAccuracy(k=2, name="top2_acc"),
        ],
    )
    print(f"🔓 Unfroze top {num_layers} layers of backbone for fine-tuning.")
    return model


if __name__ == "__main__":
    model = build_model()
    model.summary()
