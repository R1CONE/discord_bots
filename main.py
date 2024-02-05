import discord

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print('Бот готов')

@client.event
async def on_voice_state_update(member, before, after):
    global voice_channel
    voice_channel = client.get_channel(1135157429433282561)
    if after.channel and after.channel.id == 1135157429433282561 and after.channel != before.channel:
        if len(after.channel.members) == 1:
            print(f"Имя пользователя: {member.name}")
            print(f"ID пользователя: {member.id}")
            print(f"Отображаемое имя пользователя: {member.display_name}")
            print(f"Никнейм на сервере: {member.nick}")
            print(f"Дата создания учетной записи: {member.created_at}")

            channel = await client.fetch_channel(1135157429433282561)  # Получаем объект канала
            await channel.send(f"Приветствую тебя, {member.display_name}!")  # Отправляем сообщение приветствия


client.run('MTE3MTM1ODc0Mjk1MzA3ODc4NA.GlNku_.DWPfUuOm1tVoPuT3ybZp28UyJyfdvW9lptp0jg')
