const fs = require('fs')
const net = require('net')

fs.open('data.pipe', fs.constants.O_RDONLY, (err, fd) => {
    const pipe = new net.Socket({fd});

    pipe.on('data', data => {
        console.log(data.toString());
    });

    pipe.on('end', () => {
        console.log('end');
    });
});
