import pandas as pd
from datetime import date

promotions = [
    {
        "PromotionID": 1,
        "CampaignName": "Spring Hiking Event",
        "CampaignType": "Seasonal",
        "DiscountPercent": 10,
        "StartDate": "2025-03-01",
        "EndDate": "2025-04-30",
        "TestGroup": "A",
        "TargetSegment": "Outdoor Enthusiast",
        "CategoryTarget": "Hiking"
    },

    {
        "PromotionID": 2,
        "CampaignName": "Spring Hiking Event",
        "CampaignType": "Seasonal",
        "DiscountPercent": 15,
        "StartDate": "2025-03-01",
        "EndDate": "2025-04-30",
        "TestGroup": "B",
        "TargetSegment": "Outdoor Enthusiast",
        "CategoryTarget": "Hiking"
    },

    {
        "PromotionID": 3,
        "CampaignName": "Summer Camping Sale",
        "CampaignType": "Seasonal",
        "DiscountPercent": 25,
        "StartDate": "2025-06-01",
        "EndDate": "2025-08-31",
        "TestGroup": "None",
        "TargetSegment": "All",
        "CategoryTarget": "Camping"
    },

    {
        "PromotionID": 4,
        "CampaignName": "VIP Appreciation",
        "CampaignType": "Loyalty",
        "DiscountPercent": 10,
        "StartDate": "2025-09-01",
        "EndDate": "2025-09-30",
        "TestGroup": "None",
        "TargetSegment": "VIP",
        "CategoryTarget": "All"
    },

    {
        "PromotionID": 5,
        "CampaignName": "Black Friday",
        "CampaignType": "Holiday",
        "DiscountPercent": 40,
        "StartDate": "2025-11-24",
        "EndDate": "2025-11-30",
        "TestGroup": "None",
        "TargetSegment": "All",
        "CategoryTarget": "All"
    },

    {
        "PromotionID": 6,
        "CampaignName": "Holiday Gifts",
        "CampaignType": "Holiday",
        "DiscountPercent": 20,
        "StartDate": "2025-12-01",
        "EndDate": "2025-12-24",
        "TestGroup": "None",
        "TargetSegment": "Casual",
        "CategoryTarget": "All"
    }
]

df = pd.DataFrame(promotions)

df.to_csv(
    "C:/Projects/RetailAnalytics/data/raw/promotions.csv",
    index=False
)

print(
    f"Created {len(df)} promotions"
)