import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)
import matplotlib.pyplot as plt


df = pd.read_csv(
    "data/processed/cleaned_transportation_data.csv"
)

df["Date"] = pd.to_datetime(df["Date"])

print("Dataset loaded successfully!")
print(df.shape)

import pandas as pd
import numpy as np

df = pd.read_csv(
    "data/processed/cleaned_transportation_data.csv"
)

df["Date"] = pd.to_datetime(df["Date"])

print("Dataset loaded successfully!")
print(df.shape)

df["Hour"] = df["Date"].dt.hour

df["DayOfWeek"] = df["Date"].dt.dayofweek

df["Month_Number"] = df["Date"].dt.month

features = [
    "Vehicle_Capacity",
    "Distance_km",
    "Duration_min",
    "Delay_min",
    "Fare",
    "Hour",
    "DayOfWeek",
    "Month_Number"
]
target = "Passengers"

X = df[features]

y = df[target]

print("Features:")
print(X.head())

print("\nTarget:")
print(y.head())

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)
model.fit(
    X_train,
    y_train
)

# make prediction
predictions = model.predict(X_test)

print("Actual values:")
print(y_test.head(10).values)

print("\nPredicted values:")
print(predictions[:10])

mae = mean_absolute_error(
    y_test,
    predictions
)

rmse = np.sqrt(
    mean_squared_error(
        y_test,
        predictions
    )
)

r2 = r2_score(
    y_test,
    predictions
)
print("\n========== MODEL PERFORMANCE ==========")

print(
    "MAE:",
    round(mae, 2)
)

print(
    "RMSE:",
    round(rmse, 2)
)

print(
    "R² Score:",
    round(r2, 2)
)

feature_importance = pd.DataFrame({
    "Feature": features,
    "Importance": model.feature_importances_
})
feature_importance = (
    feature_importance
    .sort_values(
        "Importance",
        ascending=False
    )
)
print("\n========== FEATURE IMPORTANCE ==========")

print(feature_importance)

plt.figure(figsize=(10, 6))

plt.barh(
    feature_importance["Feature"],
    feature_importance["Importance"]
)

plt.xlabel("Importance")
plt.ylabel("Feature")

plt.title(
    "Transportation Demand Prediction - Feature Importance"
)

plt.gca().invert_yaxis()

plt.tight_layout()

plt.show()

# generate predictions for all records
df["Predicted_Passengers"] = model.predict(
    df[features]
)

df["Predicted_Passengers"] = (
    df["Predicted_Passengers"]
    .round(0)
    .astype(int)
)

# Identity high-demand trips
high_demand_threshold = (
    df["Predicted_Passengers"]
    .quantile(0.75)
)
df["Demand_Category"] = np.where(
    df["Predicted_Passengers"]
    >= high_demand_threshold,
    "High Demand",
    "Normal Demand"
)
print(
    df["Demand_Category"]
    .value_counts()
)
# analyze predicted demand by route
predicted_route_demand = (
    df.groupby("Route")
    .agg({
        "Predicted_Passengers": "mean",
        "Passengers": "mean"
    })
    .sort_values(
        "Predicted_Passengers",
        ascending=False
    )
)
print(
    "\n========== PREDICTED DEMAND BY ROUTE =========="
)

print(predicted_route_demand)

#Export Ml results 
#create
df.to_csv(
    "data/processed/transportation_predictions.csv",
    index=False
)
feature_importance.to_csv(
    "data/processed/feature_importance.csv",
    index=False
)