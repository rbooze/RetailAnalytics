import pandas as pd

dates = pd.date_range(
    start="2022-01-01",
    end="2026-12-31",
    freq="D"
)

df = pd.DataFrame({
    "DateKey":
        dates.strftime("%Y%m%d").astype(int),

    "FullDate":
        dates,

    "Year":
        dates.year,

    "Month":
        dates.month,

    "Quarter":
        dates.quarter,

    "MonthName":
        dates.month_name(),

    "Day":
        dates.day,

    "DayName":
        dates.day_name()
})

df.to_csv(
    "C:/Projects/RetailAnalytics/data/raw/dates.csv",
    index=False
)

print(
    f"Created {len(df)} dates"
)