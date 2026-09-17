import pandas as pd
from sqlalchemy import create_engine

# -----------------------------
# Database Connection
# -----------------------------

server = "localhost\\SQLEXPRESS"
database = "BlueRidgeAnalytics"

connection_string = (
    "mssql+pyodbc://"
    f"{server}/{database}"
    "?driver=ODBC+Driver+17+for+SQL+Server"
    "&trusted_connection=yes"
)

engine = create_engine(connection_string)

# -----------------------------
# File Locations
# -----------------------------

DATA_PATH = "C:/projects/RetailAnalytics/data/raw/"

# -----------------------------
# Load Function
# -----------------------------

def load_table(file_name, table_name):
    print(f"Loading {file_name}...")

    df = pd.read_csv(
        f"{DATA_PATH}/{file_name}"
    )

    print(
        f"Rows found: {len(df)}"
    )

    df.to_sql(
        table_name,
        engine,
        schema="staging",
        if_exists="append",
        index=False
    )

    print(
        f"{table_name} loaded successfully"
    )

# -----------------------------
# Execute Loads
# -----------------------------

if __name__ == "__main__":
    #load_table(
    #    "customers.csv",
    #    "Customers"
    #)

    #load_table(
    #    "products.csv",
    #    "Products"
    #)

    #load_table(
    #    "suppliers.csv",
    #    "Suppliers"
    #)

    load_table(
        "sales.csv",
        "Sales"
    )

    print(
        "ETL completed!"
    )