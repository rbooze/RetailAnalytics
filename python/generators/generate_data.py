import pandas as pd
import numpy as np
from faker import Faker
from datetime import datetime
import os

fake = Faker()

OUTPUT_PATH = "C:/projects/RetailAnalytics/data/raw/"

os.makedirs(OUTPUT_PATH, exist_ok=True)

# -------------------------
# Customers
# -------------------------

def generate_customers(num_customers=10000):
    customers = []

    for i in range(1, num_customers + 1):
        customers.append({
            "CustomerID": i,
            "FirstName": fake.first_name(),
            "LastName": fake.last_name(),
            "State": fake.state_abbr(),
            "Segment": np.random.choice(
                ["Consumer", "Business", "VIP"],
                p=[0.75,0.20,0.05]
            ),
            "JoinDate": fake.date_between(
                start_date="-5y",
                end_date="today"
            )
        })
    
    return pd.DataFrame(customers)

# -------------------------
# Suppliers
# -------------------------

def generate_suppliers(num_suppliers=100):
    suppliers=[]

    for i in range(1,num_suppliers+1):
        suppliers.append({
            "SupplierID": i,
            "SupplierName": fake.company(),
            "LeadTimeDays": np.random.randint(2,30),
            "QualityScore": round(
                np.random.uniform(70,100),2
            )
        })

    return pd.DataFrame(suppliers)

# -------------------------
# Products
# -------------------------

def generate_products(num_products=1000, suppliers=100):
    products=[]
    categories=[
        "Camping",
        "Climbing",
        "Fishing",
        "Hiking",
        "Apparel",
        "Footwear"
    ]

    for i in range(1,num_products+1):
        cost=np.random.uniform(5,300)
        products.append({
            "ProductID":i,
            "ProductName":fake.word().title(),
            "Category":np.random.choice(categories),
            "SupplierID":np.random.randint(1,suppliers+1),
            "Cost":round(cost,2),
            "Price":round(cost*1.4,2)
        })

    return pd.DataFrame(products)

# -------------------------
# Sales
# -------------------------

def generate_sales(num_sales=500000, customers=10000, products=1000):
    sales=[]

    dates=pd.date_range(
        start="2022-01-01",
        end="2026-12-31"
    )

    for i in range(1,num_sales+1):
        product_id=np.random.randint(
            1,
            products+1
        )

        quantity=np.random.randint(
            1,
            6
        )

        cost=np.random.uniform(
            5,
            300
        )

        price=cost*1.4

        sales_amount=quantity*price

        discount=np.random.choice(
            [0,.05,.10,.20],
            p=[.60,.25,.10,.05]
        )

        final_sales=sales_amount*(1-discount)

        sales.append({
            "OrderID":i,
            "OrderDate":np.random.choice(
                dates
            ),
            "CustomerID":np.random.randint(
                1,
                customers+1
            ),
            "ProductID":product_id,
            "Quantity":quantity,
            "SalesAmount":round(
                final_sales,
                2
            ),
            "CostAmount":round(
                quantity*cost,
                2
            ),
            "DiscountAmount":round(
                sales_amount*discount,
                2
            )
        })

    return pd.DataFrame(sales)

if __name__=="__main__":
    customers=generate_customers()
    suppliers=generate_suppliers()
    products=generate_products()
    sales=generate_sales()

    customers.to_csv(
        f"{OUTPUT_PATH}/customers.csv",
        index=False
    )

    suppliers.to_csv(
        f"{OUTPUT_PATH}/suppliers.csv",
        index=False
    )

    products.to_csv(
        f"{OUTPUT_PATH}/products.csv",
        index=False
    )

    sales.to_csv(
    f"{OUTPUT_PATH}/sales.csv",
    index=False
    )   


    print("Data generation complete!")