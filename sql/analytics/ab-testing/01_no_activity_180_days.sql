SELECT
    c.CustomerID,
    MAX(d.FullDate) AS LastPurchaseDate,

    DATEDIFF(
        DAY,
        MAX(d.FullDate),
        '2026-12-31'
    ) AS DaysInactive
FROM Fact.Sales s WITH (NOLOCK)
JOIN Dim.Customer c WITH (NOLOCK)
    ON s.CustomerKey = c.CustomerKey
JOIN Dim.Date d WITH (NOLOCK)
    ON s.DateKey = d.DateKey
GROUP BY
    c.CustomerID
HAVING
    DATEDIFF(
        DAY,
        MAX(d.FullDate),
        '2026-12-31'
    ) > 180;