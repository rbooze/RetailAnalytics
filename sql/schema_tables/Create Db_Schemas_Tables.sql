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

-- Create tables for warehouse layer