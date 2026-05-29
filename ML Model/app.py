import pickle
from flask import Flask, request, render_template

app = Flask(__name__)

# Load the pre-trained house price prediction model from a pickle file
with open('houseprice_model1.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the input from the form
    sqft_living = float(request.form.get('sqft_living'))
    sqft_lot = float(request.form.get('sqft_lot'))

    # Prepare the data for prediction
    input_data = [[sqft_living, sqft_lot]]

    # Make a prediction
    prediction = model.predict(input_data)[0]

    # Render the result.html with the prediction
    return render_template('result.html', predicted_price=f"The predicted house price is: ${prediction:.2f}")

if __name__ == '__main__':
    app.run(debug=True)
00