/*==========================================================
 Executive KPI Dashboard
 Blue Ridge Outfitters
==========================================================*/

SELECT
    COUNT(DISTINCT OrderID) AS TotalOrders,
    SUM(Quantity) AS UnitsSold,
    SUM(SalesAmount) AS TotalRevenue,
    SUM(CostAmount) AS TotalCost,
    SUM(ProfitAmount) AS TotalProfit,

    ROUND(
        100.0 * SUM(ProfitAmount) /
        NULLIF(SUM(SalesAmount),0),
        2
    ) AS ProfitMarginPct,

    ROUND(
        SUM(SalesAmount) /
        NULLIF(COUNT(DISTINCT OrderID),0),
        2
    ) AS AverageOrderValue

FROM Fact.Sales WITH (NOLOCK);