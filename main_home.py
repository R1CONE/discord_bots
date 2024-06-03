import discord
from discord.ext import commands
import random



bot = commands.Bot(command_prefix='-', intents=discord.Intents.all(), case_insensitive=True)

@bot.event
async def on_ready():
    print('Bot is ready')


@bot.command()
async def start(ctx, mod1: discord.Member, mod2: discord.Member):
    user = ctx.author
    if user.voice and user.voice.channel:
        voice_channel = user.voice.channel
        members = voice_channel.members
        member_names = [member.name for member in members]
        len_players = len(members)
        ctx.send(mod1, mod2)
        
        if(len_players > 12, len_players < 10):
            print(f"Number of users in voice channel: {len(members)}")
            print("User nicknames in the voice channel:")
            for name in member_names:
                print(name)
        else: 
            ctx.send("len players are > 12 or < 10")
            
            

        
    else:
        print("User is not in a voice channel")
        

        
@bot.command()
async def help_command(ctx):
    embed = discord.Embed(title="Help", description="this help for disassembly in using the bot", color=0x00ff00)
    embed.set_author(name="5 v 5 discord")
    embed.add_field(name="more text 2", value="Shows this help message", inline=False)
    
    embed.set_thumbnail(url='https://steamuserimages-a.akamaihd.net/ugc/1832417646113487031/C01A749B539CFF42C546C60BBF43E2C75ACCBD27/')
    
    # Add more fields here for other commands
    embed.add_field(name="text field 1", value="Description for text field 1", inline=False)
    embed.add_field(name="text field 2", value="Description for text field 2", inline=False)
    embed.set_footer(text="Bot developed by YourName")

    await ctx.send(embed=embed)
        

bot.run('')
