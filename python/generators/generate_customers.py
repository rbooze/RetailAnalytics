import pandas as pd
import numpy as np
from faker import Faker
import random


fake = Faker()

random.seed(42)
np.random.seed(42)

NUM_CUSTOMERS = 250000


segments = [
    "Budget",
    "Casual",
    "Outdoor Enthusiast",
    "Professional",
    "VIP"
]

segment_weights = [
    .45,
    .30,
    .15,
    .07,
    .03
]

states = [
    "NC","VA","SC","GA","TN",
    "FL","TX","CO","WA","CA"
]

customers = []

for customer_id in range(1, NUM_CUSTOMERS + 1):
    segment = np.random.choice(
        segments,
        p=segment_weights
    )

    customers.append({
        "CustomerID": customer_id,
        "FirstName": fake.first_name(),
        "LastName": fake.last_name(),
        "State": random.choice(states),
        "Segment": segment,
        "JoinDate": fake.date_between(
            start_date="-5y",
            end_date="today"
        )
    })

df = pd.DataFrame(customers)

df.to_csv(
    "C:/Projects/RetailAnalytics/data/raw/customers.csv",
    index=False
)

print(
    f"Created {len(df)} customers"
)