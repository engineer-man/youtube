const fs = require('fs');

fs.readFile('stuff.txt', (err, data) => {
    console.log(data.toString());
});

console.log('here');
