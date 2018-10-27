const fs = require('fs');

for (var i = 0; i < 10; ++i) {
    fs.readFile('stuff.txt', (err, data) => {
        console.log(data.toString());
    });
}

console.log('here');
