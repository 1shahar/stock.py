#instance
stocks = ['spyi','sh'] 
investment_amount = 10000  # balance all stock by value -- if investment_amount > 0
#------------------------------------------------------------------------------------------
priceDiv(stocks) # stock info
#-----------------------------------------insert stocks-------------------------------------------------
print("\n---cost and risk--")

Firstcost(tkr="s",amount=0,div=0,enter_price=0,risk=0,profit=0, tax=2.5) # check cost and risk 

print("\n")
#------------------------------------------------------------------------------------------
# check caroltion 
print("------stock_carolation ------")
tickers = stocks
period = '1mo'
analyzer = StockAnalyzer()
for ticker in tickers:
    analyzer.add_stock(ticker, period)
analyzer.display_correlation_matrix()
print("\n")
#------------------------------------------------------------------------------------------
if investment_amount != 0:
    # balance all stock 
    print("------balance all stock------")
    analyzer = StockBalancer()
    for i in stocks:
        analyzer.add_stock(i, "1y")
    analyzer.display_allocations(investment_amount)
    print("\n")

#------------------------------------------------------------------------------------------
                        # final line insert holds
#------------------------------------------------------------------------------------------
# My stock 
print("------My-stock------")
spyi=Protfolio_stock(tkr="spyi", amount=100 , enter_price=0 , risk=24 , reword=35 , tax= 2.5 ) 
spyi.update(amount=1+1,buy_value=50+50,get_div=0,pay_tax=0)

#------------------------------------------------------------------------------------------
Protfolio_stock.mystock_total()
#------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------