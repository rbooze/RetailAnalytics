INSERT INTO Dim.Promotion
(
    PromotionID,
    CampaignName,
    CampaignType,
    DiscountPercent,
    TestGroup,
    TargetSegment,
    CategoryTarget
)
SELECT
    PromotionID,
    CampaignName,
    CampaignType,
    DiscountPercent,
    TestGroup,
    TargetSegment,
    CategoryTarget
FROM Staging.Promotions;