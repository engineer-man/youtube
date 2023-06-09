const fs = require('fs');
const crypto = require('crypto');

const util = require('./util');

(async () => {
    let contents = await util.open('package.json');

    console.log(contents);
})();
