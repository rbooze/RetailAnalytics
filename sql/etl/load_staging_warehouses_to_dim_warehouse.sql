INSERT INTO Dim.Warehouse
(
    WarehouseID,
    WarehouseName,
    Region,
    Capacity
)
SELECT
    WarehouseID,
    WarehouseName,
    Region,
    Capacity
FROM Staging.Warehouses;