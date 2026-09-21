IF OBJECT_ID('Staging.ExperimentResults') IS NOT NULL
    DROP TABLE Staging.ExperimentResults;
GO

CREATE TABLE Staging.ExperimentResults
(
    CustomerID      INT           NOT NULL,
    Purchased       BIT           NOT NULL,
    PurchaseDate    DATE          NULL,
    Revenue         DECIMAL(12,2) NOT NULL,
    Profit          DECIMAL(12,2) NOT NULL
);