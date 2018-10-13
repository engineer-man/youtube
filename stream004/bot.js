const ws = require('ws');

const wss = new ws('ws://10.0.0.10:3434');

wss.on('message', message => {
    console.log(message)
    message = JSON.parse(message)

    if (message.message === 'hello felix') {
        wss.send(JSON.stringify({
            type: 'bot',
            name: 'felix',
            message: 'hi friend'
        }))
    }
});
