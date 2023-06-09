import fs from 'fs/promises';

export default {

    async open(file) {
        let content = await fs.readFile(file);

        return content.toString();
    }

};
