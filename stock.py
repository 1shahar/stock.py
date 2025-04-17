import tkinter as tk
import pandas as pd
import os
from finvizfinance.quote import finvizfinance  
import yfinance as yf
import pandas as pd
from tradingview_ta import TA_Handler, Interval, Exchange
from db import *


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

def USD_ILS():
    """convert usa to nis"""  
    handler = TA_Handler(
    symbol="USDILS",
    exchange="FX_IDC",  
    screener="forex",
    interval=Interval.INTERVAL_1_DAY  )
    analysis = handler.get_analysis()
    return (round(analysis.indicators['close'],2))
#--------------------fun and class--------------------------------
def clear_cli():
    os.system('cls' if os.name == 'nt' else 'clear')
#----------------------------------------------------
def vs_code ():    
    file_path = r"C:\Users\user\Desktop\7up" 
    command = f'code "{file_path}"'
    os.system(command)
#----------------------------------------------------
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
#----------------------------------------------------
class broker():
    balance = 0
    def __init__(self,budget):
        self.budget=budget
                    
        for i in self.budget:
            self.add_less(i)

    def add_less(self,i):
        self.acount = i["inin"]-i["out"]
        broker.balance+=self.acount
    
    @classmethod
    def result(cls):
        print(f'broker deposit up for today {cls.balance}  {cls.balance/(float(USD_ILS())):.2f}$')
#----------------------------------------------------
def data_base(y,stocks): 
    global new_stocks
    global stocks_list
    new_stocks=[]
    #1
    stock1_name = stock1.get("1.0", tk.END).strip()
    stock2_name = stock2.get("1.0", tk.END).strip()
    stock3_name = stock3.get("1.0", tk.END).strip()
    stock4_name = stock4.get("1.0", tk.END).strip()

    if stock1_name:
        new_stocks.append({'tkr':stock1_name})
    if stock2_name:
        new_stocks.append({'tkr':stock2_name})
    if stock3_name:
        new_stocks.append({'tkr':stock3_name})
    if stock4_name:
        new_stocks.append({'tkr':stock4_name})

    amount_value1 = amount1.get("1.0", tk.END).strip()
    amount_value2 = amount2.get("1.0", tk.END).strip()
    amount_value3 = amount3.get("1.0", tk.END).strip()
    amount_value4 = amount4.get("1.0", tk.END).strip()

    if amount_value1:
        new_stocks[0]["amount"] = int(amount_value1)
    if amount_value2:
        new_stocks[1]["amount"] = int(amount_value2)
    if amount_value3:
        new_stocks[2]["amount"] = int(amount_value3)
    if amount_value4:
        new_stocks[3]["amount"] = int(amount_value4)

    entery_price_1 = entery_price1.get("1.0", tk.END).strip()
    entery_price_2 = entery_price2.get("1.0", tk.END).strip()
    entery_price_3 = entery_price3.get("1.0", tk.END).strip()
    entery_price_4 = entery_price4.get("1.0", tk.END).strip()

    if entery_price_1:
        new_stocks[0]["entery_price"] = float(entery_price_1)
    if entery_price_2:
        new_stocks[1]["entery_price"] = float(entery_price_2)
    if entery_price_3:
        new_stocks[2]["entery_price"] = float(entery_price_3)
    if entery_price_4:
        new_stocks[3]["entery_price"] = float(entery_price_4)
        
    risk_1 = risk1.get("1.0", tk.END).strip()
    risk_2 = risk2.get("1.0", tk.END).strip()
    risk_3 = risk3.get("1.0", tk.END).strip()
    risk_4 = risk4.get("1.0", tk.END).strip()
        
    if risk_1:
        new_stocks[0]["risk"] = float(risk_1)
    if risk_2:
        new_stocks[1]["risk"] = float(risk_2)
    if risk_3:
        new_stocks[2]["risk"] = float(risk_3)
    if risk_4:
        new_stocks[3]["risk"] = float(risk_4)       
        
    reward_1= reward1.get("1.0", tk.END).strip()
    reward_2= reward2.get("1.0", tk.END).strip()
    reward_3= reward3.get("1.0", tk.END).strip()
    reward_4= reward4.get("1.0", tk.END).strip()
    if reward_1:
        new_stocks[0]["reward"] = float(reward_1) 
    if reward_2:
        new_stocks[1]["reward"] = float(reward_2) 
    if reward_3:
        new_stocks[2]["reward"] = float(reward_3) 
    if reward_4:
        new_stocks[3]["reward"] = float(reward_4)  

    if y==0:
        stocks_list=new_stocks.copy()
    if y==1:
        stocks_list = stocks.copy()
    if y==2:
        if new_stocks:
            stocks_list = stocks.copy()
            for j in new_stocks:
                stocks_list.append(j)
    if y==3:
        new_stocks.clear()
        stocks_list.clear()
    basket = []   
    for i in stocks_list:
        print(i)
    #     basket.append(i['tkr'])
    # print (f"calculet for stocks: {basket}")
