USE BlueRidgeAnalytics;
GO

INSERT INTO warehouse.DimCustomer
(
    CustomerID,
    FirstName,
    LastName,
    State,
    Segment,
    JoinDate
)

SELECT
    CustomerID,
    FirstName,
    LastName,
    State,
    Segment,
    JoinDate
FROM staging.Customers;

-------------------------------------------------

INSERT INTO warehouse.DimSupplier
(
    SupplierID,
    SupplierName,
    LeadTimeDays,
    QualityScore
)

SELECT
    SupplierID,
    SupplierName,
    LeadTimeDays,
    QualityScore
FROM staging.Suppliers;

-------------------------------------------------

INSERT INTO warehouse.DimProduct
(
    ProductID,
    ProductName,
    Category,
    SupplierKey,
    Cost,
    Price
)

SELECT 
	p.ProductID,
    p.ProductName,
    p.Category,
    ds.SupplierKey,
    p.Cost,
    p.Price 
FROM staging.Products p
INNER JOIN warehouse.DimSupplier ds WITH (NOLOCK)
	ON p.SupplierID = ds.SupplierKey;

-------------------------------------------------

INSERT INTO warehouse.FactSales
(
    OrderID,
    DateKey,
    CustomerKey,
    ProductKey,
    Quantity,
    SalesAmount,
    CostAmount,
    ProfitAmount,
    DiscountAmount
)

SELECT
    s.OrderID,
    CONVERT(INT, FORMAT(s.OrderDate,'yyyyMMdd')),
	c.CustomerKey,
    p.ProductKey,
    s.Quantity,
    s.SalesAmount,
    s.CostAmount,
    s.SalesAmount - s.CostAmount,
    s.DiscountAmount
FROM staging.Sales s
INNER JOIN warehouse.DimCustomer c
    ON s.CustomerID = c.CustomerID
INNER JOIN warehouse.DimProduct p
    ON s.ProductID = p.ProductID;