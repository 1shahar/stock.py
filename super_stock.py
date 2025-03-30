from liberys import *
from db import *

#________________alert______________________
def alert(stocks):
    for i in stocks:
        price_now_i =float(price_now(i['tkr'])[0])
        print (f'{i['tkr']} price now {price_now_i} risk: {i['risk']} reword: {i['reward']}') 

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

#_________________broker deposit______________________
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
        print(f'broker deposit up for today {cls.balance}  {cls.balance/(float(USD_ILS())):.2f}$')
        return cls.balance
    
#-------------------my stock info---------------------

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

            print(f'{i['tkr']:4} cost: {cost:.2f}$  now:{self.now_value:8}$  Profit: {self.profit_value:8.2f}$ {self.prosent:8.2f}%  '
                f'Profit:{i['reward']:6.2f} {self.reward_value:6.2f}$  Stop:{i['risk']:6.2f} {self.stop_value:6.2f}$ ')

            return self.now_value
       
    @classmethod
    def result(cls):
        print("\n")
        print (f' total buy: {cls.buy}$ ')
        print (f' total now value: {cls.now_value}$ ')
        print (f' total profit: {cls.profit}$ ')
        if cls.buy!=0:
            print (f' total profit %: {(cls.profit/cls.buy)*100:.2f}% ')
        print (f' total risk: {cls.risk}$ ')
        print (f' total reward: {cls.reward}$ ')
        print("\n")

#-------------------my stock coronation --------------------- 
class carolation_check():
    def __init__(self,stocks=[],new_stock="",add_protfolio_value=0,setb=""):
        self.setb=setb
        self.stocks=stocks
        self.new_stock=new_stock
        self.add_protfolio_value=add_protfolio_value
        self.get_corolathion()

    
    def get_corolathion(self,corelation_time='1mo'):
        
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

        if self.setb!="b2":
            stock_value=[]
            wigete = []
            for i in stocks:
                if i["amount"]:
                    #stock_value
                    stock_value.append(float(i["amount"])*(float(price_now(i["tkr"])[0])))
                t_stock_value=sum(stock_value)
                print(f"protfolio total value = {t_stock_value}\n")

                for i in stocks:
                #wi (stock_value/total_value)
                    wigete.append((float(i["amount"])*(float(price_now(i["tkr"])[0])/t_stock_value)))
                    print(f"stock {i['tkr']} wighet {((float(i["amount"])*(float(price_now(i["tkr"])[0])/t_stock_value))*100):.2f}%")
                
                index_wi=0  
                portfolio_coronation=0
                ct = ct=self.one_line_correlations.to_dict()
                for i in ct:
                    portfolio_coronation+=round(wigete[index_wi]*ct[i],2)
                    index_wi+=1
                print(f"\n portfolios corelation: {portfolio_coronation}")

        
#-------------------- new stock--------------------------------------   
class build_instance:
    def __init__(self,tkr=""):
        self.tkr=tkr
        self.now_price,self.div = price_now(self.tkr)
        print(f'{self.tkr} price: {self.now_price} div: {self.div}$ {self.div/12:.2f}$\n')
        self.get_cost_div()

    
    def get_cost_div(self):
        while True:
            self.enter_price = input(f'insert price order of {self.tkr}: ')
            self.enter_price =float(self.enter_price )
            self.amount = input(f'insert amount amount of {self.tkr}: ')
            self.amount=int(self.amount)
            self.cost = (self.amount*self.enter_price)+2.5
            self.real_price=self.cost/self.amount
            print(f"{self.tkr} real price: {self.real_price:.2f}$ cost: {self.cost:.2f}$ {self.cost*float(USD_ILS()):.2f} div: {float((self.div/12)*self.amount):.2f} {float((self.div/12)*self.amount)*float(USD_ILS()):.2f}")
            user=input("\nEnter '1' to continue any key to change ")
            if user =="1":
                print("\n")
                break
            else:
                print("\n")
        self.risk()

    def risk(self):
        while True:
            self.risk_price = input(f'insert risk price of {self.tkr} : ')
            self.risk_price=float(self.risk_price)
            self.stop_value=(self.amount*self.risk_price)-self.cost+-2.5
            self.reward = input(f'insert price of {self.tkr} reward: ')
            self.reward=float(self.reward)
            self.reward=(self.reward)
            self.reward_value=(self.amount*self.reward)-self.cost-2.5
            print(f"{self.tkr} stop value: {self.stop_value}$ {self.stop_value*float(USD_ILS()):.2f} reward value: {self.reward_value}$ {self.reward_value*float(USD_ILS()):.2f}\n")
            user=input("insert '1' to create instance any key to change or 0 to exit without ")
            if user=="0":
                break
            if user =="1":
                print("\n")
                print(f"'tkr':'{self.tkr}','amount':{self.amount},'enter_price':{self.enter_price},'cost':0,'risk':{self.risk_price:.2f},'reward':{self.reward:.2f}") 
                break
            else:
                print("\n")



#-------------------- balance corelation 0--------------------------------------   
class stocks_balance:
    def __init__(self,stocks):
        self.stocks=stocks
        print ("\n")
        carolation_check(stocks)
        good_amount= ""
        print ("\n")
        print("insert new amount of stock check carolation result")
        print("--------------------------------------------")
        
        while good_amount !="y":
            for stock in stocks:
                print(stock["tkr"] , stock['amount'])
                stock["amount"] = input ("new amount ? " )

            print ("\n")
            for stock in stocks:
                print (f"{stock['tkr']} amount:{stock['amount']}")
            carolation_check(stocks)
            good_amount = input("if the corlation good y/n ? " )


#-------------------- change amount for--------------------------------------   
class changes():
    def __init__(self,stocks=[]):
        self.stocks=stocks
        new_stock=[]
        print ("insert new amount hold if no change press enter")
        print ("-----------------------------------------------")
        profit=0
        for stock in self.stocks:
            new_amount = input (f"stock: {stock['tkr']} amount: {stock['amount']} price: {float(price_now(stock["tkr"])[0])} new amount ? " )
            if new_amount !="":
                new_amount=int(stock['amount'])+int(new_amount)
                delta_amount = new_amount - int(stock['amount'])
                cange_value=float(price_now(stock["tkr"])[0])* delta_amount
                new_stock.append(f"stock :{stock['tkr']},amount_change:{delta_amount} ,value: {cange_value:.2f}")
                profit += cange_value

        print("\n")
        for i in new_stock:
            print(i)

        print (f'\ntotal profit {profit}$ {profit*float(USD_ILS()):.2f} ')


#-------------------- get from input price and div ----------------------8
def get_price_div():
    stock_lis = []
    stock="spy"
    while stock!="":
        stock = input("what the tkr ? (press enter to continue) " )
        if stock =="":
            break
        else:
            stock_lis.append(stock) 
    for i in stock_lis:
        try:
            print (f" {i} {price_now(i)}")
        except:
            print (f"{i} not found")
   
 