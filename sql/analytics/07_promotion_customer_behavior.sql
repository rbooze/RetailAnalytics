SELECT
    c.Segment,

    CASE
        WHEN s.DiscountAmount > 0 THEN 'Discount Customer'
        ELSE 'Full Price Customer'
    END AS CustomerType,

    COUNT(DISTINCT c.CustomerID) AS Customers,

    COUNT(DISTINCT s.OrderID) AS Orders,

    SUM(s.SalesAmount) AS Revenue,

    SUM(s.ProfitAmount) AS Profit,

    ROUND(
        SUM(s.SalesAmount) /
        COUNT(DISTINCT c.CustomerID),
        2
    ) AS RevenuePerCustomer
FROM Fact.Sales s WITH (NOLOCK)
JOIN Dim.Customer c WITH (NOLOCK)
    ON s.CustomerKey = c.CustomerKey
GROUP BY
    c.Segment,

    CASE
        WHEN s.DiscountAmount > 0 THEN 'Discount Customer'
        ELSE 'Full Price Customer'
    END
ORDER BY
    c.Segment,
    CustomerType;

/*
Promotions appear effective at generating sales volume, but discounted customers have lower revenue per customer across all segments. Rather than increasing broad promotions, I would target promotions toward at-risk or inactive customers and measure whether the incremental purchases 
offset the margin impact.
*/