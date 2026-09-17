import pandas as pd
import random
import numpy as np

random.seed(42)
np.random.seed(42)

NUM_SUPPLIERS = 60

supplier_profiles = [
    {
        "SupplierName": "Summit Gear Co.",
        "Country": "USA",
        "SupplierTier": "Premium",
        "LeadTimeDays": 5,
        "QualityScore": 98,
        "CostRating": "High"
    },

    {
        "SupplierName": "Alpine Supply",
        "Country": "USA",
        "SupplierTier": "Strategic",
        "LeadTimeDays": 7,
        "QualityScore": 95,
        "CostRating": "Medium"
    },

    {
        "SupplierName": "TrailWorks",
        "Country": "Vietnam",
        "SupplierTier": "Cost Leader",
        "LeadTimeDays": 18,
        "QualityScore": 86,
        "CostRating": "Low"
    },

    {
        "SupplierName": "Peak Manufacturing",
        "Country": "China",
        "SupplierTier": "Standard",
        "LeadTimeDays": 12,
        "QualityScore": 90,
        "CostRating": "Medium"
    },

    {
        "SupplierName": "North Ridge Imports",
        "Country": "China",
        "SupplierTier": "High Risk",
        "LeadTimeDays": 25,
        "QualityScore": 75,
        "CostRating": "Very Low"
    }
]

suppliers = []

# Add strategic suppliers first

supplier_id = 1

for supplier in supplier_profiles:
    suppliers.append({
        "SupplierID": supplier_id,
        **supplier,
        "RiskLevel":
            "High"
            if supplier["QualityScore"] < 80
            else "Low"
    })

    supplier_id += 1

# Generate remaining suppliers

for i in range(
    supplier_id,
    NUM_SUPPLIERS + 1
):

    quality = random.randint(
        80,
        95
    )

    suppliers.append({

        "SupplierID": i,
        "SupplierName":
            f"Outdoor Supplier {i}",
            
        "Country":
            random.choice(
                [
                    "USA",
                    "Canada",
                    "China",
                    "Vietnam",
                    "Mexico"
                ]
            ),

        "SupplierTier":
            random.choice(
                [
                    "Standard",
                    "Strategic",
                    "Cost Leader"
                ]
            ),

        "LeadTimeDays":
            random.randint(
                7,
                20
            ),

        "QualityScore":
            quality,

        "CostRating":
            random.choice(
                [
                    "Low",
                    "Medium",
                    "High"
                ]
            ),

        "RiskLevel":
            "Medium"
    })

df = pd.DataFrame(suppliers)

df.to_csv(
    "C:/Projects/RetailAnalytics/data/raw/suppliers.csv",
    index=False
)

print(
    f"Created {len(df)} suppliers"
)