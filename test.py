import os
from dotenv import load_dotenv
load_dotenv()
import pyupbit
import pandas as pd
import pandas_ta as ta
import json
from openai import OpenAI
import schedule
import time


result = pyupbit.get_orderbook(ticker="KRW-BTC")

df_daiy = pyupbit.get_ohlcv("KRW-BTC", "day", count=30)
df_hourly = pyupbit.get_ohlcv("KRW-BTC", interval="minue60", count=24)

print(df_daiy)