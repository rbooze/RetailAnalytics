INSERT INTO Dim.Supplier
(
    SupplierID,
    SupplierName,
    Country,
    SupplierTier,
    LeadTimeDays,
    QualityScore,
    RiskLevel
)
SELECT
    SupplierID,
    SupplierName,
    Country,
    SupplierTier,
    LeadTimeDays,
    QualityScore,
    RiskLevel
FROM Staging.Suppliers;
GO

SELECT COUNT(*)
FROM Dim.Supplier;