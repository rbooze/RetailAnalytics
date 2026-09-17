-- Customer
CREATE INDEX IX_DimCustomer_CustomerID
ON Dim.Customer(CustomerID);

-- Product
CREATE INDEX IX_DimProduct_ProductID
ON Dim.Product(ProductID);

-- Promotion
CREATE INDEX IX_DimPromotion_PromotionID
ON Dim.Promotion(PromotionID);

-- Channel
CREATE INDEX IX_DimChannel_ChannelID
ON Dim.Channel(ChannelID);

-- Warehouse
CREATE INDEX IX_DimWarehouse_WarehouseID
ON Dim.Warehouse(WarehouseID);

-- Date
CREATE INDEX IX_DimDate_DateKey
ON Dim.Date(DateKey);

CREATE INDEX IX_StagingSales_CustomerID
ON Staging.Sales(CustomerID);

CREATE INDEX IX_StagingSales_ProductID
ON Staging.Sales(ProductID);

CREATE INDEX IX_StagingSales_DateKey
ON Staging.Sales(DateKey);