"""
Generate A/B Test Experiment Results

Purpose:
    Simulate customer behavior after a marketing experiment.

Process:
    1. Read experiment assignments from SQL Server
    2. Apply purchase probabilities
    3. Generate purchases
    4. Generate revenue
    5. Validate results
    6. Compare Control vs Treatment

"""

import random
import sys
from datetime import timedelta
from pathlib import Path

import pandas as pd
import numpy as np
import pyodbc

# Allow this script to be run directly from the repository root.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from experiments.experiment_config import EXPERIMENT
from experiments.customer_behavior import SEGMENT_MULTIPLIERS
from experiments.revenue_generator import generate_revenue
from experiments.profit_generator import generate_profit

# Make results reproducible
random.seed(42)
np.random.seed(42)

# SQL Server connection
conn = pyodbc.connect(
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=localhost\\SQLEXPRESS;"
    "Database=RetailAnalyticsDW;"
    "Trusted_Connection=yes;"
)

# Read the experiment
query = f"""
SELECT
    e.CustomerID,
    e.GroupName,
    c.Segment
FROM Fact.CustomerExperiment e WITH (NOLOCK)
JOIN Dim.Customer c WITH (NOLOCK)
    ON e.CustomerID = c.CustomerID
"""

df = pd.read_sql(query, conn)

# Purchase Probability
def purchase_probability(group, segment):
    base = EXPERIMENT["groups"][group]["purchase_probability"]

    multiplier = SEGMENT_MULTIPLIERS[segment]["purchase"]

    probability = base * multiplier

    return min(probability, 0.95)    # Ensure probability does not exceed 0.95

# Simulate Purchases (Bernoulli trial)
df["Purchased"] = df.apply(
    lambda row: 
        random.random() < purchase_probability(row["GroupName"], row["Segment"]),
    axis=1
)

# --------------------------------------------------
# Generate Revenue 
# --------------------------------------------------
df["Revenue"] = np.where(
    df["Purchased"],

    df.apply(
        lambda row:
            generate_revenue(
                row.GroupName,
                row.Segment
            ),
        axis=1
    ),

    0.0
)

# --------------------------------------------------
# Generate Profit
# --------------------------------------------------
df["Profit"] = df.apply(
    lambda row:
        generate_profit(
            row["Revenue"],
            row["GroupName"]
        ),

    axis=1
)

# --------------------------------------------------
# Validation Output
# --------------------------------------------------
print("\nPurchase Counts")

print(
    df["Purchased"]
    .value_counts()
)

print("\nRevenue Distribution By Segment (Purchasers Only)")

print(
    df[df["Purchased"]]
    .groupby("Segment")["Revenue"]
    .describe()
)

# --------------------------------------------------
# A/B Test Group Comparison
# --------------------------------------------------
print("\nExperiment Results")

group_results = (
    df.groupby("GroupName")["Purchased"]
    .agg(
        Customers="count",
        Purchases="sum",
        PurchaseRate="mean"
    )
)

print(group_results)

# --------------------------------------------------
# Revenue Comparison
# --------------------------------------------------
print("\nRevenue Results")
revenue_results = (
    df.groupby("GroupName")
    .agg(
        Customers=("CustomerID","count"),
        Purchasers=("Purchased","sum"),
        Revenue=("Revenue","sum")
    )
)

revenue_results["RevenuePerCustomer"] = (
    revenue_results["Revenue"] / revenue_results["Customers"]
)

print(revenue_results)

print("\nProfit Results")
profit_results = (
    df.groupby("GroupName")
    .agg(
        Customers=("CustomerID","count"),
        Purchasers=("Purchased","sum"),
        Revenue=("Revenue","sum"),
        Profit=("Profit","sum")
    )
)

profit_results["ProfitPerCustomer"] = (
    profit_results["Profit"] / profit_results["Customers"]
)

profit_results["ProfitMarginPct"] = (
    profit_results["Profit"] / profit_results["Revenue"] * 100
)

print(profit_results)

"""
print()
print(df.head())
print()
print(df["Purchased"].value_counts())
print()
df[df["Purchased"]].groupby("Segment")["Revenue"].describe()
"""

# --------------------------------------------------
# Close Connection
# --------------------------------------------------

conn.close()