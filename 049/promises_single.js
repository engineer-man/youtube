const fs = require('fs');
const util = require('util');

// old
fs.readFile('data1.txt', (err, data) => {
    console.log(data.toString());
});

// new
var read = util.promisify(fs.readFile);

read('data1.txt')
    .then(data => {
        console.log(data.toString());
    });
