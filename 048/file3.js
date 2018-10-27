const fs = require('fs');

for (let i = 1; i <= 5; ++i) {
    fs.readFile('stuff/' + i + '.txt', (err, data) => {
        console.log(data.toString().trim());
    });
}
