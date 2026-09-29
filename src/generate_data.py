import pandas as pd
import numpy as np

# Reproducible random data
np.random.seed(42)

# Number of transportation records
NUM_RECORDS = 5000

# -----------------------------
# Transportation categories
# -----------------------------

routes = [
    "Guntur-Hyderabad",
    "Guntur-Vijayawada",
    "Hyderabad-Warangal",
    "Vijayawada-Hyderabad",
    "Guntur-Tenali",
    "Hyderabad-Nalgonda",
    "Vijayawada-Guntur",
    "Guntur-Chennai"
]

vehicle_types = [
    "Non-AC Bus",
    "AC Bus",
    "Mini Bus",
    "Volvo Bus"
]

payment_methods = [
    "Cash",
    "UPI",
    "Card",
    "Online"
]

customer_types = [
    "Regular",
    "Student",
    "Corporate",
    "Senior Citizen"
]

status_types = [
    "Completed",
    "Cancelled",
    "Delayed"
]

# -----------------------------
# Create dataset
# -----------------------------

df = pd.DataFrame({

    "Trip_ID": [
        f"T{str(i).zfill(5)}"
        for i in range(1, NUM_RECORDS + 1)
    ],

    "Date": pd.date_range(
        start="2026-01-01",
        periods=NUM_RECORDS,
        freq="h"
    ),

    "Route": np.random.choice(
        routes,
        size=NUM_RECORDS
    ),

    "Vehicle_Type": np.random.choice(
        vehicle_types,
        size=NUM_RECORDS
    ),

    "Passengers": np.random.randint(
        10,
        60,
        size=NUM_RECORDS
    ),

    "Vehicle_Capacity": np.random.choice(
        [40, 50, 60],
        size=NUM_RECORDS
    ),

    "Distance_km": np.random.randint(
        20,
        400,
        size=NUM_RECORDS
    ),

    "Duration_min": np.random.randint(
        30,
        500,
        size=NUM_RECORDS
    ),

    "Delay_min": np.random.randint(
        0,
        60,
        size=NUM_RECORDS
    ),

    "Fare": np.random.randint(
        100,
        1000,
        size=NUM_RECORDS
    ),

    "Fuel_Cost": np.random.randint(
        500,
        5000,
        size=NUM_RECORDS
    ),

    "Maintenance_Cost": np.random.randint(
        100,
        2000,
        size=NUM_RECORDS
    ),

    "Status": np.random.choice(
        status_types,
        size=NUM_RECORDS,
        p=[0.85, 0.05, 0.10]
    ),

    "Payment_Method": np.random.choice(
        payment_methods,
        size=NUM_RECORDS
    ),

    "Customer_Type": np.random.choice(
        customer_types,
        size=NUM_RECORDS
    )
})

# -----------------------------
# Save dataset
# -----------------------------

df.to_csv(
    "data/transportation_data.csv",
    index=False
)

# -----------------------------
# Display information
# -----------------------------

print("=" * 50)
print("TRANSPORTATION DATASET CREATED")
print("=" * 50)

print("\nNumber of records:", len(df))
print("Number of columns:", len(df.columns))

print("\nFirst 5 records:")
print(df.head())

print("\nDataset columns:")
print(df.columns.tolist())

print("\nDataset saved to:")
print("data/transportation_data.csv")