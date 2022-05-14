import os
import time
from binance.client import Client
from datetime import datetime
now = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]



api_key = os.environ.get('binance_api')
api_secret = os.environ.get('binance_secret')

#print(api_key)
#print(api_secret)

client = Client(api_key, api_secret)

# get latest price from Binance API
#btc_price = client.get_symbol_ticker(symbol="BTCGBP")
# print full output (dictionary)
#print(btc_price)

def ethusdt():
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
# get latest price from Binance API
    eth_price = client.get_symbol_ticker(symbol="ETHUSDT")
# print full output (dictionary)
    print(eth_price)
    price = eth_price['price']
    print(price)


    print_data = eth_price['symbol'] + ':' + price + ' ' + str(now) + '\n'
    print(print_data)
    return print_data


filetime = datetime.now().strftime('%Y%m%d%H') +'00'
path = '/home/becky/ethusdt/ethusdt__' + filetime + '.txt'

f = open(path, 'w')
i=0
while i<720:
    print_data = ethusdt()
    f.write(print_data)
    time.sleep(5)
    i=i+1
f.close()
