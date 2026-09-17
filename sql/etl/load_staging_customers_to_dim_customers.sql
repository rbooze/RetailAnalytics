INSERT INTO Dim.Customer
(
    CustomerID,
    FirstName,
    LastName,
    State,
    Segment,
    JoinDate
)
SELECT
    CustomerID,
    FirstName,
    LastName,
    State,
    Segment,
    JoinDate
FROM Staging.Customers;
GO

SELECT COUNT(*) FROM Dim.Customer;