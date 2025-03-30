from finvizfinance.quote import finvizfinance    # the script 
import yfinance as yf
from tradingview_ta import TA_Handler, Interval, Exchange
import pandas as pd
import numpy as np
import os

def USD_ILS():
    """convert usa to nis"""  
    handler = TA_Handler(
    symbol="USDILS",
    exchange="FX_IDC",  
    screener="forex",
    interval=Interval.INTERVAL_1_DAY  )
    analysis = handler.get_analysis()
    return (round(analysis.indicators['close'],2))

def price_now(tkr):
    """give the stock price"""
    stock = finvizfinance(tkr)
    a = stock.ticker_fundament()
    now_price = a['Price']
    div = a.get('Dividend TTM').split()[0]
    try:
        div=float(div)
    except:
        div=0
    return now_price , div , tkr