#----------------------------------------------------
def cal_info_stock():
    for i in stocks_list:
        stock_price_div= price_now(i['tkr'])
        print (f" {i['tkr']:6}   price: {stock_price_div[0]}$  yearly_div: {stock_price_div[1]}$  div_montly: {float(stock_price_div[1])/12:.2f}")
#----------------------------------------------------
def cal_simpel_crolation():
    stocks=stocks_list

    tickers =  [] 
    for i in stocks:
            tickers.append(i["tkr"])         
    data = {}
    for ticker in tickers:
        stock_data = yf.Ticker(ticker).history(period='1mo', interval='1d')
        data[ticker] = stock_data['Close']
    df = pd.DataFrame(data)
    correlation_matrix = df.corr() #print(correlation_matrix)
    one_line_correlations = correlation_matrix.iloc[:, 0] 
    print(f"stocks corelation \n______________\n{one_line_correlations}\n")
#----------------------------------------------------
def amount_crolation():
    stocks=stocks_list
    tickers =  [] 
    for i in stocks:
            tickers.append(i["tkr"])         
    data = {}
    for ticker in tickers:
        stock_data = yf.Ticker(ticker).history(period='1mo', interval='1d')
        data[ticker] = stock_data['Close']
    df = pd.DataFrame(data)
    correlation_matrix = df.corr() #print(correlation_matrix)
    one_line_correlations = correlation_matrix.iloc[:, 0] 

    stock_value=[]
    wigete = []

    for i in stocks:
        stock_value.append(float(i["amount"])*(float(price_now(i["tkr"])[0])))
        t_stock_value=sum(stock_value)

    print(f"protfolio total value\n______________\n{t_stock_value}\n")

    print(f"wight\n______________")
    for i in stocks:
    #wi (stock_value/total_value)
        wigete.append((float(i["amount"])*(float(price_now(i["tkr"])[0])/t_stock_value)))
        print(f"stock {i['tkr']} wighet {((float(i["amount"])*(float(price_now(i["tkr"])[0])/t_stock_value))*100):.2f}% amount: {i['amount']}")

    index_wi=0  
    portfolio_coronation=0
    ct = one_line_correlations.to_dict()
    for i in ct:
        portfolio_coronation+=round(wigete[index_wi]*ct[i],2)
        index_wi+=1
    print(f"\n __________\n portfolios corelation by amount\n___________\n: {portfolio_coronation:.2f}")
#----------------------------------------------------
def value_risk_reward():
   
   # value cost risk 
   stocks= stocks_list
   total_cost=0
   
   results=[]
   for i in stocks:

        print(i)
        cost = (i['amount']*i['entery_price'])+2.5
        real_price = cost/i['amount']
        i_now_price =round(float(price_now(i["tkr"])[0]),2)
        i_div =round(float(price_now(i["tkr"])[1])*i['amount'],2)

        risk_value= (i['amount']*i['risk'])-cost+-2.5  
        rward_value = (i['amount']*i['reward'])-cost-2.5 

        result=(f"{i['tkr']:6} amount: {i['amount']:4} "
                f"cost: {cost:.2f}$ buy_price: {real_price:.2f}$ "
                f"today_price: {i_now_price}$  " 
                f"risk_value: {risk_value:.2f}$ reward_value: {rward_value:.2f}$"
                f"div get: {i_div/12:.2f}$")
        results.append(result)
   for i in results:
       print(i)
#----------------------------------------------------
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
                i['real_price']=round(real_price,2)

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

            print(f"{i['tkr']:4} amount: {i['amount']:4} "
                  f"real_price: {real_price:.2f}$ now_price: {self.i_now_price:.2f}$ profit: {self.profit_value:.2f}$ {self.prosent:.2f}%")
            
            # print(f'{i['tkr']:4} cost:{cost:.2f}$ price:{real_price:.2f} now:{self.now_value:8}$  Profit: {self.profit_value:8.2f}$ {self.prosent:8.2f}% -- '
                # f'reward:{i['reward']:6.2f} {self.reward_value:6.2f}$  Stop:{i['risk']:6.2f} {self.stop_value:6.2f}$ ')
            
    @classmethod
    def result(cls):
        print(f"profit: {cls.profit}$ {cls.profit*float(USD_ILS()):.2f}")   

