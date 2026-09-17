CREATE TABLE Staging.Customers
(
    CustomerID INT,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    State VARCHAR(10),
    Segment VARCHAR(50),
    JoinDate DATE
);
GO

CREATE TABLE Staging.Products
(
    ProductID INT,
    ProductName VARCHAR(150),
    Category VARCHAR(50),
    Subcategory VARCHAR(50),
    SupplierID INT,
    Cost DECIMAL(10,2),
    Price DECIMAL(10,2),
    ProductStatus VARCHAR(20)
);
GO

CREATE TABLE Staging.Suppliers
(
    SupplierID INT,
    SupplierName VARCHAR(100),
    Country VARCHAR(50),
    SupplierTier VARCHAR(50),
    LeadTimeDays INT,
    QualityScore DECIMAL(5,2),
    CostRating VARCHAR(50),
    RiskLevel VARCHAR(20)
);
GO

CREATE TABLE Staging.Promotions
(
    PromotionID INT,
    CampaignName VARCHAR(100),
    CampaignType VARCHAR(50),
    DiscountPercent DECIMAL(5,2),
    TestGroup VARCHAR(20),
    TargetSegment VARCHAR(50),
    CategoryTarget VARCHAR(50)
);
GO

CREATE TABLE Staging.Sales
(
    SalesID INT,
    OrderID INT,
    DateKey INT,
    CustomerID INT,
    ProductID INT,
    PromotionID INT,
    ChannelID INT,
    WarehouseID INT,
    Quantity INT,
    SalesAmount DECIMAL(12,2),
    CostAmount DECIMAL(12,2),
    DiscountAmount DECIMAL(12,2),
    ProfitAmount DECIMAL(12,2)
);
GO

CREATE TABLE Staging.Dates
(
    DateKey INT,
    FullDate DATE,
    Year INT,
    Quarter INT,
    Month INT,
    MonthName VARCHAR(20),
    Day INT,
    DayName VARCHAR(20)
);
GO

CREATE TABLE Staging.Channels
(
    ChannelID INT,
    ChannelName VARCHAR(50)
);
GO

CREATE TABLE Staging.Warehouses
(
    WarehouseID INT,
    WarehouseName VARCHAR(100),
    Region VARCHAR(50),
    Capacity INT
);
GO

SELECT 
	*
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_SCHEMA='Staging';