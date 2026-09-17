import pandas as pd

channels = [
    {
        "ChannelID":1,
        "ChannelName":"Retail Store"
    },

    {
        "ChannelID":2,
        "ChannelName":"Website"
    },

    {
        "ChannelID":3,
        "ChannelName":"Mobile App"
    }
]

df = pd.DataFrame(channels)

df.to_csv(
    "C:/Projects/RetailAnalytics/data/raw/channels.csv",
    index=False
)

print("Channels generated")