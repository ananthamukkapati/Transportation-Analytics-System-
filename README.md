# 🚍 Transportation Analytics System

An end-to-end transportation analytics and predictive analytics project built using **Python, Pandas, NumPy, Scikit-learn, and Power BI**.

The project analyzes transportation trips, passenger demand, route performance, revenue, costs, profitability, vehicle utilization, delays, customer segments, and predicted passenger demand.

---

## 📌 Project Overview

Transportation companies generate large amounts of operational data from trips, routes, vehicles, passengers, payments, revenue, and costs.

This project transforms transportation data into:

* Business KPIs
* Route performance analysis
* Vehicle utilization analysis
* Customer and payment analysis
* Demand analysis
* Interactive Power BI dashboards
* Passenger-demand predictions

---

## 🎯 Objectives

* Analyze transportation trip performance
* Identify revenue and profitability patterns
* Analyze passenger demand
* Evaluate vehicle utilization
* Monitor delays and cancellations
* Analyze customer segments
* Build an interactive Power BI dashboard
* Predict passenger demand using machine learning
* Identify high-demand transportation segments

---

## 🛠️ Technologies Used

### Programming & Analytics

* Python
* Pandas
* NumPy

### Machine Learning

* Scikit-learn
* Random Forest Regression

### Visualization & BI

* Power BI
* DAX
* Matplotlib

### Development

* VS Code
* Git
* GitHub

---

## 📊 Project Workflow

```text
Raw Transportation Data
        ↓
Data Cleaning
        ↓
Feature Engineering
        ↓
Exploratory Data Analysis
        ↓
KPI Analysis
        ↓
Power BI Dashboard
        ↓
Machine Learning
        ↓
Demand Prediction
        ↓
Business Insights
```

---

## 📈 Key KPIs

The dashboard tracks:

* Total Trips
* Total Passengers
* Total Revenue
* Total Cost
* Total Profit
* Profit Margin
* Average Fare
* Average Delay
* Average Utilization
* Completion Rate
* Delay Rate
* Cancellation Rate
* Revenue per Passenger
* Profit per Trip
* Passenger Load Factor

---

## 🤖 Machine Learning

A Random Forest Regression model was developed to estimate passenger demand.

### Features

* Vehicle Capacity
* Distance
* Trip Duration
* Delay
* Fare
* Hour
* Day of Week
* Month

### Target

```text
Passengers
```

### Evaluation Metrics

* MAE
* RMSE
* R² Score

The model's feature importance was also analyzed to understand which variables contributed most to its predictions.

---

## 📊 Power BI Dashboard

The Power BI report contains:

### Executive Overview

Provides a high-level view of transportation performance using KPI cards and trend charts.

### Route Performance

Analyzes:

* Revenue
* Cost
* Profit
* Delays
* Predicted passenger demand

### Vehicle & Operations

Analyzes:

* Vehicle utilization
* Revenue
* Costs
* Profit
* Operational delays

### Customer & Demand

Analyzes:

* Customer types
* Payment methods
* Passenger demand
* Peak hours
* Actual vs predicted demand

### Route Details

Provides drill-through analysis for individual routes.

---

## 🔎 Business Insights

The project enables analysis of:

* High-revenue routes
* Route-level profitability
* Vehicle utilization
* Operational delays
* Customer demand patterns
* Payment-method usage
* Peak-demand periods
* Predicted passenger demand

---

## 📁 Project Structure

```text
Transportation-Analytics-System/
│
├── data/
├── src/
├── powerbi/
├── screenshots/
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
```

### 2. Navigate to the project

```bash
cd Transportation-Analytics-System
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the environment

Windows:

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run data generation

```bash
python src/generate_data.py
```

### 7. Run data cleaning

```bash
python src/data_cleaning.py
```

### 8. Run KPI analysis

```bash
python src/kpi_calculation.py
```

### 9. Run demand prediction

```bash
python src/demand_prediction.py
```

---

## 📌 Note

The transportation dataset used in this project is synthetic and was created for educational and portfolio purposes. The analysis demonstrates an end-to-end analytics workflow rather than reporting real transportation-company performance.

---

## 👨‍💻 Author

**Anantha Mukkapati**

B.Tech — Computer Science and Engineering

Interested in Data Analytics, Software Engineering, Backend Development, and AI.
