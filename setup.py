from finvizfinance.quote import finvizfinance    
import tkinter as tk  
import yfinance as yf
from tradingview_ta import TA_Handler, Interval, Exchange
import pandas as pd
import numpy as np
import os
from db import *


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




#----------------------------------------------------------------------------------------------------------------------
#________________alert______________________
def alert(stocks):
    for i in stocks:
        price_now_i =float(price_now(i['tkr'])[0])
        print (f'{i['tkr']} price now {price_now_i:.2f} risk: {i['risk']} reword: {i['reward']}')

#________________get price__________________

def price(stocks):
    for i in stocks:
        j = price_now(i['tkr'])
        print (f'{i['tkr']:4} , price:{float(j[0]):4.2f} , div:{float(j[1]):4.2f} ,div/12: {(j[1])/12:.2f}')

#___________________ carolation and amount ________

class corelation():
    def __init__(self,stocks=[]):
        self.stocks=stocks
        self.get_corelation()
        
    def get_corelation(self,corelation_time='1mo'):
        tickers =  [] 
        for i in self.stocks:
                tickers.append(i["tkr"])         
        data = {}
        for ticker in tickers:
            stock_data = yf.Ticker(ticker).history(period=corelation_time)
            data[ticker] = stock_data['Close']
        df = pd.DataFrame(data)
        correlation_matrix = df.corr() #print(correlation_matrix)
        self.one_line_correlations = correlation_matrix.iloc[:, 0] 
        print(f"stocks corelation \n______________\n{self.one_line_correlations}\n")

        stock_value=[]
        wigete = []

        for i in self.stocks:
            try:
                i["amount"]
            except:
                print("insert amount and try again")
                break

        for i in self.stocks:
            stock_value.append(float(i["amount"])*(float(price_now(i["tkr"])[0])))
            t_stock_value=sum(stock_value)
        print(f"protfolio total value\n______________\n{t_stock_value}\n")

        print(f"wight\n______________")
        for i in self.stocks:
        #wi (stock_value/total_value)
            wigete.append((float(i["amount"])*(float(price_now(i["tkr"])[0])/t_stock_value)))
            print(f"stock {i['tkr']} wighet {((float(i["amount"])*(float(price_now(i["tkr"])[0])/t_stock_value))*100):.2f}%")
        
        index_wi=0  
        portfolio_coronation=0
        ct = ct=self.one_line_correlations.to_dict()
        for i in ct:
            portfolio_coronation+=round(wigete[index_wi]*ct[i],2)
            index_wi+=1
        print(f"\n __________\n portfolios corelation by amount\n___________\n: {portfolio_coronation:.2f}")

# cost and risk -----------------
class build_values_instance:
    def __init__(self,new_stock=[]):
        self.new_stock=new_stock
        
        for i in self.new_stock:
            print (i)
            self.now_price,self.div = price_now(i['tkr'])
            self.div = float(self.div)*i['amount']
            self.cost = (i['entery_price']*i['amount'])+2.5
            self.real_price=self.cost/i['amount']

            print(f'{i['tkr']} cost: {self.cost}$  year-div: {self.div:.2f}$ monthly: {self.div/12:.2f}$')
            
            self.stop_value=(i['amount']*i['risk'])-self.cost+-2.5
            self.reward_value=(i["amount"]*i["reward"])-self.cost-2.5

            print(f"{i['tkr']} stop value: {self.stop_value}$ {self.stop_value*float(USD_ILS()):.2f} reward value: {self.reward_value}$ {self.reward_value*float(USD_ILS()):.2f}\n")
            
#c1 -------------------my stock info---------------------
class protfolio_value:
    buy=0
    now_value=0
    profit=0
    risk=0
    reward=0
    dive=0

    def __init__(self,stocks=[]):
        self.stocks=stocks
        for i in self.stocks:
            self.calculates(i)

    def calculates(self,i):
            if i['cost'] == 0:   
                cost = (i['amount']*i['enter_price'])+2.5
                real_price=cost/i['amount']
            else:
                cost = i['cost']
                real_price = cost/i['amount']

            self.stop_value=round((i['amount']*i['risk'])-cost+-2.5,2)
            self.reward_value=round((i['amount']*i['reward'])-cost-2.5,2)
            self.i_now_price =round(float(price_now(i["tkr"])[0]),2)
            self.now_value =round( i['amount']*self.i_now_price,2)
            self.profit_value = round(self.now_value - cost,2)
            self.prosent = round((self.profit_value/cost)*100,2)
    
            protfolio_value.buy+=cost
            protfolio_value.now_value+=self.now_value
            protfolio_value.profit+=self.profit_value
            protfolio_value.risk+=self.stop_value
            protfolio_value.reward+=self.reward_value

            print(f'{i['tkr']:4} cost: {cost:.2f}$ price:{real_price:.2f} now:{self.now_value:8}$  Profit: {self.profit_value:8.2f}$ {self.prosent:8.2f}% -- '
                f'reward:{i['reward']:6.2f} {self.reward_value:6.2f}$  Stop:{i['risk']:6.2f} {self.stop_value:6.2f}$ ')
            
    @classmethod
    def result(cls):
        print(f"profit: {cls.profit}$ {cls.profit*float(USD_ILS()):.2f}")   

def my_stock_value():
    protfolio_value(stocks)
    protfolio_value.result()

#c2 -------------------- balance corelation 0--------------------------------------   
class stocks_balance:
    def __init__(self,stocks):
        self.stocks=stocks
        print ("\n")
        corelation(stocks)
        good_amount= ""

        print ("\n")
        print("insert new amount of stock check carolation result")
        print("--------------------------------------------")
        
        
        for stock in stocks:
            print(stock["tkr"] , stock['amount'])
            stock["amount"] = input ("new amount ? " )

        print ("\n")
        for stock in stocks:
            print (f"{stock['tkr']} amount:{stock['amount']}")
        corelation(stocks)


#-------------------------------------------------------------------
#_________________bank present______________________
def bank():
    print("summary bank")
    folder_path = '.'
    for root, directories, files in os.walk(folder_path):
        for filename in files:
            if filename.endswith('.xlsx'):
                file_path = os.path.join(root, filename)
                print(filename)
    df = pd.read_excel(file_path, engine='openpyxl')
    date_format = '%Y-%m-%d'
    df['Month_Year'] = pd.to_datetime(df['Unnamed: 0'], format=date_format, errors='coerce').dt.to_period('M')
    monthly_summary = df.groupby('Month_Year').agg(
        spend=('Unnamed: 4', 'sum'),
        earn=('Unnamed: 5', 'sum')
    ).reset_index()
    monthly_summary['profit'] = monthly_summary['earn'] - monthly_summary['spend']
    sum_row = monthly_summary[['spend', 'earn', 'profit']].sum()# Calculate sum 
    average_row = monthly_summary[['spend', 'earn', 'profit']].mean()# Calculate average
    summary_df = pd.DataFrame([sum_row, average_row], index=['Sum', 'Average'])# new DataFrame sum and average
    monthly_summary = pd.concat([monthly_summary, summary_df])# Concatenate the summary 
    print (monthly_summary) 

#------------------------------------------------------------broker
class broker():
    balance = 0
    def __init__(self,budget):
        self.budget=budget
                    
        for i in budget:
            self.add_less(i)

    def add_less(self,i):
        self.acount = i["inin"]-i["out"]
        broker.balance+=self.acount
    
    @classmethod
    def result(cls):
        r=(f'broker deposit up for today {cls.balance}  {cls.balance/(float(USD_ILS())):.2f}$')
        return r