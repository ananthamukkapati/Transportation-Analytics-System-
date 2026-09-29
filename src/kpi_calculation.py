import pandas as pd
import numpy as np

# Load cleaned dataset
df = pd.read_csv(
    "data/processed/cleaned_transportation_data.csv"
)

df["Date"] = pd.to_datetime(df["Date"])

print("Dataset loaded successfully!")
print("Rows:", len(df))
print("Columns:", len(df.columns))

# ==========================================
# MAIN BUSINESS KPIs
# ==========================================

total_trips = df["Trip_ID"].nunique()

total_passengers = df["Passengers"].sum()

total_revenue = df["Revenue"].sum()

total_cost = df["Total_Cost"].sum()

total_profit = df["Profit"].sum()

average_fare = df["Fare"].mean()

average_delay = df["Delay_min"].mean()

average_utilization = (
    df["Utilization_Percentage"].mean()
)

total_distance = df["Distance_km"].sum()

average_duration = df["Duration_min"].mean()

print("\n========== TRANSPORTATION KPIs ==========")

print("Total Trips:", total_trips)

print("Total Passengers:", total_passengers)

print(
    "Total Revenue:",
    round(total_revenue, 2)
)

print(
    "Total Cost:",
    round(total_cost, 2)
)

print(
    "Total Profit:",
    round(total_profit, 2)
)

print(
    "Average Fare:",
    round(average_fare, 2)
)

print(
    "Average Delay:",
    round(average_delay, 2),
    "minutes"
)

print(
    "Average Utilization:",
    round(average_utilization, 2),
    "%"
)

print(
    "Total Distance:",
    round(total_distance, 2),
    "km"
)

print(
    "Average Duration:",
    round(average_duration, 2),
    "minutes"
)

profit_margin = (
    total_profit /
    total_revenue
) * 100
print(
    "Profit Margin:",
    round(profit_margin, 2),
    "%"
)


vehicle_analysis = df.groupby(
    "Vehicle_Type"
).agg({
    "Trip_ID": "count",
    "Passengers": "sum",
    "Revenue": "sum",
    "Total_Cost": "sum",
    "Profit": "sum",
    "Utilization_Percentage": "mean",
    "Delay_min": "mean"
})
#rename
vehicle_analysis.columns = [
    "Total_Trips",
    "Total_Passengers",
    "Total_Revenue",
    "Total_Cost",
    "Total_Profit",
    "Average_Utilization",
    "Average_Delay"
]
print("\n========== VEHICLE PERFORMANCE ==========")

print(vehicle_analysis)

#route performance
route_analysis = df.groupby(
    "Route"
).agg({
    "Trip_ID": "count",
    "Passengers": "sum",
    "Revenue": "sum",
    "Total_Cost": "sum",
    "Profit": "sum",
    "Delay_min": "mean",
    "Utilization_Percentage": "mean"
})
#rename
route_analysis.columns = [
    "Total_Trips",
    "Total_Passengers",
    "Total_Revenue",
    "Total_Cost",
    "Total_Profit",
    "Average_Delay",
    "Average_Utilization"
]
print("\n========== ROUTE PERFORMANCE ==========")

print(route_analysis)

# High revenue routes
top_revenue_routes = route_analysis.sort_values(
    "Total_Revenue",
    ascending=False
)
print("\n========== ROUTES BY REVENUE ==========")

print(top_revenue_routes)

# Customer segment analysis
customer_analysis = df.groupby(
    "Customer_Type"
).agg({
    "Trip_ID": "count",
    "Passengers": "sum",
    "Revenue": "sum",
    "Profit": "sum"
})
#rename
customer_analysis.columns = [
    "Total_Trips",
    "Total_Passengers",
    "Total_Revenue",
    "Total_Profit"
]
print("\n========== CUSTOMER ANALYSIS ==========")

print(customer_analysis)

