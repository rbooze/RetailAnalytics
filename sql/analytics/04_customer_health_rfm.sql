SELECT
    c.CustomerID,
    c.FirstName,
    c.LastName,
    c.Segment,
    COUNT(DISTINCT s.OrderID) AS TotalOrders,
    SUM(s.SalesAmount) AS TotalRevenue,
    SUM(s.ProfitAmount) AS TotalProfit,
    MAX(d.FullDate) AS LastPurchaseDate,

    DATEDIFF(
        DAY,
        MAX(d.FullDate),
         '2026-12-31'
    ) AS DaysSinceLastPurchase
FROM Fact.Sales s WITH (NOLOCK)
INNER JOIN Dim.Customer c WITH (NOLOCK)
    ON s.CustomerKey = c.CustomerKey
INNER JOIN Dim.Date d WITH (NOLOCK)
	ON s.DateKey = d.DateKey
GROUP BY
    c.CustomerID,
    c.FirstName,
    c.LastName,
    c.Segment;