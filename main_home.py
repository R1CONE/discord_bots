import discord
from discord import app_commands
from discord.ext import commands
import random


bot = commands.Bot(command_prefix='-', intents=discord.Intents.all())
bot.tracked_reactions = {}
bot.member_names_dict = {}

@bot.event
async def on_ready():
    print('Bot is ready')
    synced = await bot.tree.sync()
    print(synced)
    print("Slash commands: " + str(len(synced)) + " commands")

@bot.tree.command(name="looking_user", description="Looking for discord user")
@app_commands.describe(voice_channel_1="First voice channel", voice_channel_2="Second voice channel")
async def looking_user(interaction: discord.Interaction, voice_channel_1: discord.VoiceChannel = None, voice_channel_2: discord.VoiceChannel = None):
    user = interaction.user
    if user.voice and user.voice.channel and voice_channel_1 and voice_channel_2:
        voice_channel = user.voice.channel
        members = voice_channel.members  # list with full information about everyone
        print(members)
        member_names = [member.name for member in members]

        if len(member_names) == 1:
            await interaction.response.send_message(f'Members in voice channel: {", ".join(member_names)}')

            embed = discord.Embed(title="Welcome to discord fight 5v5", description="Get ready to start game!", color=discord.Color.purple())
            embed.set_thumbnail(url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSRh6UJMDoGniGMJrj_UHk9fGlbSH0o8XR71w&s')
            embed.set_author(name="5 V 5")
            embed.add_field(name='Accept your game!', value=f'{", ".join(member_names)}')
        
            message = await interaction.followup.send(embed=embed)
            await message.add_reaction('\u2705')
            bot.tracked_reactions[message.id] = message
            bot.member_names_dict[message.id] = member_names 

        
        else:
            await interaction.response.send_message('Anti-abuse system')

        
    else:
        await interaction.response.send_message('You are not in a voice channel.')

@bot.event
async def on_reaction_add(reaction, user):
    message = reaction.message
    if message.id in bot.tracked_reactions:
        if reaction.emoji == '\u2705':  # Проверяем, что это нужная реакция
            print(f'User {user.name} reacted with {reaction.emoji}') ##nickname only
            await message.channel.send(f'{user.mention} accepted the game!')
            ##print(user.mention) user discord id only 
            accepted_players = []
            accepted_players.append(user.name)

            member_names = bot.member_names_dict.get(message.id, [])

            if sorted(accepted_players) == sorted(member_names):
                peaking_players(accepted_players)

def peaking_players(accepted_players):
    kapitan_players = []
    kapitan_players = random.sample(accepted_players, 2)
    last_players = [player for player in accepted_players if player not in kapitan_players]

    




bot.run('')
