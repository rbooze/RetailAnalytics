ALTER TABLE Fact.CustomerExperiment
ADD
Purchased BIT,
PurchaseDate DATE,
Revenue DECIMAL(12,2),
Profit DECIMAL(12,2),
Returned BIT,
ReturnAmount DECIMAL(12,2);
