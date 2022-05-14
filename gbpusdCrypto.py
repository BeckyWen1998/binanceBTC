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
    ethgbp = client.get_symbol_ticker(symbol="ETHGBP")

    ethusdt_price = float(ethusdt['price'])
    ethgbp_price = float(ethgbp['price'])
    print(ethusdt_price)
    print(ethgbp_price)
# print full output (dictionary)
    change_price =(ethusdt_price*1.02)/ethgbp_price
    change_price = ('%.4f'% change_price)


    print_data = "gbpethusdtusd:" + change_price + ' ' + str(now) + '\n'
    print(print_data)
    return print_data


filetime = datetime.now().strftime('%Y%m%d%H') +'00'
path = '/home/becky/gbpusdCrypto/gbpusdCrypto_' + filetime + '.txt'

f = open(path, 'w')
i=0
while i<720:
    print_data = changeToUsd()
    f.write(print_data)
    time.sleep(5)
    i=i+1
f.close()
