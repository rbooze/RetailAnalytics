ALTER TABLE Fact.Sales
ADD CONSTRAINT FK_FactSales_Customer
FOREIGN KEY (CustomerKey)
REFERENCES Dim.Customer(CustomerKey);