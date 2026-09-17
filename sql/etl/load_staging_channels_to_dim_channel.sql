INSERT INTO Dim.Channel
(
    ChannelID,
    ChannelName
)
SELECT
    ChannelID,
    ChannelName
FROM Staging.Channels;