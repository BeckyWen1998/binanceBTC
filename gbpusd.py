import logging
import pymysql
pymysql.install_as_MySQLdb()
import time
import requests
from datetime import datetime
from bs4 import BeautifulSoup
import threading

headers = {
    'user-agent' : 'Mozilla/5.0'    

}


#GBP to USD
def gbpToUsd():

    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
    url = 'https://finance.yahoo.com/quote/GBPUSD=X/'
    res = requests.get(url, headers=headers)
    res.encoding = 'utf-8-sig'
    soup = BeautifulSoup(res.text, 'lxml')
    data = soup.find("div","D(ib) Mend(20px)")
    gbpusd = data.select("fin-streamer")[0].text
    gbpusd = float(gbpusd)
    gbpusd = ('%.4f'% gbpusd)


    print_gbpusd = "GBPUSD:"+str(gbpusd) + " " + str(now) + '\n'
    #print("GBP-USD = " + str(gbpusd), now)
    return print_gbpusd

def timeinterval():
    time.sleep(30)

filetime = datetime.now().strftime('%Y%m%d%H') +'00'
path = '/home/becky/gbpusd/gbpusd_' + filetime + '.txt'

f = open(path,'w')
i=0
while i <120:
    t = threading.Thread(target = timeinterval)
    t.start()
    print_gbpusd = gbpToUsd()
    f.write(print_gbpusd)
    t.join()
    i=i+1
f.close

