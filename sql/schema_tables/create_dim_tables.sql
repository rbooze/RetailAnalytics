CREATE TABLE Dim.Date
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
GO

CREATE TABLE Dim.Customer
(
    CustomerKey INT IDENTITY(1,1) PRIMARY KEY,
    CustomerID INT,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    State VARCHAR(10),
    Segment VARCHAR(50),
    JoinDate DATE
);
GO

CREATE TABLE Dim.Product
(
    ProductKey INT IDENTITY(1,1) PRIMARY KEY,
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

CREATE TABLE Dim.Supplier
(
    SupplierKey INT IDENTITY(1,1) PRIMARY KEY,
    SupplierID INT,
    SupplierName VARCHAR(100),
    Country VARCHAR(50),
    SupplierTier VARCHAR(50),
    LeadTimeDays INT,
    QualityScore DECIMAL(5,2),
    RiskLevel VARCHAR(20)
);
GO

CREATE TABLE Dim.Promotion
(
    PromotionKey INT IDENTITY(1,1) PRIMARY KEY,
    PromotionID INT,
    CampaignName VARCHAR(100),
    CampaignType VARCHAR(50),
    DiscountPercent DECIMAL(5,2),
    TestGroup VARCHAR(20),
    TargetSegment VARCHAR(50),
    CategoryTarget VARCHAR(50)
);
GO

CREATE TABLE Dim.Channel
(
    ChannelKey INT IDENTITY(1,1) PRIMARY KEY,
    ChannelID INT,
    ChannelName VARCHAR(50)
);
GO

CREATE TABLE Dim.Warehouse
(
    WarehouseKey INT IDENTITY(1,1) PRIMARY KEY,
    WarehouseID INT,
    WarehouseName VARCHAR(100),
    Region VARCHAR(50),
    Capacity INT
);
GO

