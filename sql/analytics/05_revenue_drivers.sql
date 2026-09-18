SELECT
    COUNT(DISTINCT OrderID) AS Orders,
    SUM(SalesAmount) AS Revenue,

    ROUND(
        SUM(SalesAmount) /
        COUNT(DISTINCT OrderID),
        2
    ) AS AverageOrderValue,

    SUM(Quantity) AS UnitsSold,

    ROUND(
        SUM(Quantity) * 1.0 /
        COUNT(DISTINCT OrderID),
        2
    ) AS UnitsPerOrder
FROM Fact.Sales WITH (NOLOCK);