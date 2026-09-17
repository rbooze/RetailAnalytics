DROP TABLE Fact.Sales;
GO

CREATE TABLE Fact.Sales
(
    SalesKey BIGINT IDENTITY(1,1) PRIMARY KEY,

    SalesID INT,
    OrderID INT,

    DateKey INT,
    CustomerKey INT,
    ProductKey INT,
    PromotionKey INT,
    ChannelKey INT,
    WarehouseKey INT,

    Quantity INT,
	SalesAmount DECIMAL(12,2),
    CostAmount DECIMAL(12,2),
    DiscountAmount DECIMAL(12,2),
    ProfitAmount DECIMAL(12,2)
);
GO