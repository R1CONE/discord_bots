import discord
from discord import app_commands
from discord.ext import commands
import random

global voice_channel_1, voice_channel_2, kap
accepted_players = []
kap = 1  # Инициализация переменной kap
intents = discord.Intents.all()  # Включаем все intents
intents.message_content = True  # Разрешаем чтение содержимого сообщений
intents.reactions = True  # Разрешаем обработку реакций
bot = commands.Bot(command_prefix='-', intents=intents)
bot.tracked_reactions = {}
bot.member_names_dict = {}
bot.voice_channels_dict = {}
emoji = ['\u0031\uFE0F\u20E3', '\u0032\uFE0F\u20E3', '\u0033\uFE0F\u20E3', '\u0034\uFE0F\u20E3', '\u0035\uFE0F\u20E3', '\u0036\uFE0F\u20E3', '\u0037\uFE0F\u20E3', '\u0038\uFE0F\u20E3']

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

        if 4 <= len(member_names) <= 10:
            await interaction.response.send_message(f'Members in voice channel: {", ".join(member_names)}')

            embed = discord.Embed(title="Welcome to discord fight 5v5", description="Get ready to start game!", color=discord.Color.purple())
            embed.set_thumbnail(url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSRh6UJMDoGniGMJrj_UHk9fGlbSH0o8XR71w&s')
            embed.set_author(name="5 V 5")
            embed.add_field(name='Accept your game!', value=f'{", ".join(f"@{name}" for name in member_names)}')
        
            message = await interaction.followup.send(embed=embed)
            await message.add_reaction('\u2705')
            
            # Сохраняем данные каналов в словарь
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
        if reaction.emoji == '\u2705':  # Проверяем, что это нужная реакция
            print(f'User {user.name} reacted with {reaction.emoji}')  # nickname only
            await message.channel.send(f'{user.mention} accepted the game!')
            # Проверяем, есть ли пользователь уже в списке
            if user.name not in accepted_players:
                accepted_players.append(user.name)
            
            print(f"accepted players {len(accepted_players)}")
            
            member_names = bot.member_names_dict.get(message.id, [])
            voice_channel_1, voice_channel_2 = bot.voice_channels_dict.get(message.id, (None, None))

            print(sorted(member_names))
            print(sorted(accepted_players))

            # Если все игроки приняли, вызываем peaking_players
            if sorted(accepted_players) == sorted(member_names):
                await peaking_players(message, user, accepted_players, voice_channel_1, voice_channel_2)

async def peaking_players(message, user, accepted_players, voice_channel_1, voice_channel_2, interaction: discord.Interaction = None):
    # Функционал команды, когда все игроки приняли участие
    await message.channel.send("Starting the game!")

    global kap
    kapitan_players = random.sample(accepted_players, 2)
    kapitan1_nickname = kapitan_players[0]
    kapitan2_nickname = kapitan_players[1]

    last_players = [player for player in accepted_players if player not in kapitan_players]
    list_com1 = []
    list_com2 = []

    embed = discord.Embed(
        title="Welcome to discord fight",
        description="Let's start",
        color=discord.Color.purple()
    )
    embed.set_thumbnail(url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTvbwstNLPp77vL3VG5G3H6EVUt705BVF-sEQ&usqp=CAU')
    embed.set_author(name="discord battle")
    embed.add_field(name=f'Capitan 1 - @{kapitan1_nickname}', value=f'Players team 1: {list_com1}')
    embed.add_field(name=f'Capitan 2 - @{kapitan2_nickname}', value=f'Players team 2: {list_com2}')
    embed.add_field(name='Unpeaked players:', value='\n'.join(last_players), inline=False)

    message = await message.channel.send(embed=embed)

    reactions_to_add = emoji[:len(last_players)]
    for reaction in reactions_to_add:
        await message.add_reaction(reaction)

    curent_kapitan = kapitan1_nickname if kap == 1 else kapitan2_nickname

    if kap == 1 and user.name == kapitan1_nickname or kap == 2 and user.name == kapitan2_nickname:
        if str(reaction) in emoji:
            emoji_index = emoji.index(str(reaction))
            selected_player = last_players[emoji_index]
            if selected_player in list_com1 or selected_player in list_com2:
                await message.channel.send(f'Player {selected_player} is already in another team')
            else:
                last_players.remove(selected_player)
                (list_com1 if kap == 1 else list_com2).append(selected_player)

                embed.set_field_at(0, name=f"Captain 1: {kapitan1_nickname}", value=f"Players: {', '.join(list_com1)}")
                embed.set_field_at(1, name=f"Captain 2: {kapitan2_nickname}", value=f"Players: {', '.join(list_com2)}")
                embed.set_field_at(2, name="Unpicked Players", value="\n".join(last_players) if last_players else "All players have been picked", inline=False)
                embed.description = f"Now choosing: {curent_kapitan}"
                await message.edit(embed=embed)
                await message.remove_reaction(reaction, user)

                kap = 2 if kap == 1 else 1
        else:
            await message.channel.send(f'Wrong emoji')

    if not last_players:
        for el1 in list_com1:    
            member = discord.utils.get(message.guild.members, name=el1)
            if member:
                await member.move_to(voice_channel_1)
        await message.guild.get_member_named(kapitan1_nickname).move_to(voice_channel_1)

        for el2 in list_com2:    
            member = discord.utils.get(message.guild.members, name=el2)
            if member:
                await member.move_to(voice_channel_2)
        await message.guild.get_member_named(kapitan2_nickname).move_to(voice_channel_2)

        embed = discord.Embed(title="Game is ready!", description="Here are your teams:", color=discord.Color.purple())
        embed.set_thumbnail(url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTvbwstNLPp77vL3VG5G3H6EVUt705BVF-sEQ&usqp=CAU')
        embed.set_author(name="discord battle")
        embed.add_field(name=f'Capitan 1 - @{kapitan1_nickname}', value=f'Players team 1: {", ".join(list_com1)}')
        embed.add_field(name=f'Capitan 2 - @{kapitan2_nickname}', value=f'Players team 2: {", ".join(list_com2)}')
        await message.channel.send(embed=embed)

