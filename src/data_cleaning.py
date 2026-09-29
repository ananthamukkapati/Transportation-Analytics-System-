import pandas as pd
import numpy as np

# ==========================================
# 1. LOAD DATASET
# ==========================================

df = pd.read_csv(
    "data/transportation_data.csv"
)

print("=" * 60)
print("TRANSPORTATION DATA CLEANING")
print("=" * 60)

print("\nFirst 5 rows:")
print(df.head())

print("\nOriginal shape:")
print(df.shape)

# ==========================================
# 2. DATA TYPES
# ==========================================

print("\nOriginal data types:")
print(df.dtypes)

# Convert Date
df["Date"] = pd.to_datetime(df["Date"])

# ==========================================
# 3. MISSING VALUES
# ==========================================

print("\nMissing values:")
print(df.isnull().sum())

# ==========================================
# 4. DUPLICATES
# ==========================================

duplicate_count = df.duplicated().sum()

print(
    "\nDuplicate rows:",
    duplicate_count
)

df = df.drop_duplicates()

# ==========================================
# 5. VALIDATION
# ==========================================

invalid_passengers = df[
    df["Passengers"] <= 0
]

invalid_distance = df[
    df["Distance_km"] <= 0
]

invalid_fare = df[
    df["Fare"] <= 0
]

print(
    "\nInvalid passenger records:",
    len(invalid_passengers)
)

print(
    "Invalid distance records:",
    len(invalid_distance)
)

print(
    "Invalid fare records:",
    len(invalid_fare)
)

# ==========================================
# 6. CALCULATED COLUMNS
# ==========================================

# Revenue
df["Revenue"] = (
    df["Passengers"] *
    df["Fare"]
)

# Total Cost
df["Total_Cost"] = (
    df["Fuel_Cost"] +
    df["Maintenance_Cost"]
)

# Profit
df["Profit"] = (
    df["Revenue"] -
    df["Total_Cost"]
)

# Vehicle utilization
df["Utilization_Percentage"] = (
    df["Passengers"] /
    df["Vehicle_Capacity"]
) * 100

# ==========================================
# 7. DATE FEATURES
# ==========================================

df["Year"] = df["Date"].dt.year

df["Month"] = df["Date"].dt.month

df["Month_Name"] = (
    df["Date"].dt.strftime("%B")
)

df["Day"] = df["Date"].dt.day

df["Day_Name"] = (
    df["Date"].dt.strftime("%A")
)

df["Hour"] = df["Date"].dt.hour

# ==========================================
# 8. FINAL INFORMATION
# ==========================================

print("\nFinal shape:")
print(df.shape)

print("\nFinal columns:")
print(df.columns.tolist())

print("\nSample cleaned data:")
print(df.head())

# ==========================================
# 9. SAVE CLEAN DATASET
# ==========================================

df.to_csv(
    "data/processed/cleaned_transportation_data.csv",
    index=False
)

print(
    "\nCleaned dataset saved successfully!"
)

print(
    "\nFile:"
)

print(
    "data/processed/cleaned_transportation_data.csv"
)