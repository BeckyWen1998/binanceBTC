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

def changeToUsd():
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
# get latest price from Binance API
    ethusdt = client.get_symbol_ticker(symbol="ETHUSDT")
    gbpusdt = client.get_symbol_ticker(symbol="GBPUSDT")
    ethusdt2 = client.get_symbol_ticker(symbol="ETHUSDT")
    
    ethusdt_price = float(ethusdt['price'])
    gbpusdt_price = float(gbpusdt['price'])
    ethusdt2_price = float(ethusdt2['price'])

    print(ethusdt_price)
    print(gbpusdt_price)
    print(ethusdt2_price)
# print full output (dictionary)
    change_price =(gbpusdt_price*ethusdt2_price*1.02)/ethusdt_price
    change_price = ('%.4f'% change_price)


    print_data = "gbpusdtethusdtusd:" + change_price + ' ' + str(now) + '\n'
    print(print_data)
    return print_data


filetime = datetime.now().strftime('%Y%m%d%H') +'00'
path = '/home/becky/gbpusdtusdCrypto/gbpusdtusdCrypto_' + filetime + '.txt'

f = open(path, 'w')
i=0
while i<720:
    print_data = changeToUsd()
    f.write(print_data)
    time.sleep(5)
    i=i+1
f.close()
