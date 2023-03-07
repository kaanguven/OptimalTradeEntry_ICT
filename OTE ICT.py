import ccxt.pro as ccxt
import pandas as pd
import pandas_ta as ta
import numpy as np
import os
from datetime import date, datetime, timezone, tzinfo
import time, schedule
import numpy as np
import requests
from math import floor
import ta as tl
import math
import functools
from pandas import DataFrame
import warnings
from io import StringIO
from pathlib import Path
from asyncio import run, gather
warnings.filterwarnings("ignore")
 


# API TANIMLAMALARI
account_binance = ccxt.binance({
    "apiKey": '',
    "secret": '',
    "enableRateLimit": True,
    'options': {
        'defaultType': 'future'
    }
})

fibExt1 = 1.618
fibExt2=2
fibExt3=1.5
fibExt4 = 2.5
fibExt5=3
fixExt6 = 3.5
symbol = "ETH/BUSD"  
timeframe = "15m"

async def ote():
    while True: 
        time.sleep(0.34)
        try:
            
            orderTime = datetime.utcnow()
            ohlcvLB = await account_binance.fetch_ohlcv(symbol, timeframe)
            dfLB = pd.DataFrame(ohlcvLB, columns=['time', 'open', 'high', 'low', 'close', 'volume'])
            indiPoint = pd.DataFrame(columns=['time'])
            if len(ohlcvLB):
                dfLB['time'] = pd.to_datetime(dfLB['time'], unit='ms')
                chartHigh = dfLB["high"].max()
                chartLow = dfLB["low"].min()
                isBull = dfLB["low"].idxmin() < dfLB["high"].idxmax()
                OTE=[]
                def fibLine(fibLevel):
                    fibRatio = 1-(fibLevel / 100)
                    if isBull:
                        fibPrice = chartLow  + ((chartHigh - chartLow) * fibRatio)
                    else:
                        fibPrice = chartHigh - ((chartHigh - chartLow) * fibRatio)

                    return fibPrice
                OTE.append([fibLine(61.8),fibLine(78.9)])
                print("Does Optimal Trade Entry for Bullish?",isBull)
                print("Optimal Trade Entry Price Ranges: ",OTE)
        except Exception as e:
            print(e)
            continue


# YOUR TRADE ENTRY CODE HERE.
run(ote())