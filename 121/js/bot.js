const Discord = require('discord.js');
const bot = new Discord.Client();

bot.on('message', async message => {
    // do something with message
    console.log(message.content)

    if (message.content == 'hello bottymcbotface') {
        await message.channel.send('hello!')
    }
});

bot.login('NzY5NzU4NTQ2MDkwMTMxNDc2.X5Trgg.Il75Uo9yz8XXyN-55xSN9Im0nw4');
