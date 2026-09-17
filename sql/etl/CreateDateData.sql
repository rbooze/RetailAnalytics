DECLARE @StartDate DATE = '2022-01-01';
DECLARE @EndDate DATE = '2026-12-31';


WHILE @StartDate <= @EndDate
BEGIN
    INSERT INTO warehouse.DimDate
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

    VALUES
    (
        CONVERT(INT, FORMAT(@StartDate,'yyyyMMdd')),
        @StartDate,
        YEAR(@StartDate),
        DATEPART(QUARTER,@StartDate),
        MONTH(@StartDate),
        DATENAME(MONTH,@StartDate),
        DAY(@StartDate),
        DATENAME(WEEKDAY,@StartDate)
    );

    SET @StartDate = DATEADD(DAY,1,@StartDate);
END;