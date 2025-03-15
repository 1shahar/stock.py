#-------------------stock----------------------
from finvizfinance.quote import finvizfinance
import yfinance as yf
from tradingview_ta import TA_Handler, Interval, Exchange
import pandas as pd
import numpy as np

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
#------------------------------------------------------------------------------------------
# stock to check price and div
def priceDiv(stock=[]):
    for tkrs in stock:
        price = price_now(tkrs.upper())
        print(f"-{tkrs}- --{price[0]}$ div: {price[1]} monthly-div {price[1]/12:.2f}")
    
#------------------------------------------------------------------------------------------  
# first cost and risk       
def Firstcost(tkr="",amount=0,div=0,enter_price=0,risk=0,profit=0, tax=2.5):
    cost = (amount*enter_price)+tax
    buy_value=(amount*enter_price)+tax
    stop_value=(amount*risk)-buy_value+-2.5
    profit_value=(amount*profit)-buy_value-2.5

    print(f"{tkr} amount-{amount}- cost {cost}$/ {cost*float(USD_ILS()):.2f} ---- div {div*amount:.2f}$ /{div*amount*float(USD_ILS()):.2f} "
         f"stop:{stop_value}$/{stop_value*float(USD_ILS())} profit:{profit_value}$/{profit_value*float(USD_ILS()):.2f} ")
    
#------------------------------------------------------------------------------------------  
# stop and profit
def StopProfit(tkr="spyi",buy_value=5000 ,amount=100, stop_loss=45, take_profit=55):
    stop_value=(amount*stop_loss)-buy_value+-2.5
    profit_value=(amount*take_profit)-buy_value-2.5
    
#------------------------------------------------------------------------------------------  
# stock carolation 
class StockAnalyzer:
    def __init__(self):
        self.data = {}
    def add_stock(self, ticker, period):
        stock_data = yf.Ticker(ticker).history(period=period)
        self.data[ticker] = stock_data['Close']
    def calculate_correlation_matrix(self):
        df = pd.DataFrame(self.data)
        correlation_matrix = df.corr()
        return correlation_matrix
    def display_correlation_matrix(self):
        correlation_matrix = self.calculate_correlation_matrix()
        print(correlation_matrix)
        first_row_sum = correlation_matrix.iloc[0].sum()
        print(f"corlation: {first_row_sum:.2f}/0")
        
#------------------------------------------------------------------------------------------  
# balance all stock 
class StockBalancer:
    def __init__(self):
        self.data = {}
    def add_stock(self, ticker, period):
        stock_data = yf.Ticker(ticker).history(period=period)
        self.data[ticker] = stock_data['Close']
    def calculate_correlation_matrix(self):
        df = pd.DataFrame(self.data)
        correlation_matrix = df.corr()
        return correlation_matrix
    def calculate_weights(self):
        correlation_matrix = self.calculate_correlation_matrix()
        sum_of_correlations = correlation_matrix.sum(axis=1) - 1  # Exclude self-correlation
        inverse_sum_of_correlations = 1 / sum_of_correlations
        weights = inverse_sum_of_correlations / inverse_sum_of_correlations.sum()
        return weights
    def balance_investment(self, investment_amount):
        weights = self.calculate_weights()
        allocations = {}
        for ticker, weight in weights.items():
            price = self.data[ticker][-1]  # Use the latest closing price
            shares = investment_amount * weight / price
            allocations[ticker] = int(shares)
        return allocations
    def display_allocations(self, investment_amount):
        allocations = self.balance_investment(investment_amount)
        for ticker, shares in allocations.items():
            print(f"Number of shares to buy for {ticker}: {shares}")
        
#------------------------------------------------------------------------------------------
# My-stock 

class Protfolio_stock():
    profit=0
    div=0
    acount=22000

    def __init__(self,tkr="", amount=0 , enter_price=0 , risk=0 , reword=0 , tax= 2.5 ):
        self.amount =amount 
        self.tkr =tkr 
        self.enter_price  =enter_price  
        self.risk  =risk  
        self.reword  =reword  
        self.tax=tax
        self.cost = 0
        self.buy_value = 0
        self.get_div = 0
        self.pay_tax = 0
    def update(self,amount=0,buy_value=0,get_div=0,pay_tax=0):
        if amount!=0:
            self.amount=amount
        if buy_value!=0:
            self.buy_value=buy_value
        else:
            self.buy_value = (self.amount*self.enter_price)+self.tax
        real_price = self.buy_value/self.amount
        now_price = price_now(self.tkr)
        now_value = float(now_price[0])*self.amount
        profit = now_value-self.buy_value
        profit_prosent = (profit/self.buy_value)*100
        print(f"{self.tkr} ||Price: buy:{real_price:.2f} now:{now_price[0]} ||value buy:{self.buy_value:.2f} -now:{now_value:.2f} profit: {profit:.2f} {profit_prosent:.2f}% stop:{self.risk} take:{self.reword}")
        Protfolio_stock.profit+=profit
        Protfolio_stock.div+=get_div
        
    @classmethod
    def mystock_total(cls):
        print("\n")
        print (f"start year acount: {cls.acount:.2f}")
        print (f"profit: {cls.profit:.2f}")
        print (f"div {cls.div:.2f}")

