import pyodbc
import pandas as pd

def get_connection():
    return pyodbc.connect(
        "Driver={ODBC Driver 17 for SQL Server};"
        "Server=localhost\\SQLEXPRESS;"
        "Database=RetailAnalyticsDW;"
        "Trusted_Connection=yes;"
    )

def read_sql(query):
    conn = get_connection()

    #print("Connected Database:", conn.getinfo(pyodbc.SQL_DATABASE_NAME))
    #print("Database:", conn.getinfo(pyodbc.SQL_DATABASE_NAME)

    df = pd.read_sql(query, conn)
    conn.close()
    return df