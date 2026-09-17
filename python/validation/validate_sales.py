import pandas as pd
from pathlib import Path

DATA_PATH = Path("C:/Projects/RetailAnalytics/data/raw")

sales = pd.read_csv(
    DATA_PATH / "sales.csv"
)

print("\n--- ROW COUNT ---")
print(len(sales))

print("\n--- NULL CHECK ---")
print(
    sales.isnull()
    .sum()
)

print("\n--- DUPLICATE SALES IDS ---")
print(
    sales["SalesID"]
    .duplicated()
    .sum()
)

print("\n--- NEGATIVE VALUES ---")

print(
    "Negative Sales:",
    (sales["SalesAmount"] < 0).sum()
)

print(
    "Negative Cost:",
    (sales["CostAmount"] < 0).sum()
)

print(
    "Negative Profit:",
    (sales["ProfitAmount"] < 0).sum()
)

print("\n--- PROFIT SUMMARY ---")

print(
    sales[
        [
            "SalesAmount",
            "CostAmount",
            "ProfitAmount"
        ]
    ]
    .describe()
)

print("\n--- TOTALS ---")

print(
    "Revenue:",
    round(
        sales["SalesAmount"].sum(),
        2
    )
)

print(
    "Profit:",
    round(
        sales["ProfitAmount"].sum(),
        2
    )
)

print(
    "Margin:",
    round(
        sales["ProfitAmount"].sum()
        /
        sales["SalesAmount"].sum()
        *
        100,
        2
    ),
    "%"
)