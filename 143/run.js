const util = require('util');
const fs = require('fs/promises');
const exec = util.promisify(require('child_process').exec);
const axios = require('axios');

(async () => {
    // capture frame
    // await exec(
    //     'ffmpeg -y -f video4linux2 -s 1280x720 ' +
    //     '-i /dev/video1 -frames 1 code.jpg'
    // );

    // convert to base 64
    const image = await fs.readFile('code.jpg');
    const base64 = image.toString('base64');

    const url =
        `https://vision.googleapis.com/v1/images:annotate` +
        `?key=${process.env.gkey}`;

    // send to vision api
    const results = await axios
        .post(url, {
            requests: [{
                image: {
                    content: base64
                },
                features: [{
                    type: 'DOCUMENT_TEXT_DETECTION'
                }]
            }]
        });

    const code = results.data.responses[0].fullTextAnnotation.text;

    console.log(code);
    //eval(code);
})();
