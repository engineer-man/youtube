const ws = require('ws');

const server = new ws.Server({ host: '0.0.0.0', port: 3434 });

server.on('connection', socket => {
    socket.on('message', message => {
        server.clients.forEach(c => {
            c.send(message)
        });
    });
});
