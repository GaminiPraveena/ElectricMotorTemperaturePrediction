👩‍💻 Author
Praveena Gamini
B.Tech – Computer Science and Engineering
Machine Learning & AI Enthusiast

Live Server Link:https://electricmotortemperatureprediction.onrender.com/

Electric Motor Temperature Prediction

A Machine Learning + Flask web application that predicts the Permanent Magnet (PM) temperature of an electric motor based on sensor input parameters.
This system helps in monitoring motor health, preventing overheating, and avoiding potential motor failures.

--Project Overview

Electric motors are widely used in industries and electric vehicles. Overheating of the Permanent Magnet (PM) can cause efficiency loss and damage.

This project:

Takes real-time input parameters

Uses a trained ML model to predict PM temperature

Classifies the motor condition (Normal / High / Critical)

Displays results via a Flask web interface

--Features

✅ Machine Learning temperature prediction

✅ Flask-based web application

✅ Overheating alert system

✅ User-friendly interface

✅ Threshold-based safety warnings
--Technologies Used

Python
Pandas
NumPy
Scikit-learn
Flask
HTML / CSS
Joblib (for model saving)

Output Classification

Based on predicted PM temperature:

Temperature Range	Status
< 55°C	✅ Normal Temperature
55–75°C	⚠ High Temperature – Monitor Closely
> 75°C	🔥 Critical Temperature (Near Maximum Limit)

Installation & Setup
1) Clone the Repository
git clone https://github.com/your-username/ElectricMotorTemperaturePrediction.git
cd ElectricMotorTemperaturePrediction

2️) Create Virtual Environment (Optional but Recommended)
python -m venv venv
venv\Scripts\activate  

3️) Install Dependencies
pip install -r requirements.txt

4️) Run the Application
python app.py

5️) Open in Browser
http://127.0.0.1:5000/


