import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='-', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print('Bot is ready')
    synced = await bot.tree.sync()
    print(synced)
    print("Slash commands: " + str(len(synced)) + " commands")

@bot.tree.command(name="looking_user", description="Looking for discord user")
async def looking_user(ctx, interaction: discord.Interaction, capitan1: discord.Member = None, capitan2: discord.Member = None):
    user = ctx.author
    if user.voice and user.voice.channel and capitan1 and capitan2:
        await interaction.response.send_message(f'User1: {capitan1.name} User2: {capitan2.name}')
        voice_channel = user.voice.channel
        members = voice_channel.members
        member_names = [member.name for member in members]
        len_players = len(members)

        if len_players and member_names:
            embed = discord.Embed(title="Welcome to discord fight 5v5", description="Kapitans, peak players", color=discord.Color.purple())
            embed.set_thumbnail(url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSRh6UJMDoGniGMJrj_UHk9fGlbSH0o8XR71w&s')
            embed.set_author(name="5 V 5")
            embed.add_field(name=f'Capitan 1 - {capitan1}', value=f'Players team 1: ')
            embed.add_field(name=f'Capitan 2 - {capitan2}', value=f'Players team 2: ')
            embed.add_field(name=f'unpicked plauers: {member_names}')


    else:
        await interaction.response.send_message('No member specified.')

bot.run('')
