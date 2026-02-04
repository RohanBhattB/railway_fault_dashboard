# 🚆 Railway Track Health Monitoring System  
### An ML-Driven Fault Detection & Maintenance Dashboard

---

## 🔍 Problem Statement
Railway track faults such as **misalignment, bearing defects, and unbalance** are difficult to detect at early stages and can lead to serious safety risks if ignored.  
Conventional inspection methods are largely manual, time-consuming, and reactive.

This project proposes a **machine-learning-based monitoring system** that analyzes vibration sensor data to detect fault patterns and present **actionable safety insights** through an interactive dashboard.

---

## 💡 Project Overview
The system uses vibration feature data collected from railway tracks to:

1. Train a **Random Forest classifier** for fault detection  
2. Classify vibration patterns into fault categories  
3. Map fault categories into **railway safety conditions**  
4. Display results using an interactive **Streamlit dashboard**  
5. Support maintenance decision-making through alerts and tracking  

The focus of this project is **decision support**, not just prediction.

---

## 🧠 Machine Learning Approach
- **Algorithm Used:** Random Forest Classifier  
- **Reason for Selection:**  
  - Handles noisy sensor data effectively  
  - Performs well for multi-class classification  
  - Robust and interpretable for engineering problems  

### Fault to Condition Mapping
| ML Output Label | Track Condition | Meaning |
|----------------|----------------|---------|
| `normal_like` | 🟢 Good | Track operating normally |
| `misalignment_like` | 🟡 OK | Minor issue, monitoring required |
| `bearing_like` | 🔴 Dangerous | High risk, immediate action |
| `unbalance_like` | 🔴 Dangerous | Unsafe operating condition |

This mapping converts technical ML output into **real-world operational severity**.

---

## 📊 Dashboard Features
The web dashboard provides:

- **Health Overview**
  - Pie chart showing percentage of track conditions  
  - Bar chart showing count of Good / OK / Dangerous segments  

- **Emergency Alert Panel**
  - Displays unresolved dangerous track segments  
  - Sorted by severity and time  
  - Clickable alerts for detailed inspection  

- **Maintenance Workflow**
  - Mark maintenance as completed  
  - Automatically removes resolved alerts  
  - Session-based state management  

- **Reporting**
  - Download active emergency alerts as a CSV file  

---

## 🛠️ Technology Stack
- **Language:** Python  
- **Machine Learning:** scikit-learn  
- **Data Processing:** pandas, numpy  
- **Visualization:** Plotly  
- **Dashboard Framework:** Streamlit  
- **Deployment:** Streamlit Community Cloud  

---

## 📁 Project Structure
railway_fault_dashboard/
│
├── app.py # Streamlit dashboard
├── model.py # ML training and prediction logic
├── vibration_fault_classification_random_forest.csv
├── requirements.txt
└── README.md



---

## ▶️ How to Run the Project Locally
```bash
pip install -r requirements.txt
streamlit run app.py

http://localhost:8501
