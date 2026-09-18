SELECT
    c.Segment,
    COUNT(DISTINCT c.CustomerID) AS Customers,
    COUNT(DISTINCT s.OrderID) AS Orders,
    SUM(s.SalesAmount) AS Revenue,
    SUM(s.ProfitAmount) AS Profit,

    ROUND(
        SUM(s.SalesAmount) /
        COUNT(DISTINCT c.CustomerID),
        2
    ) AS RevenuePerCustomer,

    ROUND(
        100.0 * SUM(s.ProfitAmount) /
        NULLIF(SUM(s.SalesAmount),0),
        2
    ) AS ProfitMarginPct
FROM Fact.Sales s WITH (NOLOCK)
INNER JOIN Dim.Customer c WITH (NOLOCK)
    ON s.CustomerKey = c.CustomerKey
GROUP BY
    c.Segment
ORDER BY
    Profit DESC;