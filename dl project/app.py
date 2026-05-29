from flask import Flask, render_template, request
import numpy as np
import tensorflow as tf
import joblib
import os

# -----------------------------
# Load Saved Model & Tools
# -----------------------------
model = tf.keras.models.load_model("best_model.keras")
scaler = joblib.load("scaler.save")
label_encoder = joblib.load("label_encoder.pkl")

# Flask App
app = Flask(__name__)

# Folder for uploaded images
UPLOAD_FOLDER = "static/uploads"
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# -----------------------------
# Routes
# -----------------------------
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get numeric form inputs
        features = [
            float(request.form["PM2.5"]),
            float(request.form["PM10"]),
            float(request.form["NO2"]),
            float(request.form["SO2"]),
            float(request.form["CO"]),
            float(request.form["O3"]),
            float(request.form["Temperature"]),
            float(request.form["Humidity"]),
            float(request.form["Wind_Speed"])
        ]

        # Handle uploaded image (optional)
        image_file = request.files["image_file"]
        image_path = None
        if image_file and image_file.filename != "":
            image_path = os.path.join(app.config["UPLOAD_FOLDER"], image_file.filename)
            image_file.save(image_path)

        # Scale input features
        features_scaled = scaler.transform([features])

        # Predict AQI category
        prediction = model.predict(features_scaled)
        pred_class = np.argmax(prediction, axis=1)[0]
        final_result = label_encoder.inverse_transform([pred_class])[0]

        # Return result with optional image
        return render_template(
            "index.html",
            prediction_text=f"Predicted AQI Category: {final_result}",
            image_path=image_path
        )

    except Exception as e:
        return render_template("index.html", prediction_text=f"Error: {str(e)}")


if __name__ == "__main__":
    app.run(debug=True)
