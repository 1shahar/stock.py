from db import *
from super_stock import *


def setup(y):
    if y == "": (print("\n"), alert(stocks), print("\n"))
    
    if y == "0": (exit())
    
    if y == "00": (print("\n"), get_price_div(), print("\n"))
    
    if y == "1": (print("\n"), bank(), print("\n"))
    
    if y == "10": (print("\n"), broker(budget).result(), print("\n"))
    
    if y == "b2":
        tkr=input ("tkr ? ")
        tkr_price=price_now(tkr)
        new_tkr={'tkr':tkr}
        stocks.append(new_tkr)
        carolation_check(stocks,setb="b2")
        

    if y == "b3":
        tkr=input ("tkr ? ")
        tkr_price=price_now(tkr)
        new_tkr={'tkr':tkr}
        stocks.append(new_tkr)
        stocks_balance(stocks)
    
    if y == "fb":
        build_instance(tkr=input("tkr ? "))
        
        
    if y == "c1": (print("\n"), protfolio_value(stocks), protfolio_value.result(), print("\n"))
        
    if y == "c2": (print("\n"), carolation_check(stocks), print("\n"))
    if y == "c3": (print("\n"), changes(stocks), print("\n"))
        
        # finel set enter get instance risk value
        #carolation_check(stocks) #check carolation 

        # continue to info 

    if y == "5": build_instance(tkr=input("insert the new tkr ? "))
    if y == "6": (print("\n"), stocks_balance(stocks), print("\n"))

def user_press():
    y = input ("""
    0. exit 
    -----bank------
            1. bank xls present 
               
    -----broker------
            10. broker acount
               
    -----stock------
        !!! enter for alert 
        !!! 0. to exit
            ___buy:___       
                b1. level-1-check -- check list of tkrs for price and div
                b2. level-2-check -- input tkr - get: price , corelation 
                b3. level-3- set amounts by corelation for input new tkr

            ___check:___       
                c1. my stock info
                c2. corelation info       
                c3. calculate profit change unit amount 
        00. from input get stock price and div               
        """)
    
    return y

while True:
    print("\n") 
    print (f"Usd-Nis__{USD_ILS()} spy__{price_now("spy")[0]}$ ")
    y=user_press()
    setup(y)

