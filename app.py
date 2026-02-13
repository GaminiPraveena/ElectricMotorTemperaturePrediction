from flask import Flask, render_template, request
import numpy as np
import joblib

app = Flask(__name__)

# Load saved model and scaler
model = joblib.load("model.save")
scaler = joblib.load("transform.save")

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

        # Prepare input
        user_input = np.array([[ambient, coolant, u_d, u_q, motor_speed, i_d, i_q]])
        user_input_scaled = scaler.transform(user_input)

        prediction = model.predict(user_input_scaled)[0]

        # Status condition
        if prediction < 40:
            status = "✅ Normal Temperature"
        elif 40 <= prediction < 60:
            status = "⚠ High Temperature - Monitor Closely"
        else:
            status = "🔥 Critical Temperature (Near Maximum Limit)"

        return render_template('index.html',
                               prediction_text=f"Predicted PM Temperature: {round(prediction,2)} °C",
                               status=status)

    except:
        return render_template('index.html',
                               prediction_text="Invalid Input! Please enter valid numbers.")

if __name__ == "__main__":
    app.run(debug=False)
