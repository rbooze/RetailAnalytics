CREATE OR ALTER VIEW Analytics.vw_ExperimentCustomerDetail
AS

SELECT
    e.ExperimentID,
    e.CustomerID,
    e.GroupName,
    c.Segment,
    e.Purchased,
    e.PurchaseDate,
    e.Revenue,
    e.Profit,
    e.Returned,
    e.ReturnAmount
FROM Fact.CustomerExperiment e WITH (NOLOCK)
INNER JOIN Dim.Customer c WITH (NOLOCK)
    ON e.CustomerID = c.CustomerID;