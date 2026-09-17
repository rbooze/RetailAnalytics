INSERT INTO Fact.Sales
(
    SalesID,
    OrderID,
    DateKey,
    CustomerKey,
    ProductKey,
    PromotionKey,
    ChannelKey,
    WarehouseKey,
    Quantity,
    SalesAmount,
    CostAmount,
    DiscountAmount,
    ProfitAmount
)

SELECT
    s.SalesID,
    s.OrderID,
    s.DateKey,
    c.CustomerKey,
    p.ProductKey,
    pr.PromotionKey,
    ch.ChannelKey,
    w.WarehouseKey,
    s.Quantity,
    s.SalesAmount,
    s.CostAmount,
    s.DiscountAmount,
    s.ProfitAmount
FROM Staging.Sales s WITH (NOLOCK)
INNER JOIN Dim.Customer c WITH (NOLOCK)
    ON s.CustomerID = c.CustomerID
INNER JOIN Dim.Product p WITH (NOLOCK)
    ON s.ProductID = p.ProductID
INNER JOIN Dim.Promotion pr WITH (NOLOCK)
    ON s.PromotionID = pr.PromotionID
INNER JOIN Dim.Channel ch WITH (NOLOCK)
    ON s.ChannelID = ch.ChannelID
INNER JOIN Dim.Warehouse w WITH (NOLOCK)
    ON s.WarehouseID = w.WarehouseID;