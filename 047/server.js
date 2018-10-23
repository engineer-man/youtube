const http = require('http');

return http
    .createServer((req, res) => {
        res.end('test');
    })
    .listen(8080);
