const { google } = require('googleapis');

(async () => {
    const client = new google.auth.OAuth2(
        '507952577459-nkp348iglr2gs7fepn6ek4sn65qugllv.apps.googleusercontent.com',
        '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',
        'http://localhost'
    );

    const url = client.generateAuthUrl({
        access_type: 'offline',
        scope: [
            'https://www.googleapis.com/auth/youtube'
        ]
    });

    console.log(url)

    const { tokens } = await client.getToken('4/0AX4XfWggMxidf57Tf1J24pEi3M-YOLQUjP7TqpwO3mgfenA0yKJK-QCv8Yvk-Z7LhIDfAg');

    console.log(tokens)
})();
