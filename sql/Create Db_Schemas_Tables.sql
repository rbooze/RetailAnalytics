CREATE DATABASE BlueRidgeAnalytics;
Go

--------------------------------------------

-- Create schemas
USE BlueRidgeAnalytics;
GO

CREATE SCHEMA staging;		-- Raw imported data
GO

CREATE SCHEMA warehouse;	-- Analytical model
GO

CREATE SCHEMA reporting;	-- Optimized for dashboards
GO

--------------------------------------------

-- Create tables for raw data
CREATE TABLE staging.Customers
(
    CustomerID INT,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    State CHAR(2),
    Segment VARCHAR(20),
    JoinDate DATE
);

CREATE TABLE staging.Products
(
    ProductID INT,
    ProductName VARCHAR(100),
    Category VARCHAR(50),
    SupplierID INT,
    Cost DECIMAL(10,2),
    Price DECIMAL(10,2)
);

CREATE TABLE staging.Suppliers
(
    SupplierID INT,
    SupplierName VARCHAR(100),
    LeadTimeDays INT,
    QualityScore DECIMAL(5,2)
);

--------------------------------------------

-- Create tables for warehouse layer
CREATE TABLE warehouse.DimCustomer
(
    CustomerKey INT IDENTITY(1,1) PRIMARY KEY,
    CustomerID INT,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    State CHAR(2),
    Segment VARCHAR(20),
    JoinDate DATE
);

CREATE TABLE warehouse.DimSupplier
(
    SupplierKey INT IDENTITY(1,1) PRIMARY KEY,
    SupplierID INT,
    SupplierName VARCHAR(100),
    LeadTimeDays INT,
    QualityScore DECIMAL(5,2)
);

CREATE TABLE warehouse.DimProduct
(
    ProductKey INT IDENTITY(1,1) PRIMARY KEY,
    ProductID INT,
    ProductName VARCHAR(100),
    Category VARCHAR(50),
    SupplierKey INT,
    Cost DECIMAL(10,2),
    Price DECIMAL(10,2)
);

--------------------------------------------

-- Create Date table
CREATE TABLE warehouse.DimDate
(
    DateKey INT PRIMARY KEY,
    FullDate DATE,
    Year INT,
    Quarter INT,
    Month INT,
    MonthName VARCHAR(20),
    Day INT,
    DayName VARCHAR(20)
);

--------------------------------------------

-- Create Sales table in warehouse schema
CREATE TABLE warehouse.FactSales
(
    SalesKey INT IDENTITY(1,1) PRIMARY KEY,
	OrderID INT,
    DateKey INT,
    CustomerKey INT,
    ProductKey INT,
    Quantity INT,
    SalesAmount DECIMAL(12,2),
    CostAmount DECIMAL(12,2),
    ProfitAmount DECIMAL(12,2),
    DiscountAmount DECIMAL(12,2)
);

--------------------------------------------

-- Create Sales table in staging schema
CREATE TABLE staging.Sales
(
    OrderID INT,
    OrderDate DATE,
    CustomerID INT,
    ProductID INT,
    Quantity INT,
    SalesAmount DECIMAL(12,2),
    CostAmount DECIMAL(12,2),
    DiscountAmount DECIMAL(12,2)
);