import discord
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
async def looking_user(ctx, interaction: discord.Interaction, voice_channel_1: discord.VoiceChannel = None, voice_channel_2: discord.VoiceChannel = None):
    user = ctx.author
    if user.voice and user.voice.channel and voice_channel_1 and voice_channel_2:
        voice_channel = user.voice.channel
        members = voice_channel.members
        print(members)
        member_names = [member.name for member in members]
        print(member_names)


    else:
        await interaction.response.send_message('No member specified.')

def Embed(member_names, voice_channel_1, voice_channel_2):
    embed = discord.Embed(title="Welcome to discord fight 5v5", description="Kapitans, peak players", color=discord.Color.purple())
    embed.set_thumbnail(url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSRh6UJMDoGniGMJrj_UHk9fGlbSH0o8XR71w&s')
    embed.set_author(name="5 V 5")
    embed.add_field(name=f'Capitan 1 - ', value=f'Players team 1: ')
    embed.add_field(name=f'Capitan 2 - ', value=f'Players team 2: ')
    embed.add_field(name=f'unpicked plauers: {member_names}')
        



bot.run('')
