from flask import Flask, render_template, request
import pickle
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

app = Flask(__name__)

# Load model + tokenizer
MODEL_PATH = "sms_rnn_model.h5"
TOKENIZER_PATH = "tokenizer.pkl"
MAXLEN = 100

model = load_model(MODEL_PATH)
with open(TOKENIZER_PATH, "rb") as f:
    tokenizer = pickle.load(f)

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    if request.method == "POST":
        sms = request.form["sms"]
        seq = tokenizer.texts_to_sequences([sms])
        X = pad_sequences(seq, maxlen=MAXLEN, padding="post")
        prob = model.predict(X)[0][0]
        prediction = "Spam" if prob > 0.5 else "Ham"
        return render_template("index.html", sms=sms, prob=prob, prediction=prediction)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
