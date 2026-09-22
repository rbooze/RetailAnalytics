USE RetailAnalyticsDW;
GO

--Add the column
ALTER TABLE Fact.CustomerExperiment
ADD PurchaseDateKey INT NULL;

--Populate it
UPDATE Fact.CustomerExperiment
SET PurchaseDateKey = CONVERT(INT, CONVERT(CHAR(8), PurchaseDate, 112));

--Add the foreign key
ALTER TABLE Fact.CustomerExperiment
ADD CONSTRAINT FK_CustomerExperiment_Date
FOREIGN KEY (PurchaseDateKey)
REFERENCES Dim.Date(DateKey);