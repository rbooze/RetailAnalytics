# Retail Analytics Platform

## Overview

Retail Analytics is an end-to-end Business Intelligence and Analytics platform built using SQL Server, Python, and Power BI.

The project simulates a modern retail organization by integrating sales, customers, products, suppliers, inventory, promotions, marketing experiments, and financial performance into a dimensional data warehouse.

The project demonstrates the complete analytics lifecycle:

- Data warehouse design
- ETL development
- Synthetic enterprise data generation
- Statistical analysis
- A/B testing
- Executive dashboards
- Business analytics

---

## Technology Stack

SQL Server
Python
Power BI
Git
GitHub

Libraries

- pandas
- numpy
- pyodbc
- scipy
- faker

---

## Project Structure

RetailAnalytics
data/
    processed/
    raw/
dbt/
docs/
powerbi/
python/
    common/
    etl/
    experiments/
    generators/
    statistics/
    validation/
screenshots/
sql/
    analytics/
        ab-testing/
        experiments/
    etl/
    schema_tables/
    views/

---

## Data Warehouse

Dimensions
- Channel
- Customer
- Date
- Product
- Promotion
- Supplier
- Warehouse

Facts
- Inventory
- CustomerExperiment

Staging
- Channel
- Customer
- Dates
- ExperimentResults
- Products
- Promotions
- Sales
- Suppliers
- Warehouses

---

## Business Questions Answered

Sales
- Which products are most profitable?
- Which customer segments drive revenue?
- Which promotions improve sales?

Marketing
- Did the promotion increase purchases?
- What was the conversion lift?
- Which customer segments responded best?

Finance
- Revenue
- Profit
- Profit Margin
- Incremental Profit

---

## Statistical Analysis

The project includes:
- A/B Testing
- Two-proportion Z Test
- Confidence Intervals
- Effect Size
- Incremental Profit Analysis

---

## Power BI Dashboards

### Executive Summary
- Conversion Rate
- Incremental Profit
- Revenue Lift

### Financial Performance
- Revenue
- Profit
- Margin Impact

### Customer Segments
- Purchase Rate
- Revenue
- Profit

### Analyst Deep Dive
- Customer Detail
- Scatter Analysis
- Timeline
- Drill-through

---

## Future Enhancements
- Forecasting
- Customer Lifetime Value
- Market Basket Analysis
- RFM Analysis
- Churn Prediction
- Inventory Optimization