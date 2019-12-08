const request = require('request-promise');

const CLIENT_ID = '12345';
const CLIENT_SECRET = 'abcde';

module.exports = {

    discord_login(req, res) {
        // redirect the user to the resource owner for authorization
        return res.redirect(
            'https://discordapp.com/api/oauth2/authorize'+
            '?client_id=' + CLIENT_ID +
            '&redirect_uri=' +
                encode_uri_component('http://127.0.0.1/discord_login_callback') +
            '&response_type=code'+
            '&scope=identify%20email'
        );
    },

    async discord_login_callback(req, res) {
        // the code that comes back from the resource owner during authorization
        let code = req.query.code;

        // trade the code in for an access token
        let auth = await request
            ({
                method: 'post',
                url: 'https://discordapp.com/api/v6/oauth2/token',
                headers: {
                    'content-type': 'application/x-www-form-urlencoded'
                },
                form: {
                    code,
                    client_id: CLIENT_ID,
                    client_secret: CLIENT_SECRET,
                    grant_type: 'authorization_code',
                    redirect_uri: 'http://127.0.0.1/discord_login_callback',
                    scope: 'identify email'
                },
                json: true,
                simple: true
            });

        // use that token to get the data of the user
        let user = await request
            ({
                method: 'get',
                url: 'https://discordapp.com/api/v6/users/@me',
                headers: {
                    Authorization: 'Bearer ' + auth.access_token
                },
                json: true,
                simple: true
            });

        // do something with the user data
    }

};
