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
        member_names = [member.name for member in members]

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

        await start_message(interaction, members, member_names)
        

    elif not (voice_channel_1 and voice_channel_2):
        await interaction.response.send_message('Both voice channels must be specified.')

    else:
        await interaction.response.send_message('You are not in a voice channel.')

emoji = ['\u0031\uFE0F\u20E3', '\u0032\uFE0F\u20E3', '\u0033\uFE0F\u20E3', '\u0034\uFE0F\u20E3', '\u0035\uFE0F\u20E3', '\u0036\uFE0F\u20E3', '\u0037\uFE0F\u20E3', '\u0038\uFE0F\u20E3']
list_com_1 = []
list_com_2 = []
kap = 1

async def start_message(interaction, members, member_names):
    kapitan_players = random.sample(member_names, 2)
    members_slim = members

    for player in kapitan_players:
        members_slim.remove(player)
        members_to_peack = members_slim


    
    kapitan1 = kapitan_players[0]
    kapitan2 = kapitan_players[1]
    print(f"Kapian1 name is {kapitan1}")
    print(f"Kapian1 name is {kapitan2}")
    for member in members:
        if member.name == kapitan1:
            kapitan1_id = member.id
        elif member.name == kapitan2:
            kapitan2_id = member.id
    print(f"kap1 is {kapitan1_id}")
    print(f"kap2 is {kapitan2_id}")

    embed = discord.Embed(title="Welcome to R1CONE Faceit", description="Kapitan 1, peak your players!", color=discord.Color.purple())
    embed.set_thumbnail(url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSRh6UJMDoGniGMJrj_UHk9fGlbSH0o8XR71w&s')
    embed.set_author(name="5 V 5")
    embed.add_field(name='Kapitan 1 - ', value=f'{kapitan1}')
    embed.add_field(name='Member of first team', value=f'{list_com_1}')
    embed.add_field(name='Kapitan 2 - ', value=f'{kapitan2}')
    embed.add_field(name='Member of second team', value=f'{list_com_2}')
    embed.add_field(name='Remain players: ', value=f'{members_to_peack}')

        
    message = await interaction.followup.send(embed=embed)
    len_play = len(members_to_peack)
    reactions_to_add = emoji[:len_play]
    for reaction in reactions_to_add:
        await message.add_reaction(reaction)

    if user.id == kapitan1.id:
        if kap == 1:
            if str(reaction) in emoji:
                start_game(interaction, members, kapian1, kapian2, members_to_peack)
                
    
    
    

async def start_game(interaction, members, kapian1, kapian2, members_to_peack):
    if user.id == kapitan1.id:
        if kap == 1:
            if str(reaction) in emoji:
                emoji_index = emoji.index(str(reaction))
                selected_player = members_to_peack[emoji_index]
                embed = discord.Embed(title="Welcome to R1CONE Faceit", description="Kapitan 1, peak your players!", color=discord.Color.purple())
                embed.set_thumbnail(url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSRh6UJMDoGniGMJrj_UHk9fGlbSH0o8XR71w&s')
                embed.set_author(name="5 V 5")
                embed.add_field(name='Kapitan 1 - ', value=f'{kapitan1}')
                embed.add_field(name='Member of first team', value=f'{list_com_1}')
                embed.add_field(name='Kapitan 2 - ', value=f'{kapitan2}')
                embed.add_field(name='Member of second team', value=f'{list_com_2}')
                embed.add_field(name='Remain players: ', value=f'{members_to_peack}')
            

bot.run('')
