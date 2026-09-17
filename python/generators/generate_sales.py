import pandas as pd
import numpy as np
import random
from pathlib import Path

# -----------------------------
# Configuration
# -----------------------------

NUM_SALES = 500000
BATCH_SIZE = 50000

random.seed(42)
np.random.seed(42)

DATA_PATH = Path("C:/Projects/RetailAnalytics/data/raw")

# -----------------------------
# Load Dimensions
# -----------------------------

customers = pd.read_csv(
    DATA_PATH / "customers.csv"
)

products = pd.read_csv(
    DATA_PATH / "products.csv"
)

promotions = pd.read_csv(
    DATA_PATH / "promotions.csv"
)

channels = pd.read_csv(
    DATA_PATH / "channels.csv"
)

warehouses = pd.read_csv(
    DATA_PATH / "warehouses.csv"
)

dates = pd.read_csv(
    DATA_PATH / "dates.csv"
)

# -----------------------------
# Business Rules
# -----------------------------

segment_multiplier = {
    "Budget": .8,
    "Casual": 1.0,
    "Outdoor Enthusiast": 1.5,
    "Professional": 1.3,
    "VIP": 2.0
}

category_multiplier = {
    "Camping": {
        6: 1.4,
        7: 1.5,
        8: 1.4
    },

    "Kayaking": {
        6: 1.5,
        7: 1.6,
        8: 1.5
    },

    "Apparel": {
        11: 1.4,
        12: 1.5,
        1: 1.3
    }
}

# -----------------------------
# Generate batches
# -----------------------------

output_file = (
    DATA_PATH / "sales.csv"
)

if output_file.exists():
    output_file.unlink()

sales_id = 1

for batch_start in range(
    0,
    NUM_SALES,
    BATCH_SIZE
):

    batch_size = min(
        BATCH_SIZE,
        NUM_SALES - batch_start
    )

    customer_sample = customers.sample(
        batch_size,
        replace=True
    )

    product_sample = products.sample(
        batch_size,
        replace=True
    )

    date_sample = dates.sample(
        batch_size,
        replace=True
    )

    promotion_sample = promotions.sample(
        batch_size,
        replace=True
    )

    channel_sample = channels.sample(
        batch_size,
        replace=True
    )

    warehouse_sample = warehouses.sample(
        batch_size,
        replace=True
    )

    df = pd.DataFrame()

    df["SalesID"] = range(
        sales_id,
        sales_id + batch_size
    )

    df["OrderID"] = (
        df["SalesID"] // 2
    )

    df["DateKey"] = (
        date_sample["DateKey"]
        .values
    )

    df["CustomerID"] = (
        customer_sample["CustomerID"]
        .values
    )

    df["ProductID"] = (
        product_sample["ProductID"]
        .values
    )

    df["PromotionID"] = (
        promotion_sample["PromotionID"]
        .values
    )

    df["ChannelID"] = (
        channel_sample["ChannelID"]
        .values
    )

    df["WarehouseID"] = (
        warehouse_sample["WarehouseID"]
        .values
    )

    df["Quantity"] = np.random.choice(
        [1,2,3,4],
        size=batch_size,
        p=[.65,.25,.08,.02]
    )

    df = df.merge(
        products[
            [
                "ProductID",
                "Price",
                "Cost",
                "Category"
            ]
        ],
        on="ProductID",
        how="left"
    )

    discount_rate = np.random.choice(
    [
        0,
        .10,
        .20,
        .40
    ],
    size=batch_size,
    p=[
        .55,
        .25,
        .15,
        .05
    ]
)

    discounted_price = (
        df["Price"] * (1 - discount_rate)
    )

    # Prevent selling below cost
    discounted_price = np.maximum(
        discounted_price,
        df["Cost"] * 1.05
    )

    df["DiscountAmount"] = (
        df["Price"] - discounted_price
    )

    df["SalesAmount"] = (
        df["Quantity"] * discounted_price
    )

    df["CostAmount"] = (
        df["Quantity"] * df["Cost"]
     )

    df["ProfitAmount"] = (
        df["SalesAmount"] - df["CostAmount"]
    )

    df = df[
        [
            "SalesID",
            "OrderID",
            "DateKey",
            "CustomerID",
            "ProductID",
            "PromotionID",
            "ChannelID",
            "WarehouseID",
            "Quantity",
            "SalesAmount",
            "CostAmount",
            "DiscountAmount",
            "ProfitAmount"
        ]
    ]

    df.to_csv(
        output_file,
        mode="a",
        header=not output_file.exists(),
        index=False
    )

    sales_id += batch_size

    print(
        f"Generated {sales_id-1:,} sales"
    )

print("FactSales generation complete")