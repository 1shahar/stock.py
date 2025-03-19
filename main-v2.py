from finvizfinance.quote import finvizfinance
import yfinance as yf
from tradingview_ta import TA_Handler, Interval, Exchange
import pandas as pd
import numpy as np

def buget():
    '''insert year buget'''
    buget_year_2025=22000
    return buget_year_2025

def check_stock():
    '''insert stock to check'''
    tkr=["spyi","sh"]
    return tkr

def stocks():
    '''insert stock 
    pro(strategy1)/
    hold/
    '''
    cal_tkr=[
        {"step": "pr",'position':'hold' ,"tkr": "spyi", "amount": 1,"buy_value":400 ,"div": 0, "enter_price": 3, "risk": 200, "reward": 800, "tax": 2.5},
        {"step": "pr",'position':'ne' ,"tkr": "msty", "amount": 1,"buy_value":0 ,"div": 0, "enter_price": 250, "risk": 200, "reward": 800, "tax": 2.5} 
    ]
    return cal_tkr  

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
    return now_price , div

class stock():
    buy=0
    now_value=0
    profit=0
    risk=0
    reward=0
    
    def __init__(self,buget_broker):
        self.buget_broker=buget_broker

    def selector(self,tkr=[]):
        if tkr==[]:
            print("no stock to check")
        else :   
            self.tkr=tkr
            for i in self.tkr:
                print(f'stock {i} {float(price_now(i)[0]):.2f} {float(price_now(i)[1]):.2f}/{float(price_now(i)[1])/12:.2f}')
        
    def calculates(self,i):
        if i['buy_value'] == 0:   
            cost = (i['amount']*i['enter_price'])+i['tax']
            real_price=cost/i['amount']
        else:
            cost = i['buy_value']
            i['enter_price'] = cost/i['amount']
            real_price = i['enter_price']
        stop_value=(i['amount']*i['risk'])-cost+-2.5
        reward_value=(i['amount']*i['reward'])-cost-2.5
        i_now_price =float(price_now(i["tkr"])[0])
        now_value = i['amount']*i_now_price
        profit_value = now_value - cost
        prosent = (profit_value/cost)*100

        stock.buy+=cost
        stock.now_value+=now_value
        stock.profit+=profit_value
        stock.risk+=stop_value
        stock.reward+=reward_value

        return cost,real_price,stop_value,reward_value,i_now_price,now_value,profit_value,prosent

    #startagy1 pro
    def pro(self,cal_tkr=[],new=0):
        for i in cal_tkr:
            if new==1:
                i['position']='hold'
            if i['step']=='pro' and i['position']!='new':
                cal=self.calculates(i)
                
                print(f'{i['tkr']} - Buy: {cal[0]:.2f}$ (At Price: {cal[1]:.2f})'
                      f' Now Price:{cal[4]:.2f}$ '
                      f'(Stop:{i['risk']:.2f}/{cal[2]:.2f}$ Profit:{i['reward']:.2f}/{cal[3]:.2f}$)' 
                      f'atm-Value: {cal[5]:.2f}$, Profit: {cal[6]:.2f}$ ({cal[7]:.2f}%)')
    
    @classmethod
    def result(cls):
        print (f' total buy: {cls.buy}$ ')
        print (f' total now value: {cls.now_value}$ ')
        print (f' total profit: {cls.profit}$ ')
        print (f' total profit %: {(cls.profit/cls.buy)*100:.2f}% ')
        print (f' total risk: {cls.risk}$ ')
        print (f' total reward: {cls.reward}$ ')


buget2025=buget()
y2025=stock(buget2025)

# check price and div
tkr=check_stock()
if tkr:
    print("_________stock was check result:_________:")
    y2025.selector(tkr)
    print("\n")

# strategy1 pro
runer_strategy1=0
cal_tkr=stocks()
for i in cal_tkr:
    if "pro" in i["step"]:
        runer_strategy1=1

if runer_strategy1==1:
    print("_________stock holds in profit strategy result:_________:")
    y2025.pro(cal_tkr,new=0)
    print("_________total stock holds in profit strategy result:_________:")
    stock.result()
    print("\n")

runer_strategy1=0
for i in cal_tkr:
    if "new" in i["position"]:
        runer_strategy1+=1

if runer_strategy1>0:
    print("_________stock holds+new in profit strategy result:_________:")
    cal_tkr=stocks()
    y2025.pro(cal_tkr,new=1)
    print("_________total stock holds+new in profit strategy result:_________:")
    stock.result()
    print("\n")

