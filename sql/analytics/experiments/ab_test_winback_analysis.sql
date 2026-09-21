/*
    A/B Test:
    Win-back Promotion

    Measures:
    - Customers
    - Purchases
    - Conversion Rate
    - Revenue
    - Profit
    - Margin
*/

DECLARE @ExperimentID INT = 1;

SELECT
    GroupName,
    COUNT(*) AS Customers,
    SUM(CAST(Purchased AS INT)) AS Purchasers,

    CAST(
        SUM(CAST(Purchased AS INT)) * 1.0 / COUNT(*)
        AS DECIMAL(10,4)
    ) AS PurchaseRate,

    SUM(Revenue) AS Revenue,
    SUM(Profit) AS Profit,

    CAST(
        SUM(Profit) * 1.0 / NULLIF(SUM(Revenue),0) * 100 AS DECIMAL(10,2)) AS ProfitMarginPct,

    CAST(SUM(Profit) * 1.0 / COUNT(*) AS DECIMAL(10,2)) AS ProfitPerCustomer

FROM Fact.CustomerExperiment
WHERE 
	ExperimentID = @ExperimentID
GROUP BY
    GroupName;

--===============================================================

WITH ExperimentSummary AS
(
    SELECT
        GroupName,
        COUNT(*) AS Customers,
        SUM(CAST(Purchased AS INT)) AS Purchasers,
        SUM(Revenue) AS Revenue,
        SUM(Profit) AS Profit
    FROM Fact.CustomerExperiment
    WHERE 
		ExperimentID = 1
    GROUP BY 
		GroupName
)

SELECT
    'Purchase Rate Lift' AS Metric,
    CAST((Treatment.Purchasers * 1.0 / Treatment.Customers) - (Control.Purchasers * 1.0 / Control.Customers) AS DECIMAL(10,4)) AS Lift
FROM ExperimentSummary Treatment
CROSS JOIN ExperimentSummary Control
WHERE 
	Treatment.GroupName = 'Treatment'
	AND Control.GroupName = 'Control';