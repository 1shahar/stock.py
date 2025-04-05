# runner main window

from db import *
from setup import *
import tkinter as tk 

all_stock = [] 
#main window 
root = tk.Tk()
root.title("Stock Analysis")
root.geometry("600x600")
root.configure(bg="black")



label = tk.Label(root, text="stocks", font=("Arial", 18), bg="black", fg="white")
label.place(x=100, y=10)
label = tk.Label(root, text="amount", font=("Arial", 18), bg="black", fg="white")
label.place(x=95, y=80)
label = tk.Label(root, text="entery price", font=("Arial", 18), bg="black", fg="white")
label.place(x=80, y=140)

label = tk.Label(root, text="risk price", font=("Arial", 18), bg="black", fg="white")
label.place(x=95, y=200)

label = tk.Label(root, text="reward price", font=("Arial", 18), bg="black", fg="white")
label.place(x=80, y=260)

broker(budget)
my_broker = broker.result()
label = tk.Label(root, text=f"{my_broker}", font=("Arial", 10), bg="black", fg="white")
label.place(x=10, y=450)


# input new stock 
stock1 = tk.Text(root, font=("Arial", 10), fg="black")
stock1.place(x=10, y=60, width=60, height=20)
amount1 = tk.Text(root, font=("Arial", 10), fg="black")
amount1.place(x=10, y=110, width=60, height=20)
entery_price1=tk.Text(root, font=("Arial", 10), fg="black")
entery_price1.place(x=10, y=180, width=60, height=20)
risk1=tk.Text(root, font=("Arial", 10), fg="black")
risk1.place(x=10, y=240, width=60, height=20)
reward1=tk.Text(root, font=("Arial", 10), fg="black")
reward1.place(x=10, y=300, width=60, height=20)


stock2 = tk.Text(root, font=("Arial", 10), fg="black")
stock2.place(x=80, y=60, width=60, height=20)
amount2 = tk.Text(root, font=("Arial", 10), fg="black")
amount2.place(x=80, y=110, width=60, height=20)
entery_price2=tk.Text(root, font=("Arial", 10), fg="black")
entery_price2.place(x=80, y=180, width=60, height=20)
risk2=tk.Text(root, font=("Arial", 10), fg="black")
risk2.place(x=80, y=240, width=60, height=20)
reward2=tk.Text(root, font=("Arial", 10), fg="black")
reward2.place(x=80, y=300, width=60, height=20)

stock3 = tk.Text(root, font=("Arial", 10), fg="black")
stock3.place(x=150, y=60, width=60, height=20)  # Corrected to stock3.place()
amount3 = tk.Text(root, font=("Arial", 10), fg="black")
amount3.place(x=150, y=110, width=60, height=20)
entery_price3=tk.Text(root, font=("Arial", 10), fg="black")
entery_price3.place(x=150, y=180, width=60, height=20)
risk3=tk.Text(root, font=("Arial", 10), fg="black")
risk3.place(x=150, y=240, width=60, height=20)
reward3=tk.Text(root, font=("Arial", 10), fg="black")
reward3.place(x=150, y=300, width=60, height=20)

stock4 = tk.Text(root, font=("Arial", 10), fg="black")
stock4.place(x=220, y=60, width=60, height=20) 
amount4 = tk.Text(root, font=("Arial", 10), fg="black") 
amount4.place(x=220, y=110, width=60, height=20)

entery_price4=tk.Text(root, font=("Arial", 10), fg="black")
entery_price4.place(x=220, y=180, width=60, height=20)
risk4=tk.Text(root, font=("Arial", 10), fg="black")
risk4.place(x=220, y=240, width=60, height=20)
reward4=tk.Text(root, font=("Arial", 10), fg="black")
reward4.place(x=220, y=300, width=60, height=20)


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')



new_stock = []
def freset_data():
    global new_stock 
    new_stock = []
    global all_stock   
    all_stock = [] 
    

