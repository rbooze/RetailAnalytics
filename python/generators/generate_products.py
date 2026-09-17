import pandas as pd
import numpy as np
import random

random.seed(42)
np.random.seed(42)

NUM_PRODUCTS = 2500

product_templates = {
    "Camping": {
        "Tents": [
            "Alpine",
            "Summit",
            "TrailMaster",
            "Explorer"
        ],

        "Sleeping Bags": [
            "Cold Weather",
            "Trail Comfort",
            "Mountain"
        ],

        "Lighting": [
            "LED Camp",
            "Rechargeable",
            "Outdoor Lantern"
        ]
    },

    "Hiking": {

        "Backpacks": [
            "Trail",
            "Explorer",
            "Adventure"
        ],

        "Trekking Poles": [
            "Carbon",
            "Aluminum",
            "Ultralight"
        ]

    },

    "Apparel": {

        "Jackets": [
            "RainShell",
            "Thermal",
            "StormGuard"
        ],

        "Shirts": [
            "Performance",
            "Outdoor",
            "Moisture"
        ]
    },

    "Footwear": {

        "Hiking Boots": [
            "Summit",
            "TrailPro",
            "Mountain"
        ],

        "Trail Shoes": [
            "Runner",
            "Adventure",
            "Explorer"
        ]

    },

    "Fishing": {

        "Rods": [
            "River",
            "Lake",
            "Professional"
        ],

        "Reels": [
            "Spin",
            "Pro",
            "Tournament"
        ]
    },

    "Kayaking": {
        "Kayaks": [
            "River",
            "Ocean",
            "Explorer"
        ],

        "Paddles": [
            "Carbon",
            "Aluminum"
        ]
    }
}

products = []

supplier_ids = list(range(1,61))

product_id = 1

while len(products) < NUM_PRODUCTS:
    category = random.choice(
        list(product_templates.keys())
    )

    subcategory = random.choice(
        list(product_templates[category].keys())
    )

    model = random.choice(
        product_templates[category][subcategory]
    )

    name = (
        f"{model} "
        f"{subcategory}"
    )

    cost = round(
        random.uniform(10,250),
        2
    )

    margin = random.uniform(
        1.4,
        2.8
    )

    price = round(
        cost * margin,
        2
    )

    products.append({
        "ProductID": product_id,
        "ProductName": name,
        "Category": category,
        "Subcategory": subcategory,
        "SupplierID": random.choice(
            supplier_ids
        ),
        "Cost": cost,
        "Price": price,
        "ProductStatus": random.choice(
            [
                "Active",
                "Active",
                "Active",
                "Discontinued"
            ]
        )
    })

    product_id += 1

df = pd.DataFrame(products)

df.to_csv(
    "C:/Projects/RetailAnalytics/data/raw/products.csv",
    index=False
)

print(
    f"Created {len(df)} products"
)