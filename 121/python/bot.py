import discord
import asyncio

bot = discord.Client()

@bot.event
async def on_message(message):
    # do something with message
    print(message.content)

    if message.content == 'hello bottymcbotface':
        await message.channel.send('hello!')

bot.run('NzY5NzU4NTQ2MDkwMTMxNDc2.X5Trgg.Il75Uo9yz8XXyN-55xSN9Im0nw4')
