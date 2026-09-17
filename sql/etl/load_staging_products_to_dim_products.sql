INSERT INTO Dim.Product
(
    ProductID,
    ProductName,
    Category,
    Subcategory,
    SupplierID,
    Cost,
    Price,
    ProductStatus
)
SELECT
    ProductID,
    ProductName,
    Category,
    Subcategory,
    SupplierID,
    Cost,
    Price,
    ProductStatus
FROM Staging.Products;
GO

SELECT COUNT(*) FROM Dim.Product;