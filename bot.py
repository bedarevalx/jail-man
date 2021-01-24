import discord
import os
from discord.ext import commands
client = discord.Client()



#@bot.command(pass_context=True) #разрешаем передавать агрументы
#async def test(ctx, arg): #создаем асинхронную фунцию бота
#    await ctx.send(arg) #отправляем обратно аргумент*/

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if(message.channel.id == 801192621250838548):
        channel = client.get_channel(802979380489093170)
        response = message.content
        await channel.send(f"Отправитель:<@{message.author.id}>\n {message.content}")
        await message.delete()
        await message.author.send(f"Ваша жалоба отправлена администрации\nТекст жалобы:\n{message.content}")

token = os.environ.get('BOT_TOKEN')