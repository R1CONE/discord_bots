
import discord
from discord.ext import commands


bot = commands.Bot(command_prefix='-', intents=discord.Intents.all(), case_insensitive=True)

@bot.event
async def on_ready():
    print('Bot is ready')

@bot.command()
async def sum(ctx):
    user = ctx.author
    if user.voice and user.voice.channel:
        voice_channel = user.voice.channel
        members = voice_channel.members
        member_names = [member.name for member in members]
        len_players = len(members)

        print(f"Number of users in voice channel: {len(members)}")
        print("User nicknames in the voice channel:")
        for name in member_names:
            print(name)
            
        game(member_names, len_players)
    else:
        print("User is not in a voice channel")
        
def game(member_names, len_players):
    


client.run('')
