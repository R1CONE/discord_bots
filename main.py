import discord

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print('Бот готов')

client.run('')