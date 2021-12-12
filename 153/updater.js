const axios = require('axios');
const qs = require('qs');

const CLIENT_ID = '507952577459-nkp348iglr2gs7fepn6ek4sn65qugllv.apps.googleusercontent.com';
const CLIENT_SECRET = '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';

const API_KEY = 'AIzaSyDNrXAUzEEknjgL2f7buQ-mM85mvUD3uhk';
const REFRESH_TOKEN = '1//01Yk8MtpmtPG5CgYIARAAGAESNwF-L9Ir6XHVLUIAGxaCHY85u3yC1tZQgmd271nhO6y4ggJASKvvwnidwBAYtay3_b1_9DHQsoc';

(async () => {
    // step 1 - get access token
    let res1 = await axios
        .post(
            'https://oauth2.googleapis.com/token',
            qs.stringify({
                refresh_token: REFRESH_TOKEN,
                grant_type: 'refresh_token'
            }),
            {
                auth: {
                    username: CLIENT_ID,
                    password: CLIENT_SECRET
                }
            }
        );

    const token = res1.data.access_token;

    // step 2 - get video information
    let res2 = await axios
        .get(
            'https://www.googleapis.com/youtube/v3/videos',
            {
                params: {
                    id: 'uuuTKf3y3VI',
                    part: 'snippet,statistics',
                    key: API_KEY
                }
            },
        );

    let data = res2.data.items[0];

    let { categoryId, title, description, tags } = data.snippet;
    let { viewCount } = data.statistics;

    // step 3 - update video
    await axios
        .put(
            'https://www.googleapis.com/youtube/v3/videos?part=snippet',
            {
                id: 'uuuTKf3y3VI',
                snippet: {
                    categoryId,
                    title: `This video has ${viewCount} views`,
                    description,
                    tags,
                }
            },
            {
                headers: {
                    authorization: 'Bearer ' + token
                }
            }
        );
})();