def fpull_data():  
    global all_stock
    global new_stock
      
    stock1_value = stock1.get("1.0", tk.END).strip()
    if stock1_value:
        new_stock.append({'tkr':stock1_value})
        amount_value = amount1.get("1.0", tk.END).strip()
        if amount_value:
            new_stock[0]["amount"] = int(amount_value)
        entery_price1_value = entery_price1.get("1.0", tk.END).strip()
        if entery_price1_value:
            new_stock[0]["entery_price"] = float(entery_price1_value)
        risk1_value = risk1.get("1.0", tk.END).strip()
        if risk1_value:
            new_stock[0]["risk"] = float(risk1_value)
        reward1_value = reward1.get("1.0", tk.END).strip()
        if reward1_value:
            new_stock[0]["reward"] = float(reward1_value)    
    
    
    stock2_value = stock2.get("1.0", tk.END).strip()
    if stock2_value:
        new_stock.append({'tkr':stock2_value})
        amount_value = amount2.get("1.0", tk.END).strip()
        if amount_value:
            new_stock[1]["amount"] = int(amount_value)
        entery_price2_value = entery_price2.get("1.0", tk.END).strip()
        if entery_price2_value:
            new_stock[1]["entery_price"] = float(entery_price2_value)
        risk2_value = risk2.get("1.0", tk.END).strip()
        if risk2_value:
            new_stock[1]["risk"] = float(risk2_value)
        reward2_value = reward2.get("1.0", tk.END).strip()
        if reward2_value:
            new_stock[1]["reward"] = float(reward2_value)

    stock3_value = stock3.get("1.0", tk.END).strip()
    if stock3_value:
        new_stock.append({'tkr':stock3_value})
        amount_value = amount3.get("1.0", tk.END).strip()
        if amount_value:
            new_stock[2]["amount"] = int(amount_value)
        entery_price3_value = entery_price3.get("1.0", tk.END).strip()
        if entery_price3_value:
            new_stock[2]["entery_price"] = float(entery_price3_value)
        risk3_value = risk3.get("1.0", tk.END).strip()
        if risk3_value:
            new_stock[2]["risk"] = float(risk3_value)
        reward3_value = reward3.get("1.0", tk.END).strip()
        if reward3_value:
            new_stock[2]["reward"] = float(reward3_value)

    stock4_value = stock4.get("1.0", tk.END).strip()
    if stock4_value:
        new_stock.append({'tkr':stock4_value})
        amount_value = amount4.get("1.0", tk.END).strip()
        if amount_value:
            new_stock[3]["amount"] = int(amount_value)
        entery_price4_value = entery_price4.get("1.0", tk.END).strip()  
        if entery_price4_value:
            new_stock[3]["entery_price"] = float(entery_price4_value)
        risk4_value = risk4.get("1.0", tk.END).strip()
        if risk4_value:
            new_stock[3]["risk"] = float(risk4_value)
        reward4_value = reward4.get("1.0", tk.END).strip()
        if reward4_value:
            new_stock[3]["reward"] = float(reward4_value)

    for i in stocks:
        all_stock.append(i)

    for i in new_stock:
        if i:
            all_stock.append(i)


#------------------------------------------------------------------------------------------
#system button
bclear_screen = tk.Button(root, text="clear the terminal", font=("ariel", 10), command=lambda:clear(),fg="red",bg="black")
bclear_screen.place(x=250, y=20, width=120, height=20)

pull_data = tk.Button(root, text="pull_data", font=("ariel", 10), command=lambda:fpull_data())
pull_data.place(x=300, y=60, width=60, height=20)
reset_data = tk.Button(root, text="reset_data", font=("ariel", 10), command=lambda:freset_data())
reset_data.place(x=370, y=60, width=80, height=20)

#function button
get_price = tk.Button(root, text="get price_div", font=("ariel", 10), command=lambda: price(new_stock))
get_price.place(x=300, y=100, width=90, height=20)

get_price = tk.Button(root, text="carolathion_set", font=("ariel", 10), command=lambda: corelation(all_stock))
get_price.place(x=300, y=130, width=120, height=20)

get_price = tk.Button(root, text="cost_risk", font=("ariel", 10), command=lambda: build_values_instance(new_stock))
get_price.place(x=300, y=160, width=120, height=20)

alerts = tk.Button(root, text="alert", font=("ariel", 10), command=lambda: alert(stocks))
alerts.place(x=300, y=240, width=60, height=20)

my_sto = tk.Button(root, text="my-stock", font=("ariel", 10), command=lambda: my_stock_value())
my_sto.place(x=370, y=240, width=60, height=20)

change_amount_crolathion = tk.Button(root, text="set amount caroltion", font=("ariel", 10), command=lambda: stocks_balance(all_stock))
change_amount_crolathion.place(x=440, y=240, width=140, height=20)

bank_sumry = tk.Button(root, text="bank-summruy", font=("ariel", 10), command=lambda: bank())
bank_sumry.place(x=10, y=500, width=90, height=20)


#bank & broker






# def set_carolation(new_stock=[]):
#     for i in new_stock:
#         if i:
#             stocks.append(i)
#     corelation(stocks)


root.mainloop()