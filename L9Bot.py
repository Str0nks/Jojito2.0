import discord
from discord import ChannelType

HATE_ID = {
    231089584128262144: '👎',
    830311589042454559: '👎',
    535459241478324254: '👎',
    205905040089546752: '👎🏿'
    }

class MyClient(discord.Client):
    async def on_ready(self):
        channels = self.get_all_channels()
        for channel in channels:
            if(channel.type == ChannelType.text):
                async for message in channel.history(limit=100):

                    if message.author.id in HATE_ID:
                        print(f"{message.author.name}: {HATE_ID[message.author.id]}")
                        await message.add_reaction(HATE_ID[message.author.id])


    async def on_message(self, message):
        if message.author.id in HATE_ID:
            print(f"{message.author.name}: {HATE_ID[message.author.id]}")
            await message.add_reaction(HATE_ID[message.author.id])

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('')