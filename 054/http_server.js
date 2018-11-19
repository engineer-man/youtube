const http = require('http');

const server = http.createServer((req, res) => {
    let content = '';

    // append data as it comes in
    req.on('data', data => {
        content += data;
    });

    // write the data back to the client
    req.on('end', () => {
        res.write(content);
        res.end();
    });
});

server.listen(9090, '0.0.0.0');
