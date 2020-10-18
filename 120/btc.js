setInterval(async () => {
    let { data } = await axios
        .get('https://api.coindesk.com/v1/bpi/currentprice.json');

    document.getElementById('price').innerText = '$' + data.bpi.USD.rate;
}, 2000);
