import discord
from discord import app_commands
from discord.ext import commands
import random

global voice_channel_1, voice_channel_2, kap
accepted_players = []
kap = 1  # Инициализация переменной kap
bot = commands.Bot(command_prefix='-', intents=discord.Intents.all())
bot.tracked_reactions = {}
bot.member_names_dict = {}
bot.voice_channels_dict = {}
emoji = ['1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣', '7️⃣', '8️⃣']

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
        members = voice_channel.members
        member_names = [member.name for member in members]

        if len(member_names) <= 10:
            await interaction.response.send_message(f'Members in voice channel: {", ".join(member_names)}')

            embed = discord.Embed(title="Welcome to discord fight 5v5", description="Get ready to start game!", color=discord.Color.purple())
            embed.set_thumbnail(url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSRh6UJMDoGniGMJrj_UHk9fGlbSH0o8XR71w&s')
            embed.set_author(name="5 V 5")
            embed.add_field(name='Accept your game!', value=f'{", ".join(f"@{name}" for name in member_names)}')
            
            message = await interaction.followup.send(embed=embed)
            await message.add_reaction('\u2705')
            
            bot.tracked_reactions[message.id] = message
            bot.member_names_dict[message.id] = member_names
            bot.voice_channels_dict[message.id] = (voice_channel_1, voice_channel_2)
        else:
            await interaction.response.send_message('Anti-abuse system')

    else:
        await interaction.response.send_message('You are not in a voice channel.')

@bot.event
async def on_reaction_add(reaction, user):
    if user.bot:
        return

    message = reaction.message
    if message.id in bot.tracked_reactions:
        if reaction.emoji == '\u2705':
            print(f'User {user.name} reacted with {reaction.emoji}')
            await message.channel.send(f'{user.mention} accepted the game!')
            if user.name not in accepted_players:
                accepted_players.append(user.name)
            
            print(f"Accepted players {len(accepted_players)}")
            
            member_names = bot.member_names_dict.get(message.id, [])
            voice_channel_1, voice_channel_2 = bot.voice_channels_dict.get(message.id, (None, None))

            if sorted(accepted_players) == sorted(member_names):
                await peaking_players(message, accepted_players, voice_channel_1, voice_channel_2)

async def peaking_players(message, accepted_players, voice_channel_1, voice_channel_2):
    kapitan_players = random.sample(accepted_players, 2)
    kapitan1_nickname, kapitan2_nickname = kapitan_players

    last_players = [player for player in accepted_players if player not in kapitan_players]
    list_com1, list_com2 = [], []

    unpeaked_players = {index: player for index, player in enumerate(last_players)}

    embed = discord.Embed(
        title="Welcome to discord fight",
        description="Let's start",
        color=discord.Color.purple()
    )
    embed.set_thumbnail(url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTvbwstNLPp77vL3VG5G3H6EVUt705BVF-sEQ&usqp=CAU')
    embed.set_author(name="discord battle")
    embed.add_field(name=f'Capitan 1 - @{kapitan1_nickname}', value=f'Players team 1: {list_com1}')
    embed.add_field(name=f'Capitan 2 - @{kapitan2_nickname}', value=f'Players team 2: {list_com2}')
    embed.add_field(name='Unpeaked players:', value='\n'.join(unpeaked_players.values()), inline=False)

    message = await message.channel.send(embed=embed)

    reactions_to_add = emoji[:len(last_players)]
    for reaction in reactions_to_add:
        await message.add_reaction(reaction)

    current_kapitan = kapitan1_nickname
    while unpeaked_players:
        def check(reaction, user):
            return (
                user.name == current_kapitan and
                str(reaction.emoji) in emoji and
                reaction.message.id == message.id
            )

        reaction, user = await bot.wait_for('reaction_add', check=check)
        emoji_index = emoji.index(str(reaction.emoji))

        if emoji_index not in unpeaked_players:
            await message.channel.send(f"Error: Invalid index {emoji_index}. Try again.")
            continue

        selected_player = unpeaked_players.pop(emoji_index)

        if current_kapitan == kapitan1_nickname:
            list_com1.append(selected_player)
            current_kapitan = kapitan2_nickname
        else:
            list_com2.append(selected_player)
            current_kapitan = kapitan1_nickname

        await message.clear_reaction(reaction.emoji)
        embed.clear_fields()
        embed.add_field(name=f'Capitan 1 - @{kapitan1_nickname}', value=f'Players team 1: {", ".join(list_com1)}')
        embed.add_field(name=f'Capitan 2 - @{kapitan2_nickname}', value=f'Players team 2: {", ".join(list_com2)}')
        embed.add_field(name='Unpeaked players:', value='\n'.join(unpeaked_players.values()) if unpeaked_players else 'All players have been picked', inline=False)
        await message.edit(embed=embed)
        
bot.run('MTExMjQtYHbLWYB5Fz6-18QpG5h0')
