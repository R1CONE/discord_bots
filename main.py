import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='-', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print('Bot is ready')
    synced = await bot.tree.sync()
    print(synced)
    print("Slash commands: " + str(len(synced)) + " commands")

@bot.tree.command(name="find_user", description="Looking for discord user")
async def find_user(ctx, interaction: discord.Interaction, member:discord.Member=None):
    if member:
        await interaction.response.send_message(f"User is: {member.mention}")


bot.run('MTE3')
