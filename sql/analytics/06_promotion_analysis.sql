SELECT
    p.CampaignName,
    p.CampaignType,
    p.DiscountPercent,

    COUNT(DISTINCT s.OrderID) AS Orders,

    SUM(s.SalesAmount) AS Revenue,

    SUM(s.DiscountAmount) AS TotalDiscount,

    SUM(s.ProfitAmount) AS Profit,

    ROUND(
        100.0 * SUM(s.ProfitAmount) /
        NULLIF(SUM(s.SalesAmount), 0),
        2
    ) AS ProfitMarginPct,

    ROUND(
        AVG(s.SalesAmount),
        2
    ) AS AvgSaleAmount
FROM Fact.Sales s WITH (NOLOCK)
JOIN Dim.Promotion p WITH (NOLOCK)
    ON s.PromotionKey = p.PromotionKey
GROUP BY
    p.CampaignName,
    p.CampaignType,
    p.DiscountPercent
ORDER BY
    p.DiscountPercent;

/*
While analyzing promotion effectiveness, I noticed discount levels had almost no relationship with revenue or margin. I performed data validation and identified that the simulated promotion behavior 
lacked differentiation. I would improve the model by introducing customer price sensitivity and promotion response curves.

Promotions appear to maintain profitability across discount levels. I would recommend testing targeted promotions for at-risk customers rather than increasing promotions broadly. We should measure 
whether promotional offers improve retention, repeat purchases, and customer lifetime value.
*/