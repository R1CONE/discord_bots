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

        if len(member_names) == 4:
            await interaction.response.send_message(f'Members in voice channel: {", ".join(member_names)}')

            embed = discord.Embed(title="Welcome to discord fight 5v5", description="Get ready to start game!", color=discord.Color.purple())
            embed.set_thumbnail(url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSRh6UJMDoGniGMJrj_UHk9fGlbSH0o8XR71w&s')
            embed.set_author(name="5 V 5")
            embed.add_field(name='Accept your game!', value=f'{", ".join(member_names)}')
        
            message = await interaction.followup.send(embed=embed)
            await message.add_reaction('\u2705') #\u0031\uFE0F\u20E3 #\u2705
            
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
                await peaking_players(message.channel.id, user, message.channel, accepted_players, voice_channel_1, voice_channel_2)
                

async def peaking_players(text_channel_id, user, channel, accepted_players, voice_channel_1, voice_channel_2):
    emoji = ['\u0031\uFE0F\u20E3', '\u0032\uFE0F\u20E3', '\u0033\uFE0F\u20E3', '\u0034\uFE0F\u20E3', '\u0035\uFE0F\u20E3', '\u0036\uFE0F\u20E3', '\u0037\uFE0F\u20E3', '\u0038\uFE0F\u20E3']
    global kap

    kapitan_players = random.sample(accepted_players, 2)
    kapitan1_nickname = kapitan_players[0]
    kapitan2_nickname = kapitan_players[1]

    last_players = [player for player in accepted_players if player not in kapitan_players]
    list_com1 = []
    list_com2 = []

    embed = discord.Embed(title="Welcome to discord fight", description="Let's start", color=discord.Color.purple())
    embed.set_thumbnail(url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTvbwstNLPp77vL3VG5G3H6EVUt705BVF-sEQ&usqp=CAU')
    embed.set_author(name="discord battle")
    embed.add_field(name=f'Capitan 1 - {kapitan1_nickname}', value=f'Players team 1: {list_com1}')
    embed.add_field(name=f'Capitan 2 - {kapitan2_nickname}', value=f'Players team 2: {list_com2}')

    if last_players:
        embed.add_field(name='Unpicked players:', value='\n'.join([f'{i + 1} - {last_players[i]}' for i in range(len(last_players))]), inline=False)

    await channel.send(embed=embed)
    
    if user.id == kapitan1_nickname:
        if kap == 1:
            if str(reaction) in emoji:
                emoji_index = emoji.index(str(reaction))

                selected_player = last_players[emoji_index]
                
                if selected_player in list_com2:
                    await channel.send(f'Player {selected_player} in other team')
                else:
                    await channel.send(f'Capitan 1 picked {selected_player} to team 1')
                    if selected_player in last_players:
                        last_players.remove(selected_player)
                    
                    list_com1.append(selected_player)
                    
                    new_embed = discord.Embed(title="Peaking second capitan", description="Capitan, pick players", color=discord.Color.purple())
                    new_embed.set_thumbnail(url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTvbwstNLPp77vL3VG5G3H6EVUt705BVF-sEQ&usqp=CAU')
                    new_embed.set_author(name="discord battle")
                    
                    new_embed.add_field(name=f'Capitan 1 - {kapitan1_nickname}', value= f'Players team 1: {list_com1}')
                    new_embed.add_field(name=f'Capitan 2 - {kapitan2_nickname}', value= f'Players team 2: {list_com2}')

                    if last_players:
                        new_embed.add_field(name='Unpicked players:', value='\n'.join([f'{i + 1} - {last_players[i]}' for i in range(len(last_players))]), inline=False)
                    else:
                        new_embed.add_field(name='Ready!!', value='Good luck, have fun!', inline=False)
    
                    new_embed.set_footer(text="To pick a player, click on the emoji of his number")

                    message = await channel.send(embed=new_embed)

                    reactions_to_add = emoji[len(last_players)]
                    for reaction in reactions_to_add:
                        await message.add_reaction(reaction)
                        
                    kap = 2
                    
            else:
                await channel.send(f'Player {selected_player} in other team')
        elif kap == 2:
            await channel.send(f'Now is peaking another capitan')


    if user.id == kapitan2_nickname:
        if kap == 2:
            if str(reaction) in emoji:
                emoji_index = emoji.index(str(reaction))

                selected_player = last_players[emoji_index]
                
                if selected_player in list_com1:
                    await channel.send(f'Player {selected_player} in other team')
                else:
                    await channel.send(f'Capitan 2 picked {selected_player} to team 2')
                    if selected_player in last_players:
                        last_players.remove(selected_player)

                    list_com2.append(selected_player)
                    
                    new_embed = discord.Embed(title="Peaking second capitan", description="Capitan, pick players", color=discord.Color.purple())
                    new_embed.set_thumbnail(url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTvbwstNLPp77vL3VG5G3H6EVUt705BVF-sEQ&usqp=CAU')
                    new_embed.set_author(name="discord battle")
                    new_embed.add_field(name=f'Capitan 1 - {kapitan1_nickname}', value= f'Players team 1: {list_com1}')
                    new_embed.add_field(name=f'Capitan 2 - {kapitan2_nickname}', value= f'Players team 2: {list_com2}')

                    if last_players:
                        new_embed.add_field(name='Unpicked players:', value='\n'.join([f'{i + 1} - {last_players[i]}' for i in range(len(last_players))]), inline=False)
                    else:
                        new_embed.add_field(name='Ready!!', value='Good luck, have fun!', inline=False)
    
                    new_embed.set_footer(text="To pick a player, click on the emoji of his number")

                    message = await channel.send(embed=new_embed)
                    
                    reactions_to_add = emoji[len(last_players)]
                    for reaction in reactions_to_add:
                        await message.add_reaction(reaction)

                    kap = 1
                    
            else:
                await channel.send(f'Player {selected_player} in other team')
        elif kap == 1:
            await channel.send(f'Now is peaking another capitan')
                        

    if len(last_players) == 0:
        # Assign teams and move players
        for el1 in list_com1:    
            member = discord.utils.get(channel.guild.members, name=el1)
            await member.move_to(voice_channel_1)
        await kapitan_players[0].move_to(voice_channel_1)

        for el2 in list_com2:    
           member = discord.utils.get(channel.guild.members, name=el2)
           await member.move_to(voice_channel_2)
        await kapitan_players[1].move_to(voice_channel_2)

        embed = discord.Embed(title="Game is ready!", description="Here are your teams:", color=discord.Color.purple())
        embed.set_thumbnail(url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTvbwstNLPp77vL3VG5G3H6EVUt705BVF-sEQ&usqp=CAU')
        embed.set_author(name="discord battle")
        embed.add_field(name=f'Capitan 1 - {kapitan_players[0]}', value=f'Players team 1: {", ".join(list_com1)}')
        embed.add_field(name=f'Capitan 2 - {kapitan_players[1]}', value=f'Players team 2: {", ".join(list_com2)}')
    
        await channel.send(embed=embed)

bot.run('MTExMh0')
