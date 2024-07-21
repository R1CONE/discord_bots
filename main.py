import discord
from discord import app_commands
from discord.ext import commands
import random


bot = commands.Bot(command_prefix='-', intents=discord.Intents.all())

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
        member_names = [member.name for member in members]  # list only with nicknames
        print(member_names)
        await interaction.response.send_message(f'Members in voice channel: {", ".join(member_names)}')

        embed = discord.Embed(title="Welcome to discord fight 5v5", description="Get ready to start game!", color=discord.Color.purple())
        embed.set_thumbnail(url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSRh6UJMDoGniGMJrj_UHk9fGlbSH0o8XR71w&s')
        embed.set_author(name="5 V 5")
        embed.add_field(name='Accept your game!', value=f'{", ".join(member_names)}')
        
        message = await interaction.followup.send(embed=embed)
        await message.add_reaction('\u2705')

        def check(reaction, user):
            return str(reaction.emoji) == '\u2705' and user in members and reaction.message.id == message.id

        reacted_members = set()
        while len(reacted_members) < len(members):
            reaction, user = await bot.wait_for('reaction_add', check=check)
            reacted_members.add(user)
        
        await start_game(interaction)

    elif not (voice_channel_1 and voice_channel_2):
        await interaction.response.send_message('Both voice channels must be specified.')

    else:
        await interaction.response.send_message('You are not in a voice channel.')

async def start_game(interaction):
    await interaction.followup.send('Go ahead')

bot.run('MTExNDU4NzQ4')
