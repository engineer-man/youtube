import threading
import requests
import sys
import time
import os

prices = { 'btc': { 'price': 0.00, 'delta': 0.00 } }

if len(sys.argv) < 2:
    print('please supply symbols')
    quit()

for sym in sys.argv[1:]:
    prices[sym.lower()] = { 'price': 0.00, 'delta': 0.00 }

def update_price(sym):
    while True:
        template = 'https://api.bittrex.com/api/v1.1/public/getticker?market={}-{}'
        first_pair = 'usd' if sym == 'btc' else 'btc'

        pricing = requests.get(template.format(first_pair, sym)).json()
        prices[sym]['price'] = pricing['result']['Last']

        time.sleep(3)

for sym, price in prices.items():
    t = threading.Thread(target=update_price, args=(sym,))
    t.start()

while True:
    os.system('cls' if os.name == 'nt' else 'clear')

    for sym, _ in prices.items():
        sym_formatted = sym.ljust(5)
        btc_price = prices[sym]['price']
        usd_price = prices['btc']['price'] * btc_price

        if sym == 'btc':
            print('{} -> ${:.2f}'.format(sym_formatted, btc_price))
        else:
            print('{} -> {:.8f} btc (${:.2f})'.format(sym_formatted, btc_price, usd_price))

    time.sleep(.5)
