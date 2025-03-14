from main import *
#instance
# stock to check price and div
print("------stock_info ------")
priceDiv(["spy", 'sh'])
#------------------------------------------------------------------------------------------
# check cost of stock
print("------stock_new-Cost ------")
Firstcost(tkr="spyi", amount=109,div=0 ,enter_price=0, tax=2.5)
#------------------------------------------------------------------------------------------
# stop loast and take profit
print("------stock_stop_loss ------")
StopProfit(tkr="spy",buy_value=5000 ,amount=109, stop_loss=45, take_profit=55) 
#------------------------------------------------------------------------------------------
# check caroltion 
print("------stock_carolation ------")
tickers = ['spyi','sh','msty']
period = '1mo'
analyzer = StockAnalyzer()
for ticker in tickers:
    analyzer.add_stock(ticker, period)
analyzer.display_correlation_matrix()
#------------------------------------------------------------------------------------------
# balance 2 stock 
print("------balance 2 stock------")
balance_2_stock(price_stock_A = 50,price_stock_B = 45,investment_amount = 5000)
#------------------------------------------------------------------------------------------
# balance all stock 
print("------balance all stock------")
analyzer = StockBalancer()
analyzer.add_stock("SPY", "1y")
analyzer.add_stock("SH", "1y")
investment_amount = 10000  # Example investment amount
analyzer.display_allocations(investment_amount)
#------------------------------------------------------------------------------------------
# My stock 
print("------My-stock------")
spyi=Protfolio_stock(tkr="spyi", amount=100 , enter_price=0 , risk=24 , reword=35 , tax= 2.5 ) 
spyi.update(amount=1+1,buy_value=50+50,get_div=0,pay_tax=0)


Protfolio_stock.mystock_total()