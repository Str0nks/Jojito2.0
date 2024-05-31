import discord
from discord import ChannelType
# local import
import config
import random

WHITELIST = [195286013109600256, 248516720493330432]


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
        if message.author.id != 1245830858921738280:
            if message.author.id in WHITELIST:
                if(random.randint(0,100)==69):
                    await message.reply('correct')
            if message.author.id in HATE_ID:
                if(random.randint(0,100)==69):
                    await message.reply('wrong')

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
token = config.get_token()
client.run(token)