#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------
#vars 
new_stocks=[]
stocks_list=[]
total_sell_profit=[]

# main Tk
root = tk.Tk()
root.title("Stock Analysis")
root.geometry("600x600")
root.configure(bg="black")
    

#--------------------------- labels for input box
label = tk.Label(root, text="stocks", font=("Arial", 14), bg="black", fg="white")
label.place(x=10, y=10)
label = tk.Label(root, text="amount", font=("Arial", 14), bg="black", fg="white")
label.place(x=10, y=50)
label = tk.Label(root, text="entery price", font=("Arial", 14), bg="black", fg="white")
label.place(x=10, y=90)
label = tk.Label(root, text="risk price", font=("Arial", 14), bg="black", fg="white")
label.place(x=10, y=130)
label = tk.Label(root, text="reward price", font=("Arial", 14), bg="black", fg="white")
label.place(x=10, y=170)
#--------------------------- input-box
#tkr
stock1 = tk.Text(root, font=("Arial", 10), fg="black")
stock1.place(x=130, y=15, width=60, height=20)
stock2 = tk.Text(root, font=("Arial", 10), fg="black")
stock2.place(x=200, y=15, width=60, height=20)
stock3 = tk.Text(root, font=("Arial", 10), fg="black")
stock3.place(x=270, y=15, width=60, height=20)  # Corrected to stock3.place()
stock4 = tk.Text(root, font=("Arial", 10), fg="black")
stock4.place(x=340, y=15, width=60, height=20) 
#amount
amount1 = tk.Text(root, font=("Arial", 10), fg="black")
amount1.place(x=130, y=55, width=60, height=20)
amount2 = tk.Text(root, font=("Arial", 10), fg="black")
amount2.place(x=200, y=55, width=60, height=20)
amount3 = tk.Text(root, font=("Arial", 10), fg="black")
amount3.place(x=270, y=55, width=60, height=20)
amount4 = tk.Text(root, font=("Arial", 10), fg="black") 
amount4.place(x=340, y=55, width=60, height=20)
# enterprice
entery_price1=tk.Text(root, font=("Arial", 10), fg="black")
entery_price1.place(x=130, y=95, width=60, height=20)
entery_price2=tk.Text(root, font=("Arial", 10), fg="black")
entery_price2.place(x=200, y=95, width=60, height=20)
entery_price3=tk.Text(root, font=("Arial", 10), fg="black")
entery_price3.place(x=270, y=95, width=60, height=20)
entery_price4=tk.Text(root, font=("Arial", 10), fg="black")
entery_price4.place(x=340, y=95, width=60, height=20)
#risk
risk1=tk.Text(root, font=("Arial", 10), fg="black")
risk1.place(x=130, y=135, width=60, height=20)
risk2=tk.Text(root, font=("Arial", 10), fg="black")
risk2.place(x=200, y=135, width=60, height=20)
risk3=tk.Text(root, font=("Arial", 10), fg="black")
risk3.place(x=270, y=135, width=60, height=20)
risk4=tk.Text(root, font=("Arial", 10), fg="black")
risk4.place(x=340, y=135, width=60, height=20)
#reward
reward1=tk.Text(root, font=("Arial", 10), fg="black")
reward1.place(x=130, y=175, width=60, height=20)
reward2=tk.Text(root, font=("Arial", 10), fg="black")
reward2.place(x=200, y=175, width=60, height=20)
reward3=tk.Text(root, font=("Arial", 10), fg="black")
reward3.place(x=270, y=175, width=60, height=20)
reward4=tk.Text(root, font=("Arial", 10), fg="black")
reward4.place(x=340, y=175, width=60, height=20)

#---------------------------map function 
def d_clear_terminal():
    clear_cli()

def d_open_code ():    
    vs_code ()

def xls_bank():
    bank()

def broker_dep():
  broker(budget) 
  broker.result()
  
def db_get_stock_list(y,stocks): 
    data_base(y,stocks)

def d_info_stock():
    cal_info_stock()

def cal_amount_carolation():
    amount_crolation()

def cal_v_r_r():
    value_risk_reward()

def my_stock_value():
    protfolio_value(stocks)
    protfolio_value.result()

def d_new_line():
    print("\n")

