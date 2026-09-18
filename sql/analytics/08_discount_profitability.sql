SELECT
    CASE
        WHEN s.DiscountAmount > 0 THEN 'Discount Customer'
        ELSE 'Full Price Customer'
    END AS CustomerType,

    COUNT(DISTINCT c.CustomerID) AS Customers,

    COUNT(DISTINCT s.OrderID) AS Orders,

    SUM(s.SalesAmount) AS Revenue,

    SUM(s.ProfitAmount) AS Profit,

    ROUND(
        SUM(s.ProfitAmount) /
        COUNT(DISTINCT c.CustomerID),
        2
    ) AS ProfitPerCustomer,

    ROUND(
        100.0 * SUM(s.ProfitAmount) /
        NULLIF(SUM(s.SalesAmount),0),
        2
    ) AS ProfitMarginPct
FROM Fact.Sales s WITH (NOLOCK)

JOIN Dim.Customer c WITH (NOLOCK)
    ON s.CustomerKey = c.CustomerKey

GROUP BY
    CASE
        WHEN s.DiscountAmount > 0 THEN 'Discount Customer'
        ELSE 'Full Price Customer'
    END;