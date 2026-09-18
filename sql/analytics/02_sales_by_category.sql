SELECT
    p.Category,
    COUNT(DISTINCT s.OrderID) AS Orders,
    SUM(s.Quantity) AS UnitsSold,
    SUM(s.SalesAmount) AS Revenue,
    SUM(s.ProfitAmount) AS Profit,
    ROUND(
        100.0 * SUM(s.ProfitAmount) /
        NULLIF(SUM(s.SalesAmount), 0),
        2
    ) AS ProfitMarginPct
FROM Fact.Sales s WITH (NOLOCK)
INNER JOIN Dim.Product p WITH (NOLOCK)
    ON s.ProductKey = p.ProductKey
GROUP BY p.Category
ORDER BY Revenue DESC;