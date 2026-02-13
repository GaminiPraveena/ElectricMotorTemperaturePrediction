from flask import Flask, render_template, request
import numpy as np
import joblib
import os
import gdown

app = Flask(__name__)

# -------------------------
# Download model if missing
# -------------------------

MODEL_PATH = "model.save"
SCALER_PATH = "transform.save"

MODEL_URL = "https://drive.google.com/uc?id=1tTQB5h_T6W3-2_6LHdZwmCm2_K2unb6p
"
SCALER_URL = "https://drive.google.com/uc?id=1jk91aKAOj5gAWPho8g4AUySwlojzocz0"

if not os.path.exists(MODEL_PATH):
    gdown.download(MODEL_URL, MODEL_PATH, quiet=False)

if not os.path.exists(SCALER_PATH):
    gdown.download(SCALER_URL, SCALER_PATH, quiet=False)

# Load saved model and scaler
model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    try:
        ambient = float(request.form['ambient'])
        coolant = float(request.form['coolant'])
        u_d = float(request.form['u_d'])
        u_q = float(request.form['u_q'])
        motor_speed = float(request.form['motor_speed'])
        i_d = float(request.form['i_d'])
        i_q = float(request.form['i_q'])

        user_input = np.array([[ambient, coolant, u_d, u_q,
                                motor_speed, i_d, i_q]])

        user_input_scaled = scaler.transform(user_input)
        prediction = model.predict(user_input_scaled)[0]

        if prediction < 40:
            status = "✅ Normal Temperature"
        elif 40 <= prediction < 60:
            status = "⚠ High Temperature - Monitor Closely"
        else:
            status = "🔥 Critical Temperature (Near Maximum Limit)"

        return render_template('index.html',
                               prediction_text=f"Predicted PM Temperature: {round(prediction, 2)} °C",
                               status=status)

    except:
        return render_template('index.html',
                               prediction_text="Invalid Input! Please enter valid numbers.")


if __name__ == "__main__":
    app.run(debug=False)
