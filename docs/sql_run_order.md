# SQL Build Order

## 1. Create Database
Create RetailAnalyticsDW
---
## 2. Schemas
Analytics
Fact
Dim
Staging

---

## 3. Dimension Tables
Dim.Channel
Dim.Customer
Dim.Date
Dim.Product
Dim.Promotion
Dim.Supplier
Dim.Warehouse

---

## 4. Fact Tables
Fact.CustomerExperiment
Fact.Sales

---

## 5. Staging Tables
Staging.Channels
Staging.Customers
Staging.Dates
Staging.ExperimentResults
Staging.Products
Staging.Promotions
Staging.Sales
Staging.Suppliers
Staging.Warehouses

---

## 6. Constraints
Primary Keys
Foreign Keys
Indexes

---

## 7. Analytics Views
vw_ExperimentSummary
vw_ExperimentCustomerDetail

Future
vwSalesSummary
vwInventoryPerformance
vwSupplierPerformance