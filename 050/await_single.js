const fs = require('fs');
const util = require('util');
const read = util.promisify(fs.readFile);

var run = async () => {
    // promise version
    read('data1.txt')
        .then(data => {
            console.log(data.toString());
        })


    // async/await version
    try {
        const data = await read('data1.txt')
        console.log(data.toString());
    } catch (e) {
        // handle the error
    }

};

run();
