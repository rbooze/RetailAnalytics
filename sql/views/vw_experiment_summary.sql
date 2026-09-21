CREATE OR ALTER VIEW Analytics.vw_ExperimentSummary
AS

SELECT
    ExperimentID,
    GroupName,
    COUNT(*) AS Customers,
    SUM(CAST(Purchased AS INT)) AS Purchasers,
    CAST(SUM(CAST(Purchased AS INT)) * 1.0 / COUNT(*) AS DECIMAL(10,4)) AS PurchaseRate,
    SUM(Revenue) AS Revenue,
    SUM(Profit) AS Profit,
    CAST(SUM(Profit) * 1.0 / NULLIF(SUM(Revenue),0) * 100 AS DECIMAL(10,2)) AS ProfitMarginPct,
    CAST(SUM(Profit) * 1.0 / COUNT(*) AS DECIMAL(12,2)) AS ProfitPerCustomer
FROM Fact.CustomerExperiment
GROUP BY
    ExperimentID,
    GroupName;