# payment method analysis
payment_analysis = df.groupby(
    "Payment_Method"
).agg({
    "Trip_ID": "count",
    "Passengers": "sum",
    "Revenue": "sum"
})
# rename
payment_analysis.columns = [
    "Total_Trips",
    "Total_Passengers",
    "Total_Revenue"
]
print("\n========== PAYMENT ANALYSIS ==========")

print(payment_analysis)

# peak hour analysis
hour_analysis = df.groupby(
    "Hour"
).agg({
    "Trip_ID": "count",
    "Passengers": "sum",
    "Revenue": "sum"
})
#rename
hour_analysis.columns = [
    "Total_Trips",
    "Total_Passengers",
    "Total_Revenue"
]
print("\n========== HOURLY ANALYSIS ==========")

print(hour_analysis)
## find highest passenger-demand hour
peak_hour = hour_analysis[
    "Total_Passengers"
].idxmax()

print(
    "\nPeak passenger-demand hour:",
    peak_hour
)

# Daily analysis
day_analysis = df.groupby(
    "Day_Name"
).agg({
    "Trip_ID": "count",
    "Passengers": "sum",
    "Revenue": "sum"
})
print("\n========== DAILY ANALYSIS ==========")

print(day_analysis)

# Monthly revenue analysis
monthly_analysis = df.groupby(
    ["Year", "Month"]
).agg({
    "Trip_ID": "count",
    "Passengers": "sum",
    "Revenue": "sum",
    "Profit": "sum"
})
print("\n========== MONTHLY ANALYSIS ==========")

print(monthly_analysis)

# Delay analysis
delayed_trips = df[
    df["Status"] == "Delayed"
]

cancelled_trips = df[
    df["Status"] == "Cancelled"
]

completed_trips = df[
    df["Status"] == "Completed"
]

#calculate percentage
delay_rate = (
    len(delayed_trips) /
    len(df)
) * 100

cancellation_rate = (
    len(cancelled_trips) /
    len(df)
) * 100

completion_rate = (
    len(completed_trips) /
    len(df)
) * 100

print("\n========== TRIP STATUS KPIs ==========")

print(
    "Completion Rate:",
    round(completion_rate, 2),
    "%"
)

print(
    "Delay Rate:",
    round(delay_rate, 2),
    "%"
)

print(
    "Cancellation Rate:",
    round(cancellation_rate, 2),
    "%"
)

#Capacity utilization
def utilization_category(value):

    if value < 50:
        return "Low"

    elif value < 80:
        return "Medium"

    else:
        return "High"

df["Utilization_Category"] = (
    df["Utilization_Percentage"]
    .apply(utilization_category)
)

print(
    df["Utilization_Category"]
    .value_counts()
)

## Create a KPI summary table
kpi_summary = pd.DataFrame({
    "KPI": [
        "Total Trips",
        "Total Passengers",
        "Total Revenue",
        "Total Cost",
        "Total Profit",
        "Profit Margin",
        "Average Fare",
        "Average Delay",
        "Average Utilization",
        "Total Distance",
        "Average Duration",
        "Completion Rate",
        "Delay Rate",
        "Cancellation Rate"
    ],

    "Value": [
        total_trips,
        total_passengers,
        total_revenue,
        total_cost,
        total_profit,
        profit_margin,
        average_fare,
        average_delay,
        average_utilization,
        total_distance,
        average_duration,
        completion_rate,
        delay_rate,
        cancellation_rate
    ]
})

print("\n========== KPI SUMMARY ==========")

print(kpi_summary)

# save analysis results
kpi_summary.to_csv(
    "data/processed/kpi_summary.csv",
    index=False
)
#route analysis
route_analysis.to_csv(
    "data/processed/route_analysis.csv"
)
# vehicle analysis
vehicle_analysis.to_csv(
    "data/processed/vehicle_analysis.csv"
)
# customer Analysis
customer_analysis.to_csv(
    "data/processed/customer_analysis.csv"
)
#hourly analysis
customer_analysis.to_csv(
    "data/processed/customer_analysis.csv"
)
#monthly analysis
monthly_analysis.to_csv(
    "data/processed/monthly_analysis.csv"
)