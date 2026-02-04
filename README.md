🚆 Railway Track Health Monitoring Dashboard using Machine Learning
📌 Overview

This project is a Machine Learning–based Railway Track Health Monitoring System that analyzes vibration sensor data to detect faults in railway tracks and presents the results through an interactive web dashboard.

The system classifies vibration signals using a Random Forest model, maps detected faults into operational severity levels, and provides real-time visual insights and emergency alerts to support railway maintenance decision-making.

🎯 Objectives

Detect railway track faults using vibration sensor data

Classify faults using a supervised ML model

Convert technical fault outputs into actionable safety conditions

Visualize track health using an interactive dashboard

Highlight emergency conditions and maintenance actions

🧠 Machine Learning Approach

Algorithm Used: Random Forest Classifier

Why Random Forest?

Handles non-linear data well

Robust to noise

Suitable for multi-class fault classification

Fault Labels → Safety Conditions
Predicted Fault Label	Track Condition	Severity
normal_like	🟢 Good	Safe
misalignment_like	🟡 OK	Needs monitoring
bearing_like	🔴 Dangerous	Immediate action
unbalance_like	🔴 Dangerous	Immediate action
📊 Dashboard Features

📈 Pie Chart – Distribution of track conditions

📊 Bar Chart – Count of Good / OK / Dangerous tracks

🚨 Emergency Alerts Panel

Sorted by severity and time

Clickable alerts for detailed inspection

✅ Maintenance Completion Tracking

Mark emergencies as resolved

Automatically removes resolved alerts

⬇️ Download Emergency Alerts

Export unresolved emergencies as CSV

📋 Detailed Data Table

Full prediction and analysis view

🛠️ Tech Stack

Programming Language: Python

Machine Learning: scikit-learn

Data Handling: pandas, numpy

Visualization: Plotly

Web Framework: Streamlit

Deployment: Streamlit Community Cloud

📁 Project Structure
railway_fault_dashboard/
│
├── app.py        # Streamlit dashboard
├── model.py      # ML model and prediction logic
├── vibration_fault_classification_random_forest.csv
├── requirements.txt
└── README.md

▶️ How to Run Locally
1️⃣ Clone the repository
git clone https://github.com/your-username/railway-track-health-dashboard.git
cd railway-track-health-dashboard

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Run the application
streamlit run app.py


The app will open in your browser at:

http://localhost:8501

🌐 Live Deployment

The project is deployed for free on Streamlit Community Cloud.

🔗 Live Demo:
https://your-app-name.streamlit.app

🧪 Dataset

The dataset contains extracted vibration features from railway track sensors

Includes statistical and correlation-based features

Labels represent different mechanical fault patterns

🧠 Key Learning Outcomes

Applied machine learning to a real-world safety problem

Built an end-to-end ML pipeline (data → model → UI)

Learned Streamlit for rapid ML dashboard development

Implemented session-based state management

Understood fault severity mapping and decision systems

🚀 Future Scope

Integration with real-time IoT vibration sensors

Persistent storage for maintenance history (database)

SMS / Email alerts for critical conditions

GIS-based railway track visualization

Role-based login for operators and admins

👨‍🎓 Academic Use

This project is suitable for:

Final year engineering projects

Machine Learning mini-projects

Data Science & AI demonstrations

Smart transportation system studies
