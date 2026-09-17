import pandas as pd

warehouses = [
    {
        "WarehouseID":1,
        "WarehouseName":"East Distribution Center",
        "Region":"East",
        "Capacity":500000
    },

    {
        "WarehouseID":2,
        "WarehouseName":"South Distribution Center",
        "Region":"South",
        "Capacity":450000
    },

    {
        "WarehouseID":3,
        "WarehouseName":"Midwest Distribution Center",
        "Region":"Midwest",
        "Capacity":350000
    },

    {
        "WarehouseID":4,
        "WarehouseName":"West Distribution Center",
        "Region":"West",
        "Capacity":400000
    }
]

df = pd.DataFrame(warehouses)

df.to_csv(
    "C:/Projects/RetailAnalytics/data/raw/warehouses.csv",
    index=False
)

print("Warehouses generated")