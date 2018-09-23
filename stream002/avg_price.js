const request = require('request-promise');
const q = require('q');

var total_results = [];

var chain = q.fcall(() => {});

for (let i = 1; i < 4; ++i) {
    chain = chain
        .then(() => {
            return request({
                method: 'get',
                url: 'https://www.flipkey.com/content/srp/srp_fk/index_json/book/destin/222604340//zoom.11?page=' + i,
                json: true,
                simple: true
            })
            .then(results => {
                total_results = total_results.concat(results.results);
                return null;
            });
        });
}

return chain
    .then(() => {
        var daily_prices = total_results
            .map(r => r.dailyPrice)
            .filter(r => {
                if (!r) return false;
                return true;
            })
            .map(r => {
                r = +r.replace(/[^0-9]/gi, '');

                return r;
            });

        var sum = daily_prices.reduce((a, b) => a + b);
        console.log('calculation based on ' + daily_prices.length + ' values');
        console.log(sum / daily_prices.length);
    });
