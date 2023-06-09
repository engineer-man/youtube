const fs = require('fs/promises');

module.exports = {

    async open(file) {
        let content = await fs.readFile(file);

        return content.toString();
    }

};
