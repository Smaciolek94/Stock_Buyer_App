import Stock_App as sa
import ImpExp as ie
import pandas as pd
import os

path = "shares.csv"

shares = ie.importer(path)
symbols = ["SCHB","SCHZ","SCHP","SCHF","SCHE","SCHH"]
allocation = [.35,.25,.05,.15,.10,.10]

myApp = sa.Stocks(symbols,shares,allocation)

symbolprint = []
for i in range(0,len(myApp.symbols)):
    s1 = symbols[i]+": "
    symbolprint.append(s1)
    
print("You hold the following")
print(pd.DataFrame({"symbol":symbolprint,"Shares Held":myApp.shares}))
correct1 = input("Is this correct (y/n)?")
while correct1 != "y":
    newshares = []
    for i in range(0,len(myApp.shares)):
        s = input("enter the correct number of shares for "+symbolprint[i])
        s = float(s)
        newshares.append(s)
    myApp.updateshares(newshares)
    print("You hold the following")
    print(pd.DataFrame({"symbol":symbolprint,"Shares Held":myApp.shares}))
    correct1 = input("Is this correct (y/n)?")
    
print("This is your desired allocation")
print(pd.DataFrame({"Symbol":symbolprint,"Allocation":myApp.alc}))
correct2 = input("Is this correct (y/n)?")
while correct2 != "y":
    newalc = []
    for i in range(0,len(myApp.alc)):
        s = input("enter the correct allocation for "+symbolprint[i])
        s = float(s)
        newalc.append(s)
    myApp.updatealc(newalc)
    if sum(newalc) != 1.0:
        print("Your Allocation must sum to 1")
        continue
    print("This is your desired allocation")
    print(pd.DataFrame({"Symbol":symbolprint,"Allocation":myApp.alc}))
    correct2 = input("Is this correct (y/n)?")
    
bs = input("Do you wish to buy(b) or sell(s) ")
while bs != "b" and bs != "s":
    bs = input("You need to input either b or s")
if bs == "b":
    cash = input("How much cash do you have?")
    cash = float(cash)
    print("calculating.....")
    myApp.buyer(cash)   
if bs == "s":
    takeout = input("How much cash do you need to withdraw?")
    takeout = float(takeout)
    cash=input("How much cash is already in the account?")
    cash =float(cash)
    print("calculating.....")
    myApp.seller(takeout,cash)
    
ie.exporter(path,myApp.shares)

k=input("press any key to exit") 