# label function
def gui_label_result(stocks,last_acount_broker): 
    start_year=stock_start_year 
    broker_balance=list(last_acount_broker.values())[-1]

    if broker_balance > start_year:
        broker_coler="gold"
    else:
        broker_coler="red"

    costs =0
    today_worth=0
    for stock in stocks: # buy values
        costs += stock['cost']
        today_worth+=stock['amount']*float(price_now(stock['tkr'])[0])
    
    if today_worth > costs:
        costs_color="green"
    else:
        costs_color="red"

    label1 = tk.Label(root, text=f"start year: {start_year}$   last_check {broker_balance}$   {broker_balance-start_year}$"
                      f"   prosent: {((broker_balance-start_year)/start_year)*100:.2f}%", font=("david", 14), bg="black", fg="white")
    label1.place(x=10, y=350)
    
    label = tk.Label(root, text=f"--------------------------------", font=("david", 14), bg="black", fg="white")
    label.place(x=10, y=370)
    
    label2 = tk.Label(root, text=f"cost: {costs:.2f}$   today: {today_worth:.2f}$  {today_worth-costs:.2f}", font=("david", 14), bg="black", fg=costs_color)
    label2.place(x=10, y=390)    
    
def alerts(stocks):
    y=0
    for i in stocks:
        stock = finvizfinance(i['tkr'])
        a = stock.ticker_fundament()
        now_price = float(a['Price'])
        
        if now_price > i['reward']:
            label3 = tk.Label(root, text=f"sell {i['tkr']} now price: {now_price}  reward: {i['reward']}", font=("david", 14), bg="black", fg="white")
            label3.place(x=10, y=440+y)
            y+=20            
        if now_price < i['risk']:
            label3 = tk.Label(root, text=f"sell {i['tkr']} now price: {now_price}  risk: {i['risk']}", font=("david", 14), bg="black", fg="white")
            label3.place(x=10, y=440+y)
            y+=20            


#----------------- runer at start as labels
# acount - label        
gui_label_result(stocks,last_acount_broker)
alerts(stocks)

#--------------------------- click 
clear_terminal = tk.Button(root, text="clear terminal", font=("ariel", 10), command=lambda:d_clear_terminal())
clear_terminal.place(x=450, y=20, width=100, height=16)
open_code = tk.Button(root, text="7up in vs", font=("ariel", 10), command=lambda:d_open_code())
open_code.place(x=450, y=40, width=100, height=16)
bank_explore = tk.Button(root, text="bank_eXls", font=("ariel", 10), command=lambda:xls_bank())
bank_explore.place(x=450, y=60, width=100, height=16)
broker_deposit = tk.Button(root, text="broker deposit", font=("ariel", 10), command=lambda:broker_dep())
broker_deposit.place(x=450, y=80, width=100, height=16)
# reset
reset_stock_list = tk.Button(root, text="reset", font=("ariel", 10), command=lambda:db_get_stock_list(y=3,stocks=stocks))
reset_stock_list.place(x=450, y=120, width=100, height=40)
#\n
new_line = tk.Button(root, text="new line", font=("ariel", 10), command=lambda:d_new_line())
new_line.place(x=450, y=170, width=100, height=40)
# new stock only = stocks
new_stock_list = tk.Button(root, text="new-stock-only", font=("ariel", 10), command=lambda:db_get_stock_list(y=0,stocks=stocks))
new_stock_list.place(x=10, y=250, width=100, height=20)
# db stock only = stocks
db_stock_list = tk.Button(root, text="db-stock-only", font=("ariel", 10), command=lambda:db_get_stock_list(y=1,stocks=stocks))
db_stock_list.place(x=120, y=250, width=100, height=20)
# mix db and new stock only = stocks
mix_stock_list = tk.Button(root, text="db+new-stocks", font=("ariel", 10), command=lambda:db_get_stock_list(y=2,stocks=stocks))
mix_stock_list.place(x=230, y=250, width=100, height=20)
#info_stock
info_stock = tk.Button(root, text="info_stock", font=("ariel", 10), command=lambda:d_info_stock())
info_stock.place(x=10, y=280, width=100, height=20)
#simpel carolation
simpel_crolation = tk.Button(root, text="simpel carolation", font=("ariel", 10), command=lambda:cal_simpel_crolation())
simpel_crolation.place(x=120, y=280, width=120, height=20)
#amount carolation
amount_carolation = tk.Button(root, text="amount-carolathion", font=("ariel", 10), command=lambda: cal_amount_carolation())
amount_carolation.place(x=250, y=280, width=120, height=20)
#simpel value and risks
v_r_r = tk.Button(root, text="value-risk", font=("ariel", 10), command=lambda: cal_v_r_r())
v_r_r.place(x=380, y=280, width=120, height=20)
# my stocks
my_value = tk.Button(root, text="my-stock", font=("ariel", 10), command=lambda: my_stock_value())
my_value.place(x=10, y=310, width=120, height=20)

#--------------------------- main Tk
root.mainloop()