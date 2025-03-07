import discord
from discord import app_commands
from discord.ext import commands
import pymysql
import random

global voice_channel_1, voice_channel_2, kap
accepted_players = []
kap = 1  # Инициализация переменной kap
bot = commands.Bot(command_prefix='-', intents=discord.Intents.all())
bot.tracked_reactions = {}
bot.member_names_dict = {}
bot.voice_channels_dict = {}
server_activation_status = {}  # Словарь для отслеживания статуса активации по серверам
emoji = ['\u0031\uFE0F\u20E3', '\u0032\uFE0F\u20E3', '\u0033\uFE0F\u20E3', '\u0034\uFE0F\u20E3', '\u0035\uFE0F\u20E3', '\u0036\uFE0F\u20E3', '\u0037\uFE0F\u20E3', '\u0038\uFE0F\u20E3']

try:
    # Nawiązywanie połączenia z bazą danych
    connection = pymysql.connect(host='localhost', user='root',
                                 password='', database='dis_faceit')

except Exception as e:
    print(f"Error connecting to database: {e}")

@bot.event
async def on_ready():
    print('Bot is ready')
    synced = await bot.tree.sync()
    print(synced)
    print("Slash commands: " + str(len(synced)) + " commands")
    

@bot.tree.command(name="looking_user", description="Looking for discord user")
@app_commands.describe(voice_channel_1="First voice channel", voice_channel_2="Second voice channel")
async def looking_user(interaction: discord.Interaction, voice_channel_1: discord.VoiceChannel = None, voice_channel_2: discord.VoiceChannel = None):
    server_name = interaction.guild.name
    normal_server_name = server_name.replace(" ", "_")

    history_server_name = normal_server_name + "_history"

    try:
        with connection.cursor() as cursor:
            # SQL-запрос для создания таблицы
            sql = f"""
            CREATE TABLE IF NOT EXISTS `{normal_server_name}` (
                id INT AUTO_INCREMENT PRIMARY KEY,
                user_id VARCHAR(255) NOT NULL,
                user_name VARCHAR(255) NOT NULL,
                mmr INT NOT NULL,
                join_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
            """
            cursor.execute(sql)
            connection.commit()
            print(f"Table `{server_name}` checked/created successfully.")


    except Exception as e:
        print(f"Error creating table `{history_server_name}`: {e}")

    try:
        with connection.cursor() as cursor:
            # SQL-запрос для создания таблицы
            sql = f"""
            CREATE TABLE IF NOT EXISTS `{history_server_name}` (
                id_of_game VARCHAR(255)  PRIMARY KEY,
                id_player_1_team_1 VARCHAR(255),
                id_player_2_team_1 VARCHAR(255),
                id_player_3_team_1 VARCHAR(255),
                id_player_4_team_1 VARCHAR(255),
                id_player_5_team_1 VARCHAR(255),
                id_player_1_team_2 VARCHAR(255),
                id_player_2_team_2 VARCHAR(255),
                id_player_3_team_2 VARCHAR(255),
                id_player_4_team_2 VARCHAR(255),
                id_player_5_team_2 VARCHAR(255),
                game_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
            """
            cursor.execute(sql)
            connection.commit()
            print(f"Table `{server_name}` checked/created successfully.")


    except Exception as e:
        print(f"Error creating table `{server_name}`: {e}")
    
    if interaction.user.voice and interaction.user.voice.channel:

        accepted_players.clear()
 
        voice_channel = interaction.user.voice.channel
        members = voice_channel.members
        member_names = [member.name for member in members]
        guild_id = interaction.guild.id
        server_name = interaction.guild.name
        normal_server_name = server_name.replace(" ", "_")
        history_server_name = normal_server_name + "_history"

        


        if voice_channel_1 and voice_channel_2:
            if 4 <= len(member_names) <= 10:
                await interaction.response.send_message(f'Members in voice channel: {", ".join(member_names)}')

                embed = discord.Embed(
                    title="Welcome to discord fight 5v5",
                    description="Get ready to start game!",
                    color=discord.Color.purple()
                )
                embed.set_thumbnail(url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSRh6UJMDoGniGMJrj_UHk9fGlbSH0o8XR71w&s')
                embed.set_author(name="5 V 5")
                embed.add_field(name='Accept your game!', value=f'{", ".join(f"@{name}" for name in member_names)}')

                message = await interaction.followup.send(embed=embed)
                await message.add_reaction('\u2705')

                bot.tracked_reactions[message.id] = message
                bot.member_names_dict[message.id] = member_names
                bot.voice_channels_dict[message.id] = (voice_channel_1, voice_channel_2)

                



            else:
                await interaction.response.send_message('Count of players must be between 4 and 10.')
        else:
            await interaction.response.send_message('Both voice channels must be specified.')

    else:
        await interaction.response.send_message('You are not in a voice channel.')

    
@bot.tree.command(name="start", description="Start the bot and display basic information")
async def start_command(interaction: discord.Interaction):
    server_name = interaction.guild.name  # Получаем имя гильдии
    guild_id = interaction.guild.id  # Получаем ID текущей гильдии
    server_activation_status[guild_id] = True  # Активируем бота для этой гильдии

    embed = discord.Embed(
        title="Welcome to the Discord Battle Bot!",
        description=(
            "Use the available commands to organize voice channel games and battles:\n"
            "- `/looking_user`: Search for users in voice channels to start a game.\n"
            "- `/start`: Display this information.\n\n"
            "Let the games begin!"
        ),
        color=discord.Color.blue()
    )
    embed.set_thumbnail(
        url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTvbwstNLPp77vL3VG5G3H6EVUt705BVF-sEQ&usqp=CAU"
    )
    embed.set_footer(text="Enjoy the game!")

    await interaction.response.send_message(embed=embed)
    

    

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

            if len(accepted_players) == len(member_names):
                if all(player in member_names for player in accepted_players):
                    await peaking_players( message, accepted_players, voice_channel_1, voice_channel_2)
                    accepted_players.clear()

async def peaking_players(message, accepted_players, voice_channel_1, voice_channel_2):

    
    kapitan_players = random.sample(accepted_players, 2)
    kapitan1_nickname, kapitan2_nickname = kapitan_players

    server_name = message.guild.name
    normal_server_name = server_name.replace(" ", "_")
    history_server_name = normal_server_name + "_history"

    last_players = [player for player in accepted_players if player not in kapitan_players]
    list_com1, list_com2 = [], []
    current_kapitan = kapitan1_nickname
    unpeaked_players = {index: player for index, player in enumerate(last_players)}

    embed = discord.Embed(
        title="Welcome to discord fight",
        description= f"Now is peaking {current_kapitan}",
        color=discord.Color.purple()
    )
    embed.set_thumbnail(url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTvbwstNLPp77vL3VG5G3H6EVUt705BVF-sEQ&usqp=CAU')
    embed.set_author(name="discord battle")
    embed.add_field(name=f'Capitan 1 - @{kapitan1_nickname}', value=f'Players team 1: {list_com1}')
    embed.add_field(name=f'Capitan 2 - @{kapitan2_nickname}', value=f'Players team 2: {list_com2}')
    embed.add_field(
    name='Unpeaked players:', 
    value='\n'.join([f"{player} - {(index + 1)}" for index, player in unpeaked_players.items()]) if unpeaked_players else 'All players have been picked', 
    inline=False
)

    message = await message.channel.send(embed=embed)

    reactions_to_add = emoji[:len(last_players)]
    for reaction in reactions_to_add:
        await message.add_reaction(reaction)

    
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
        embed.description= f"Now is peaking {current_kapitan}"
        embed.add_field(name=f'Capitan 1 - @{kapitan1_nickname}', value=f'Players team 1: {", ".join(list_com1)}')
        embed.add_field(name=f'Capitan 2 - @{kapitan2_nickname}', value=f'Players team 2: {", ".join(list_com2)}')
        embed.add_field(
    name='Unpeaked players:', 
    value='\n'.join([f"{player} - {(index + 1)}" for index, player in unpeaked_players.items()]) if unpeaked_players else 'All players have been picked', 
    inline=False
)
        await message.edit(embed=embed)

    nicknames_team1 = list_com1 + [kapitan1_nickname]
    nicknames_team2 = list_com2 + [kapitan2_nickname]

    guild = message.guild  # Добавлено
    
    print(nicknames_team1)
    print(nicknames_team2)

    team1_ids = [member.id for member in guild.members if member.name in nicknames_team1]
    team2_ids = [member.id for member in guild.members if member.name in nicknames_team2]

    print(team1_ids)
    print(team2_ids)

    
    for el1 in list_com1:
        member = discord.utils.get(message.guild.members, name=el1)
        await member.move_to(voice_channel_1)
        captain1 = message.guild.get_member_named(kapitan1_nickname)

    if captain1:
        await captain1.move_to(voice_channel_1)
        
    
    for el2 in list_com2:
        member = discord.utils.get(message.guild.members, name=el2)
        await member.move_to(voice_channel_2)
        
        captain2 = message.guild.get_member_named(kapitan2_nickname)

    if captain2:
        await captain2.move_to(voice_channel_2)
        

    


    game_id = ''.join(random.choices("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", k=20))
    
    try:
        with connection.cursor() as cursor:
            sql_insert = f"INSERT INTO {history_server_name} (id_of_game) VALUES (%s);"
            cursor.execute(sql_insert, (game_id,))
            connection.commit()
    except Exception as e:
        print(f"Error inserting game ID: {e}")

    try:
        with connection.cursor() as cursor:
            sql_update = f"UPDATE {history_server_name} SET id_player_1_team_1 = %s WHERE id_of_game = %s;"
            cursor.execute(sql_update, (team1_ids[0], game_id))
            connection.commit()
    except Exception as e:
        print(f"Error: {e}")

    
    embed.title = "Game is ready!"
    embed.description = "Here are your teams:"
    await message.channel.send(embed=embed)
    
bot.run('MTMyNDA3OT5IzVu-HBIZE')
