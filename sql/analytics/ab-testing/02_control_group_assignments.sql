WITH EligibleCustomers AS
(
    SELECT
        c.CustomerID,

        ROW_NUMBER() OVER(
            ORDER BY NEWID()
        ) AS RandomOrder
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
        ) > 180
)

INSERT INTO Fact.CustomerExperiment
(
    ExperimentID,
    CustomerID,
    GroupName,
    PromotionID,
    StartDate,
    EndDate
)
SELECT
    1,
    CustomerID,

    CASE
        WHEN RandomOrder % 2 = 0
        THEN 'Treatment'
        ELSE 'Control'
    END,

    CASE
        WHEN RandomOrder % 2 = 0
        THEN 4
        ELSE NULL
    END,

    '2026-01-01',
    '2026-03-31'
FROM EligibleCustomers;

SELECT
    GroupName,
    COUNT(*) AS Customers
FROM Fact.CustomerExperiment
GROUP BY GroupName;