INSERT INTO Dim.Date
(
    DateKey,
    FullDate,
    Year,
    Quarter,
    Month,
    MonthName,
    Day,
    DayName
)
SELECT
    DateKey,
    FullDate,
    Year,
    Quarter,
    Month,
    MonthName,
    Day,
    DayName
FROM Staging.Dates;