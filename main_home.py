import discord
from discord.ext import commands
import random



bot = commands.Bot(command_prefix='-', intents=discord.Intents.all(), case_insensitive=True)

@bot.event
async def on_ready():
    print('Bot is ready')
    try:
        synced = await bot.tree.sync()
        print(f"synced {len(synced)} commands(s)")
    except Exception as e:
        print(e)


@bot.command()
async def start_game(ctx, kap1 = discord.member, kap2 = discord.member, moderator1 = discord.member, moderator2 = discord.member):
    user = ctx.author
    if user.voice and user.voice.channel:
        voice_channel = user.voice.channel
        members = voice_channel.members
        member_names = [member.name for member in members]
        len_players = len(members)
        
        # Для примера, выводим имена участников и их количество в текстовый канал
        await ctx.send(f'Игроки в голосовом канале: {", ".join(member_names)}')
        await ctx.send(f'Количество игроков: {len_players}')

        if(member_names, len_players):
            embed = discord.Embed(title="Добро пожаловать на фейсит", description="Капитаны, пикайте игроков", color=discord.Color.purple())
            embed.set_thumbnail(url={})
            embed.set_author(name="R1CONE faceit")
            embed.add_field(name=f'Капитан 1 - {} - {} ', value=f'Игроки команды 1: {}')
            embed.add_field(name=f'Капитан 2 - {} - {}', value=f'Игроки команды 2: {}')
        
    else:
        await ctx.send("Вы не находитесь в голосовом канале")
        

#part 2      
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
